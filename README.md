# pagerank

Implementation of PageRank.

## setup

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync
```

## usage

Run program on given `input.txt`:

```bash
uv run pagerank.py input.txt .8 >| output.txt
```

Run experiment with generated web graph and varying values of **d**:

```bash
uv run pagerank.py --test [--seed 0] [--n_max_conn 10] [--eps 1e-10] [--max_results 10]
```

## report

Result of running `uv run pagerank.py --test`:

```bash
Running experiment with d=0.75
Top 10 web page ranks:
5738: 0.0000964411
6865: 0.0000962075
2572: 0.0000956528
9820: 0.0000954522
8318: 0.0000953151
9979: 0.0000952536
479: 0.0000952536
8785: 0.0000951357
9198: 0.0000949689
1863: 0.0000949422
Mean (v): 0.0000782956
Std (v): 0.0000184202
Experiment completed in 4.81 seconds
Running experiment with d=0.80
Top 10 web page ranks:
5738: 0.0000933783
6865: 0.0000930294
2572: 0.0000922419
9820: 0.0000920136
8318: 0.0000918109
9979: 0.0000917217
479: 0.0000917217
8785: 0.0000916631
9198: 0.0000913720
8385: 0.0000912856
Mean (v): 0.0000730101
Std (v): 0.0000185526
Experiment completed in 5.7 seconds
Running experiment with d=0.85
Top 10 web page ranks:
5738: 0.0000876703
6865: 0.0000871808
2572: 0.0000861317
9820: 0.0000858972
8318: 0.0000856150
8785: 0.0000855467
479: 0.0000854936
9979: 0.0000854936
9198: 0.0000850873
1863: 0.0000849177
Mean (v): 0.0000656270
Std (v): 0.0000179626
Experiment completed in 7.14 seconds
Running experiment with d=0.90
Top 10 web page ranks:
5738: 0.0000766689
6865: 0.0000760473
2572: 0.0000747858
9820: 0.0000745811
8785: 0.0000742854
8318: 0.0000742241
9979: 0.0000740757
479: 0.0000740757
9198: 0.0000736454
1863: 0.0000733851
Mean (v): 0.0000545894
Std (v): 0.0000160582
Experiment completed in 9.29 seconds
Running experiment with d=0.95
Top 10 web page ranks:
5738: 0.0000539567
6865: 0.0000533381
2572: 0.0000521540
9820: 0.0000520286
8785: 0.0000518592
8318: 0.0000516732
9979: 0.0000515328
479: 0.0000515328
9198: 0.0000511727
9877: 0.0000509194
Mean (v): 0.0000362849
Std (v): 0.0000114514
Experiment completed in 12.79 seconds
```

The convergence criterion used was to exit the algorithm when the difference between successive PageRank vectors was less than **epsilon** (= 1e-10). As **d** increases, the time to convergence increases.

Across all experiments, the top pages are largely the same and there are only minor differences in the ordering of the lower positions. However, as **d** increases, the top PageRank value, overall mean, and overall standard deviation decrease. On the other hand, as **d** increases, the ratio of the standard deviation to the mean increases.

From the results above, it appears that lower **d** yields a smoother distribution with faster convergence, while higher **d** emphasizes the link structure which slows convergence and sharpens the differences among pages.
