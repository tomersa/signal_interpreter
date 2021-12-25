# signal_interpreter

An example of how to use the signal interpreter to tell the signal the process is catching(SigCgt) and ignoring(SigIgn)

USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
tomer       9794  0.0  0.0  16620  9440 pts/2    S+   00:14   0:00 python3 ./catch_term.py
tomer       9809  0.0  0.0  16620  9336 pts/0    S+   00:14   0:00 python3 ./ignore_term.py

On pid 9794 (catch_term.py), The output of `$ sig 9794` is:
```bash
Signal [SigPnd] -> ()
Signal [SigBlk] -> ()
Signal [SigIgn] -> ('PIPE', 'XFSZ')
Signal [SigCgt] -> ('INT', 'TERM', '32', '33')
```

* Notice how SigCgt contains the term since it is catching TERM signal. Because of the line:
```python
	signal.signal(signal.SIGTERM, signal_handler)
```

On pid 9809 (ignore_term.py), The output of `$ sig 9809` is:
Signal [SigPnd] -> ()
Signal [SigBlk] -> ()
Signal [SigIgn] -> ('PIPE', 'TERM', 'XFSZ')
Signal [SigCgt] -> ('INT', '32', '33')

* Notice how TERM signal is Ignored. Because of the line:
```python
    signal.signal(signal.SIGTERM, signal.SIG_IGN)
```

