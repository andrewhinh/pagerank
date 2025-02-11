# pagerank

Implementation of PageRank.

## setup

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync
```

## run

```bash
uv run pagerank.py input.txt .75 > output.txt
```

## report

Create a web graph with 10,000 webpages. The value of d changes the PageRank vector. You
will vary d between .75 and .95 with 0.05 increment to see how the PageRank vector changes.

- What convergence criterion did you use? How long did your PageRank algorithm
  converge in one run on average?
  - The PageRank algorithm converges when the change in the PageRank vector is less than 1e-6 between iterations.
- How different are the top sites for each d? How different are the PageRanks of the top sites? How does the PageRank vector change as a whole? Write any observations you find.
  - The PageRanks of the top sites are not very different. The PageRank vector is not very different.
