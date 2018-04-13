
import sys
import argparse


def main(argv=False):
    argv = (argv or sys.argv)[1:]

    parser = argparse.ArgumentParser(description='FPM Benchmark')
    namespace = parser.parse_args(argv)

    print("done")

    return 0


if __name__ == '__main__':
    if sys.version < '3':
        print("Only Python 3 is supported - you are using version %d.%d" % sys.version_info[:2])
    else:
        sys.exit(main());
