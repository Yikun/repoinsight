from collections import Counter
from datetime import datetime

import click
from git import Repo
from github import Github, UnknownObjectException


@click.group()
@click.option('--token', envvar='GITHUB_AUTH_TOKEN')
def cli(token):
    if not token:
        raise click.ClickException('Please set `GITHUB_AUTH_TOKEN`...')
    cli.token = token


def time_condition(pull_request, since="2021-01-01"):
    return pull_request.updated_at > datetime.strptime(since, "%Y-%m-%d")


def _commits(name, since):
    datetime.strptime(since, "%Y-%m-%d")
    project = name.split('/')[-1]

    author_dict = Counter()
    author_email = {}

    try:
        repo = Repo('./' + project)
    except Exception:
        msg = "git clone https://github.com/%s.git" % name
        raise click.ClickException('Please clone project first:\n' + msg)

    out_format = '--pretty=format:%an|%ae'
    authors = repo.git.log(
        '--since', since, out_format
    ).replace('\\', '').split('\n')
    for author_raw in authors:
        user, email = author_raw.split('|')
        author_dict[user] += 1
        author_email[user] = email

    return author_dict


def _review(name, since):
    since_date = datetime.strptime(since, "%Y-%m-%d")
    g = Github(cli.token, per_page=100)
    try:
        issues = g.search_issues("repo:%s type:pr updated:>%s" % (name, since))
        pulls = g.get_repo(name).get_pulls(
            sort='updated', direction='desc', state='all'
        )
    except UnknownObjectException:
        raise click.ClickException('Repository not found!')

    reviewers = Counter()

    prs = []
    title = 'Fetch %d+ Pull Requests' % issues.totalCount
    with click.progressbar(
        pulls, length=issues.totalCount, show_pos=True, label=title
    ) as pulls:
        for pr in pulls:
            if time_condition(pr, since=since):
                prs.append(pr)
            else:
                break

    with click.progressbar(
        prs, length=len(prs),
        show_eta=True, label='Processing Pull Requests'
    ) as pulls:
        for pr in pulls:
            for rev in pr.get_reviews():
                if rev.state in ['APPROVED', 'REQUEST_CHANGES']:
                    if rev.submitted_at > since_date:
                        reviewers[rev.user.login] += 1

    display_user_counter(reviewers)


@cli.command()
@click.argument('name')
@click.option('--since', default='2021-01-01')
def commits(name, since):
    _counters = _commits(name, since)
    if name == "apache/spark":
        for other in ["apache/spark-website"]:
            _counters += _commits(other, since)
    display_user_counter(_counters)


@cli.command()
@click.argument('name')
@click.option('--since', default='2021-01-01')
def review(name, since):
    _review(name, since)


@cli.command()
@click.argument('name')
@click.option('--since', default='2021-01-01')
def show(name, since):
    _review(name, since)
    _counters = _commits(name, since)
    display_user_counter(_counters)


def display_user_counter(counter):
    curr = 1
    for item, i in sorted(counter.items(), key=lambda x: x[1], reverse=True):
        print(str(curr) + '.\t' + str(i) + '\t' + item + '\t')
        curr += 1


if __name__ == '__main__':
    cli()
