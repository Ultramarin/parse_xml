import argparse
import os
import sys
import lxml


help_message = ""
XML = ""

def test():
    pass

def main():
    if len(sys.argv) > 1:
        if "--help" in sys.argv and len(sys.argv) > 2:
            print("--help is single argument", file=sys.stderr)
            exit(10)
        else:
            try:
                parser = argparse.ArgumentParser(description='Process some integers.', add_help=False)
                parser.add_argument("--file", nargs=1, dest="file", required=True, type=str, )
                args = parser.parse_args()
                userOpts = parser.parse_args()
            except SystemExit:
                exit(10)
            patch = sys.argv[1]
            if not os.path.exists(patch):
                print("not file XML")
                print(help_message)
                exit(0)
    exit(0)

if __name__ == "__main__":
    main()