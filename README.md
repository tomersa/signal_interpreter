# Signal Interpreter

An example of how to use the signal interpreter to tell which signals the process is catching(SigCgt) and ignoring(SigIgn)
```bash
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
tomer       9794  0.0  0.0  16620  9440 pts/2    S+   00:14   0:00 python3 ./catch_term.py
tomer       9809  0.0  0.0  16620  9336 pts/0    S+   00:14   0:00 python3 ./ignore_term.py
```

On pid 9794 (catch_term.py), The output of `$ sig 9794` is:
```bash
Signal [SigPnd] -> ()
Signal [SigBlk] -> ()
Signal [SigIgn] -> ('PIPE', 'XFSZ')
Signal [SigCgt] -> ('INT', 'TERM', '32', '33')
```

* Notice how SigCgt contains the 'TERM' since it's catching the 'TERM' signal:
[signal.signal(signal.SIGTERM, signal_handler)](https://github.com/tomersa/signal_interpreter/blob/main/catch_term.py#L15)

On pid 9809 (ignore_term.py), The output of `$ sig 9809` is:
```bash
Signal [SigPnd] -> ()
Signal [SigBlk] -> ()
Signal [SigIgn] -> ('PIPE', 'TERM', 'XFSZ')
Signal [SigCgt] -> ('INT', '32', '33')
```

* Notice how the 'TERM' signal is Ignored here:
[signal.signal(signal.SIGTERM, signal.SIG_IGN)](https://github.com/tomersa/signal_interpreter/blob/main/ignore_term.py#L10)

