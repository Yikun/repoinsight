# Repo Insight
Gain insights into the status and history of open source project.

# Install
```shell
git clone https://github.com/Yikun/repoinsight.git
cd repoinsight
pip install -e .
```


# Usage

- **Repo Commit Insights**: `repoinsight commits apache/spark --since 2021-01-01`

``` Shell
$ git clone git@github.com:apache/spark.git
$ git clone git@github.com:apache/spark-website.git
$ repoinsight commits apache/spark --since 2021-01-01
1.	85	Max Gekk
2.	54	Dongjoon Hyun
3.	35	HyukjinKwon
4.	30	Kousuke Saruta
5.	26	Wenchen Fan
6.	24	Kent Yao
7.	23	Yuming Wang
8.	19	yangjie01
9.	18	Liang-Chi Hsieh
10.	18	ulysses-you
11.	18	Angerszhuuuu
12.	17	Terry Kim
13.	16	Ruifeng Zheng
14.	16	Cheng Su
15.	13	gengjiaan
16.	13	Gengliang Wang
17.	13	Chao Sun
18.	12	“attilapiros”
19.	11	yi.wu
20.	9	angerszhu
21.	8	William Hyun
22.	8	Holden Karau
23.	7	beliefer
24.	7	attilapiros
25.	6	Anton Okolnychyi
26.	5	Sean Owen
27.	5	tanel.kiis@gmail.com
28.	5	Erik Krogen
29.	5	Yikun Jiang
30.	5	Gabor Somogyi
# ... ...
```

- **Repo Review Insights**: `repoinsight review apache/spark --since 2021-01-01`

``` Shell
$ repoinsight review apache/spark --since 2021-01-01
Fetch 1000+ Pull Requests  [####################################]  1259/1000
Processing Pull Requests  [####################################]  100%
1.      260     cloud-fan
2.      236     HyukjinKwon
3.      198     dongjoon-hyun
4.      119     maropu
5.      94      viirya
6.      72      srowen
7.      26      yaooqinn
8.      17      wangyum
9.      15      imback82
10.     13      HeartSaVioR
# ... ...
```