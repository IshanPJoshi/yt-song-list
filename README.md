# yt-song-list
A redux of some [older exploration I did](https://github.com/IshanPJoshi/Youtube-API-Exploration) of the Youtube API to get a list of all my songs. The execution is a little crude and lacked automation. I plan for this repo to revise the work I've done and build using some new knowledge I have of web development.

## Basic flask setup

### Environment variables (WINDOWS)
```powershell
$env:FLASK_ENV = "development"
$env:FLASK_APP = "server.py"
```

### Use pipenv
```bash
pipenv install
pipenv shell
flask run
```
