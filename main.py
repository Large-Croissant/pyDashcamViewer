import sys
import pathlib
import os
import logging

DIR = pathlib.Path(__file__).parent
EXIFTOOL_PATH = DIR / "exiftool" / "exiftool.exe"

logging.basicConfig(filename=DIR / "log.log", format="%(asctime)s [%(levelname)s]: %(message)s")
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def cli(args: list[str]): ...


def gui(): ...


def main(args: list[str]):
    if len(args) == 1:
        gui()
    else:
        cli(args)


def setup():
    logger.info("Beginning setup check")
    if EXIFTOOL_PATH.exists():
        logger.info("Exiftool found")
        return
    logger.warning("Exiftool not found, will download")
    EXIFTOOL_VERSION = "exiftool-13.27_64"
    os.system(rf"curl https://exiftool.org/{EXIFTOOL_VERSION}.zip -o {DIR / 'exiftool.zip'}")
    logger.info("Exiftool downloaded")
    os.system(rf"tar -xf {DIR / 'exiftool.zip'}")
    logger.info("Extracted zip archive")
    os.rename(DIR / EXIFTOOL_VERSION, DIR / "exiftool")
    os.rename((DIR / "exiftool" / "exiftool(-k).exe"), DIR / "exiftool" / "exiftool.exe")
    logger.info("Files renamed")
    os.remove(DIR / "exiftool.zip")
    logger.info("Cleaned up zip file")


if __name__ == "__main__":
    setup()
    main(sys.argv)
