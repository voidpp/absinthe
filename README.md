About
-
What is it for?
You are working with ssh and you are opening some remote files in the local editor via sshfs. But you need to search in the files. You cannot search in the files in the local mount of sshfs, because it will be slow as fuck. So you are search in ssh (with grep or etc). You found the file what is searching for, so what do you do? Switch to the local editor, opens the file open dialog, and browse across lots of directiories to find this particular file. This is slow, and uncomfortable. If the absinthe (server and client) is configured well, just type `abs path/to/file` and the file will opening in the local editor immediately.

Install
-
`pip install absinthe`

Config example
-
Server (in camel.ca, it's just a piece):
```json
{
	"agent_server": {
		"host": "0.0.0.0",
		"port": 52180
	},
	"paths": {
		"douglas": "/home/douglas/"
	},
	"default-path": "douglas"
}
```
Client:
```json
{
    "editors": {
        "npp": "c:\\Program Files (x86)\\Notepad++\\notepad++.exe"
    },
    "hosts": {
		"camel": {
			"host": "camel.ca",
			"port": 52180
		}
    },
    "sessions": [{
		"enabled": true,
		"host": "camel",
		"name": "camel-douglas",
		"remote-path": "douglas",
		"path": "k:\\",
		"editor": "npp"
    }]
}
```

Usage
-
`absinthe start`
`abs path/to/file1 path/to/file2`
