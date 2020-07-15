# Screening Test

Python 3.6.x - 3.7.6

## Setup project

Start TCP Server
```
$ python3 run_tcp_server.py
```

Start Mail Server
```
$ python3 -m smtpd -c DebuggingServer -n localhost:1025
```

## Run examples

Run script
```
$ python3 run_script.py < test/test1.json
```

Run tests
```
$ python3 run_tests.py
```
