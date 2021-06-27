## ==== 공통부분 =====
>  discordbottoken 파일을 생성해 파일안에 봇토큰 넣기

## ==== 도커를 이용하는 경우 ====
1. > docker build -t foodbot .
2. > docker run -d -it --rm foodbot

## ==== 로컬에서 실행할 경우 ====
1. 자신에게 맞는 버전의 크롬 드라이버 설치
2. > pip install --no-cache-dir -r requirements.txt
3. > python3 discordBOT.py

## ==== vscode devcontainer 사용 ====
1. reopen container
2. > apt-get -y update
3. > wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
4. > apt install -y ./google-chrome-stable_current_amd64.deb
5. > wget http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
6. > unzip ./chromedriver_linux64.zip chromedriver
7. > pip install --no-cache-dir -r requirements.txt
8. > python3 discordBOT.py


## file tree
![file tree image](https://github.com/minpeter/foodBOT/blob/main/filetree.png?raw=true)