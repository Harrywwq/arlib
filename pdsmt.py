# coding: utf-8
# pylint: disable=too-few-public-methods
# import time
import os
import signal
import psutil
from pdsmt.parallel_cdclt import parallel_cdclt


def signal_handler(sig, frame):
    """Captures the shutdown signals and cleans up all child processes of this process."""
    print("handling signals")
    parent = psutil.Process(os.getpid())
    for child in parent.children(recursive=True):
        child.kill()


def process_file(filename, logic):
    with open(filename, "r") as f:
        smt2string = f.read()
        # simple_cdclt(smt2string)
        ret = parallel_cdclt(smt2string, logic=logic)
        print(ret)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--prover', dest='prover', default='seq', type=str, help="The prover for using")
    parser.add_argument('--timeout', dest='timeout', default=8, type=int, help="timeout")
    parser.add_argument('--workers', dest='workers', default=4, type=int, help="workers")
    parser.add_argument('--verbose', dest='verbosity', default=1, type=int, help="verbosity")
    parser.add_argument('--logic', dest='logic', default='ALL', type=str, help="logic to use")
    parser.add_argument('infile', help='the input file (in SMT-LIB v2 format)')
    args = parser.parse_args()

    # Registers signal handler so we can kill all of our child processes.
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGQUIT, signal_handler)
    signal.signal(signal.SIGABRT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    process_file(args.infile, args.logic)
