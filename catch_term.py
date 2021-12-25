#! /usr/bin/env python3

import signal
import sys
from types import FrameType
from typing import Optional


def signal_handler(sig: int, frame: Optional[FrameType]):
    print('You pressed Ctrl+C!')
    sys.exit(0)


def main() -> None:
    signal.signal(signal.SIGTERM, signal_handler)
    print('Press Ctrl+C')
    signal.pause()


if __name__ == "__main__":
    main()
