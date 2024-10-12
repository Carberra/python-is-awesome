import logging
import time
from enum import Flag

logging.basicConfig(level=logging.INFO)


class RunFlags(Flag):
    NONE = 1 << 0
    VERBOSE = 1 << 1
    BUILD = 1 << 2
    DRY_RUN = 1 << 3
    DEBUG = VERBOSE | DRY_RUN


def run(*, flags: RunFlags = RunFlags.NONE) -> None:
    log = logging.getLogger("run")

    if flags & RunFlags.VERBOSE:
        log.setLevel(logging.DEBUG)

    if flags & RunFlags.BUILD:
        log.info("Building...")
        log.debug("This may take a while!")
        time.sleep(2)

    log.info("Running...")
    if flags & RunFlags.DRY_RUN:
        log.debug("Running as a dry-run, nothing will change")
    else:
        log.debug("Not running as a dry-run")

    time.sleep(1)
    log.info("Complete!")


if __name__ == "__main__":
    run(flags=RunFlags.DEBUG)
