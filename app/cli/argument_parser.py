import argparse


def parse_args():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-j",
        "--job",
        default="repair_pending"
    )

    return parser.parse_args()
