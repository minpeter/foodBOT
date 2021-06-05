FROM python:3.9
WORKDIR /usr/src/app

RUN apt-get -y update
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt install -y ./google-chrome-stable_current_amd64.deb
RUN google-chrome --version
RUN apt-get install -yqq unzip curl

RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/src/app


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

copy . .
RUN chmod +x discordBOT.py


CMD [ "python", "discordBOT.py" ]
