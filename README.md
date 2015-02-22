# absinthe
a tiny server-client app to open sshfs connected files from ssh console in any local editor

requirements:
- generic

- server
	- pyjsonrpc
	- gevent-websocket
- client
	- websocket-client

windows notes:
- the server is not tested on windows
- do not use cygwin
- python install https://www.python.org/downloads/windows/
- compiler for python pip 2.7 http://www.microsoft.com/en-us/download/confirmation.aspx?id=44266
- pywin32: http://sourceforge.net/projects/pywin32/files/pywin32/
