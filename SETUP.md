# Setup Instructions from Scratch

## Enabling SSH
```sh
sudo apt install openssh-server
```
Then to ssh
```sh
ssh ely@192.168.1.206
```

Install `screen`
```sh
sudo apt install screen
```

[screen usage](https://linuxize.com/post/how-to-use-linux-screen/)
`exit` closes a given session/window

## Directories
Make these if not present
```sh
mkdir vscode_config
mkdir appdaemon_config
mkdir homeassistant_config
mkdir swag_config
mkdir vscode_config
```

## Fix Permissions
When HA fist starts up it create a bunch of files. chown them to have edit permissions remotly in vs-code. # TODO - investigate running as user.
```sh
sudo chown -R $USER homeassistant_config
```