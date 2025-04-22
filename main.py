import sys
import pathlib
import os

DIR = pathlib.Path(__file__).parent


def cli(args: list[str]): ...


def gui(): ...


def main(args: list[str]):
    if len(args) == 1:
        gui()
    else:
        cli(args)


def setup(): ...


if __name__ == "__main__":
    setup()
    main(sys.argv)
