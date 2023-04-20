
# TelegramBot:botbibi


The 'botbibi' ,Telegram Bot app is a Python-based application that allows users to access various functionalities through a Telegram bot. The bot provides four main functionalities, including weather checking, poll creation and posting in group, access to random images from the internet, and currency exchange.

The weather checking function enables users to check the current weather of a specific location. Users can enter the name of the city, and the bot will provide the current temperature and weather conditions.

The poll creation and posting in group feature allows users to create a poll and post it in a Telegram group. Users can enter the poll question and options, and the bot will create the poll and post it in the specified group.

The access to random images from the internet function allows users to access random images of animals from the internet. 

The currency exchange feature allows users to exchange a fixed amount of currency from one type to another. Users can enter the amount, the currency type they wish to exchange from and to, and the bot will return the upto date exchanged amount.

The Telegram Bot app is built using Python and relies on the aiogram library for Telegram bot integration. The application also utilizes other Python libraries, including requests, json, aiohttp, and logging, to provide its functionalities. The app is modular and follows good coding practices, allowing for easy maintenance and updates.

By adding the image in Docker, anyone can easily pull it and supply APIs to use it in their projects. This makes it easier for developers to integrate the bot into their own applications without having to worry about the underlying infrastructure.

Moreover, the live bot is hosted on a server, which ensures that the bot is available for testing 24/7. This means that users can access the bot at any time and get the information they need without any downtime. This makes the bot a reliable tool for users who rely on it for their day-to-day needs.








## Commands to Run 'Whisper'
Clone the repository from GitHub using the command:
```
git clone https://github.com/bibinkunjumon2020/TelegramBot.git
```

Create & Activate a virtual environment & install libraries using the command :
```
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```


## Use Docker Image

Pull the Docker image from Docker Hub(Supply env file)
```
docker run -d --env-file=.env bibinkunjumon2020/botbibi
```

env file has 3 APIs:
```
API_BOT=###
API_WEATHER=###
API_EXCHANGE=###
```

The docker image look like :



## Search Bot in Telegram

Username : @bibinkunjumon_bot

You will get a welcome page below:

    $$ add image of chatbot


## Working Screenshots
## 🚀 About Me
I am a skilled software developer with over three years of experience in delivering secure and reliable applications. My expertise lies in back-end user development and AI-related work.I have a strong background in Python programming and am dedicated to continuously improving my skills and knowledge in the field.