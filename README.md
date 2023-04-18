# bard-discord
Google Bard discord bot code, join my discord server: https://discord.gg/qX5dwV3HEp
My discord bot: https://discord.com/api/oauth2/authorize?client_id=1097804626872508496&permissions=362496&scope=bot


## Installation
```
git clone https://github.com/yoou3-cyber/bard-discord
cd bard-discord
pip install -r requirements.txt
```

## Authentication
Go to https://bard.google.com/

- F12 for console
- Copy the values
  - Session: Go to Application → Cookies → `__Secure-1PSID`. Copy the value of that cookie.

Go to https://discord.com/developers/applications/

- New Application
- Bot
- Create Bot
- Copy token

Open `.env` file in bard-discord directory and put tokens there

```
DISCORD_TOKEN=<your token>
BARD_TOKEN=<your token>
```


## Running
After adding needed tokens in .env start your bot by command:
```
python bard.py
```
