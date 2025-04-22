import sys
import pathlib
import os
import logging

DIR = pathlib.Path(__file__).parent
EXIFTOOL_PATH = DIR / "exiftool" / "exiftool.exe"


def cli(args: list[str]): ...


def gui(): ...


def main(args: list[str]):
    if len(args) == 1:
        gui()
    else:
        cli(args)


def setup():
    if EXIFTOOL_PATH.exists():
        return

    EXIFTOOL_VERSION_FILE = "exiftool-13.27_64.zip"
    os.system(rf"curl https://exiftool.org/{EXIFTOOL_VERSION_FILE} -o {DIR / 'exiftool.zip'}")
    os.system(rf"tar -xf {DIR / 'exiftool.zip'}")
    os.rename(DIR / EXIFTOOL_VERSION_FILE, DIR / "exiftool")
    os.rename(DIR / "exiftool" / "exiftool(-k).exe", DIR / "exiftool" / "exiftool.exe")


if __name__ == "__main__":
    setup()
    main(sys.argv)
