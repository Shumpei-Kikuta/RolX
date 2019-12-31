"""
INPUT: struc2vec edgelist
OUTPUT: embedding file
"""

import argparse
import subprocess


def set_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, 
            help="file path of the edgelist struc2vec uses")
    # parser.add_argument("--output", required=True)
    parser.add_argument("--feature_num", type=int, default=64, required=True)
    parser.add_argument("--role_num", type=int, default=2, required=True)
    args = parser.parse_args()
    return args


def preprocess():
    """
    translate the file of the struc2vec edgelist to the file of rolx text
    """
    pass


def postprocess():
    """
    translate the file of the rolx emb to the file of the struc2vec emb
    """
    pass


def main():
    args = set_args()

    preprocess()

    cmd = "python src/main.py --input {} --dimensions {} --bins {}".format(
        args.input, args.feature_num, args.role_num)
    subprocess.call(cmd.split())

    postprocess()


if __name__ == '__main__':
    main()
