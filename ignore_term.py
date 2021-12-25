#! /usr/bin/env python3

import signal
import sys
from types import FrameType
from typing import Optional


def main() -> None:
    signal.signal(signal.SIGTERM, signal.SIG_IGN)
    signal.pause()


if __name__ == "__main__":
    main()
