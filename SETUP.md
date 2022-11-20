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

## .emv
Docker Compose expects will interpolate the variables in `compose.yml` shaped like `${VARIABLE}` with those stored in the environment (or the such).  My prefered way to store these is in a `.env` file placed in the root dir.  Example:
```.env
SUDO_PASSWORD=foobar
APPDAEMON_TOKEN=foobar
SWAG_EMAIL=foobar
SWAG_URL=foobar
DUCKDNS_SUBDOMAINS=foobar
DUCKDNS_TOKEN=foobar
VSCODE_PASSWORD=foobar
VSCODE_PROXY_DOMAIN=foobar
```
Then when the command
```sh
docker compose up
```
will interpolate and fire up the collection of services in the `compose.yml` file.