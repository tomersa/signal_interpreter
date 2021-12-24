#! /usr/bin/env python3

import sys
import subprocess
from subprocess import run
from pprint import pprint
from typing import Tuple, Dict

def print_usage() -> None:
    print(
    f"""
    Usage: {sys.argv[0]} <pid>
    """)

def interpet_signal(hexdecimal_string: str) -> Tuple[str, ...]:
    output = []
    for place, bit in enumerate(reversed(list(bin(int(hexdecimal_string, 16)))[2:]), 1):
        if bit == "1":
            cmd = f'kill -l {place}'
            completed_process = run(cmd, text=True, stdout=subprocess.PIPE, shell=True)
            if completed_process.returncode == 0:
                output.append(completed_process.stdout[:-1])
            else:
                print(completed_process.returncode)
    return tuple(output)

def main() -> None:
    if len(sys.argv) != 2:
        print_usage()
        sys.exit(1)
    pid: int = sys.argv[1]
    signals: Dict[str, Tuple[str, ...]] = {}
    with open(f'/proc/{pid}/status') as f:
        for line in f.readlines():
            if 'Sig' in line and not 'SigQ' in line:
                key, hexdecimal_string = line[:-1].split(':\t')
                signals[key] = interpet_signal(hexdecimal_string)
    for key, value in signals.items():
        print(f'Signal [{key}] -> {value}')

if __name__ == "__main__":
    main()
