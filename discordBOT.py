import time
import datetime
import discord
from food import food

f = open('discordbottoken', 'r')

client = discord.Client()
token = f.readline()
f.close()

nothing_img = 'https://p16-va-default.akamaized.net/img/musically-maliva-obj/1663611286516741~c5_720x720.jpeg'


def holiday_check (day):
    dt = datetime.datetime.now()
    return datetime.date(dt.year, dt.month, day).weekday() == 5 or datetime.date(dt.year, dt.month, day).weekday() == 6

@client.event
async def on_ready():
    print(client.user.id)
    print(client.user.name)
    print("ready")
    await client.change_presence(status = discord.Status.online, activity = discord.Game("!오늘급식 or !내일급식"))


@client.event
async def on_message(message):
    if message.content.startswith("!오늘급식") or message.content.startswith("!ㅇㄴㄱㅅ"):
        dt = datetime.datetime.now()
        
        if holiday_check(dt.day) == False:
            today = food(dt.month, dt.day)

            time = today[1].strip()
            diet = today[3].strip()
            calorie = today[4].strip()

            img = "이미지가 존재하지 않음"

            if len(today) == 6:
                img = "http://hansei.sen.hs.kr"+today[5].strip()
            
            await message.channel.send(f"```등록일: {time}\n식단: {diet}\n칼로리: {calorie}```\n{img}")
        
        elif holiday_check(dt.day) == True:
            await message.channel.send(f"```{dt.month}월 {dt.day}일은 급식이 없습니다!```\n{nothing_img}")

    if message.content.startswith("!내일급식") or message.content.startswith("!ㄴㅇㄱㅅ"):
            dt = datetime.datetime.now()
            if holiday_check(dt.day + 1) == False:
                today = food(dt.month, dt.day + 1)

                time = today[1].strip()
                diet = today[3].strip()
                calorie = today[4].strip()

                img = "이미지가 존재하지 않음"

                if len(today) == 6:
                    img = "http://hansei.sen.hs.kr"+today[5].strip()
                
                await message.channel.send(f"```등록일: {time}\n식단: {diet}\n칼로리: {calorie}```\n{img}")

                  
            elif holiday_check(dt.day + 1) == True:
                await message.channel.send(f"```{dt.month}월 {dt.day}일은 급식이 없습니다!```\n{nothing_img}")

client.run(token)
