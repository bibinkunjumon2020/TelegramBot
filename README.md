
# TelegramBot:botbibi


The 'botbibi' ,Telegram Bot app is a Python-based application that allows users to access various functionalities through a Telegram bot. The bot provides four main functionalities, including weather checking, poll creation and posting in group, access to random images from the internet, and currency exchange.

The weather checking function enables users to check the current weather of a specific location. Users can enter the name of the city, and the bot will provide the current temperature and weather conditions.

The poll creation and posting in group feature allows users to create a poll and post it in a Telegram group. Users can enter the poll question and options, and the bot will create the poll and post it in the specified group.

The access to random images from the internet function allows users to access random images of animals from the internet. 

The currency exchange feature allows users to exchange a fixed amount of currency from one type to another. Users can enter the amount, the currency type they wish to exchange from and to, and the bot will return the upto date exchanged amount.

The Telegram Bot app is built using Python and relies on the aiogram library for Telegram bot integration. The application also utilizes other Python libraries, including requests, json, aiohttp, and logging, to provide its functionalities. The app is modular and follows good coding practices, allowing for easy maintenance and updates.

By adding the image in Docker, anyone can easily pull it and supply APIs to use it in their projects. This makes it easier for developers to integrate the bot into their own applications without having to worry about the underlying infrastructure.

Moreover, the live bot is hosted on a server, which ensures that the bot is available for testing 24/7. This means that users can access the bot at any time and get the information they need without any downtime. This makes the bot a reliable tool for users who rely on it for their day-to-day needs.








## Commands to Run 'botbibi'
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
<img width="824" alt="image" src="https://user-images.githubusercontent.com/104210649/233340133-80e09acd-c4a8-4627-9cc0-33f6866977ed.png">



## Search Bot in Telegram

Username : @bibinkunjumon_bot

You will get a welcome page below:

 <img width="373" alt="image" src="https://user-images.githubusercontent.com/104210649/233340225-801516d1-f7f6-4639-b6b0-10ee953aa748.png">



## Working Screenshots

<img width="374" alt="image" src="https://user-images.githubusercontent.com/104210649/233340358-7303181e-a423-4062-8f42-bea07095b8a6.png">
<img width="356" alt="image" src="https://user-images.githubusercontent.com/104210649/233340479-ce969fa1-2d16-41be-83af-8b807a3ba989.png">
<img width="360" alt="image" src="https://user-images.githubusercontent.com/104210649/233340616-65a1b67b-85c1-4123-a9fa-cfda11f509d0.png">
<img width="363" alt="image" src="https://user-images.githubusercontent.com/104210649/233340696-b6d52d94-904e-4e83-bb15-6b9b26d440ac.png">
<img width="372" alt="image" src="https://user-images.githubusercontent.com/104210649/233340993-7d0e4bf6-2c19-43a2-afe5-ea7cd7fe54b7.png">
<img width="368" alt="image" src="https://user-images.githubusercontent.com/104210649/233341033-4227f562-2319-4376-88f8-0d52c85ebd44.png">
<img width="356" alt="image" src="https://user-images.githubusercontent.com/104210649/233341095-89dfdc1c-c720-4874-9710-c20cc364cea0.png">
<img width="367" alt="image" src="https://user-images.githubusercontent.com/104210649/233341170-fcd54355-9dff-4814-9ea8-010616c43127.png">

## 🚀 About Me
I am a skilled software developer with over three years of experience in delivering secure and reliable applications. My expertise lies in back-end user development and AI-related work.I have a strong background in Python programming and am dedicated to continuously improving my skills and knowledge in the field.
