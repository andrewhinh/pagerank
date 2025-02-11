import argparse
import random
import time

import numpy as np


def main(input_file: str, d: float, epsilon: float, max_results: int = None):
    webpages = {}
    with open(input_file) as f:
        for line in f:
            webpage, *outgoing_edges = line.strip().split(":")
            webpages[webpage] = list(map(int, outgoing_edges[0].split(",")))

    N = max(int(webpage) for webpage in webpages.keys()) + 1
    v = np.array([1 / N for _ in range(N)])
    M = np.zeros((N, N))
    for webpage, outgoing_edges in webpages.items():
        for outgoing_edge in outgoing_edges:
            M[int(webpage), outgoing_edge] = 1 / len(outgoing_edges)

    while True:
        v_new = d * M @ v + (1 - d) / N
        if np.isclose(v, v_new, atol=epsilon).all():
            break
        v = v_new

    if not max_results:  # running program against given input file
        for webpage, value in enumerate(v):
            print(f"{value:.10f}")
    else:  # running experiment
        sorted_indices = np.argsort(-v)[:max_results]
        for idx in sorted_indices:
            print(f"{idx}: {v[idx]:.10f}")
        print(f"Mean (v): {np.mean(v):.10f}")
        print(f"Std (v): {np.std(v):.10f}")


def experiment(seed: int, n_max_conn: int, epsilon: float, max_results: int):
    random.seed(seed)

    # generate 10000 random webpages where each webpage has anywhere from 0 to n_max_conn outgoing edges
    outfile = f"gen_{seed}_{n_max_conn}_{epsilon}_{max_results}.txt"
    with open(outfile, "w") as f:
        for i in range(10000):
            n_conn = random.randint(0, n_max_conn)
            outgoing_edges = (
                ",".join(str(edge) for edge in random.sample(range(10000), n_conn))
                if n_conn > 0
                else ""
            )
            if outgoing_edges:
                f.write(f"{i}: {outgoing_edges}\n")
        f.flush()

    for d in np.linspace(0.75, 0.95, num=5, endpoint=True):
        print(f"Running experiment with d={d:.2f}")
        print(f"Top {max_results} web page ranks:")
        start = time.monotonic_ns()
        main(outfile, d, epsilon, max_results)
        print(
            f"Experiment completed in {round((time.monotonic_ns() - start) / 1e9, 2)} seconds"
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "inp",
        type=str,
        help="Input file with the graph",
        nargs="?",
        default="input.txt",
    )
    parser.add_argument(
        "d", type=float, help="Teleporting parameter", nargs="?", default=0.8
    )
    parser.add_argument("--eps", type=float, help="Convergence epsilon", default=1e-10)
    parser.add_argument(
        "--test",
        action="store_true",
        help="Whether to run the program or just experiment",
    )
    parser.add_argument("--seed", type=int, help="Random seed", default=0)
    parser.add_argument(
        "--n_max_conn",
        type=int,
        help="Maximum number of connections per webpage",
        default=10,
    )
    parser.add_argument(
        "--max_results",
        type=int,
        help="Maximum number of results to print",
        default=10,
    )

    args = parser.parse_args()
    if not args.test:
        main(args.inp, args.d, args.eps, args.max_results)
    else:
        experiment(args.seed, args.n_max_conn, args.eps, args.max_results)
