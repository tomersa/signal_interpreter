#! /usr/bin/env python3

import sys
import subprocess
from subprocess import run
from typing import Tuple, Dict, Iterable


def print_usage() -> None:
    print(
        f"""
    Usage: {sys.argv[0]} <pid>
    """)


def prepare_bits(hexdecimal_string: str) -> Iterable[Tuple[int, str]]:
    decimal_string = int(hexdecimal_string, 16)  # Convert hexdecimal to decimal
    binary_string = list(bin(decimal_string))  # Convert to binary list
    binary_string = binary_string[len('0b'):]  # Removing 0b prefix
    return enumerate(reversed(binary_string), 1)


def interpret_signal(hexdecimal_string: str) -> Tuple[str, ...]:
    output = []
    for place, bit in prepare_bits(hexdecimal_string):
        if bit != "1":
            continue
        cmd = f'kill -l {place}'
        completed_process = run(cmd, text=True, stdout=subprocess.PIPE, shell=True)
        if completed_process.returncode == 0:
            output.append(completed_process.stdout.strip('\n'))
        else:
            print('error', f'{completed_process}')
    return tuple(output)


def main() -> None:
    if len(sys.argv) != 2:
        print_usage()
        sys.exit(1)
    pid: int = int(sys.argv[1])
    signals: Dict[str, Tuple[str, ...]] = {}
    with open(f'/proc/{pid}/status') as f:
        for line in f.readlines():
            if 'Sig' in line and 'SigQ' not in line:
                key, hexdecimal_string = line[:-1].split(':\t')
                signals[key] = interpret_signal(hexdecimal_string)
    for key, value in signals.items():
        print(f'Signal [{key}] -> {value}')


if __name__ == "__main__":
    main()
