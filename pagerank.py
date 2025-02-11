import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str, help="Input file with the graph")
    parser.add_argument("d", type=float, help="Teleporting parameter")
    args = parser.parse_args()
