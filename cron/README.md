This crontab script adds my WANIP to the .env file.
This allows getting this ip address despite being behind a VPN.

To edit crontabs
```sh
crontab -u $USER -e
```

Example entry:
```crontab
# m h  dom mon dow   command
* * * * * sh /home/ely/home-assistant/cron/set-wan-ip.sh
```