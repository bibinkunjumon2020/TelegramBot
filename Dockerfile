FROM python:3.9-alpine

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
#RUN pip install --no-cache-dir --no-binary :all: -r requirements.txt

CMD [ "python", "-m", "telegram_bot.main" ]
