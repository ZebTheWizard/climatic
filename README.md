# Climatic Group Project

This branch is the final project. The code is written for Raspberry Pi running Raspbian. 

<center><img src="https://raw.githubusercontent.com/ghzb/climatic2/master/public/img/main.jpg" alt="main"/></center>

### Assumptions
1. Code is running on Raspberry Pi
1. Raspberry Pi has Raspbian OS
1. Raspberry Pi is using DH11 sensor attached to pin 7
1. Code is running with Python 3.7 and venv/pip
1. Code is not for production

# How to Install/Run
1. Ensure all assumptions are met.
1. Clone the repo to raspberry pi `git clone https://github.com/ghzb/climatic2`
1. Change directories `cd climatic2`
1. Create a virtual environment `python3 -m venv venv`
1. Activate venv `source venv/bin/activate`
1. Install pip packages inside venv `pip install -r requirements.txt`
1. Make script executable `chmod +x main.py` or `chmod 700 main.py`
1. Run everything in the background `./main.py &`
1. Wait for about 20 minutes to let data populate
1. Note the ip of the raspberry pi `hostname -I`
1. Visit raspberry pi webserver in the browser **not loopback** `http://192.168.1.6:5000`
1. Look at charts or use manual entry forms.

### How does it work 
1. The executable is a custom scripts that runs "jobs". Each job spawn seperate threads or execute code in intervals like a traditional CRON job.
1. This code base spawns a job for the Flask web server. And the DH11 sensor daemon.
1. When the DH11 daemon runs it inserts the last temperature/humidity into a SQLITE database. It runs every 30 seconds.
1. When a user visits the web page, temperature data is grouped and averaged by timestamps.

# Features
Here is a quick list of features. 

#### Automatically collects temperature/humidity data every 30 seconds
The server is constantly collecting temperatures. When the server is ready for a new temperature it stores it in the database automatically.

#### Displays data in a fancy chart
See all the collected data by using a fancy chart. If you want to live in the past then you can select more date ranges.
<center><img src="https://raw.githubusercontent.com/ghzb/climatic2/master/public/img/weather.png" alt="main"/></center>
<center><img src="https://raw.githubusercontent.com/ghzb/climatic2/master/public/img/filter.png" alt="main"/></center>

#### Dark/Light Mode.
We hacked together a dark and light mode.

#### Allows manual entries
If you want to add a few dates to try things out this feature is for you.
<center><img src="https://raw.githubusercontent.com/ghzb/climatic2/master/public/img/entry.png" alt="main"/></center>

#### Allows data to be imported from a CSV file.
If you already have a collection of temperatures, then you can import them for fancy charting.
<center><img src="https://raw.githubusercontent.com/ghzb/climatic2/master/public/img/upload.png" alt="main"/></center>

#### Delete data too
Have bad data? Delete them and try again.
<center><img src="https://raw.githubusercontent.com/ghzb/climatic2/master/public/img/entries.png" alt="main"/></center>

#### Runs on port 5000
Port 5000 so you don't need admin privledges. 

#### No NGINX or Apache required
The connections are forwarded straight to the background processes. If you want to use in production environment you should use NGINX or Apache.
