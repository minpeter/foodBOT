import time
import datetime
import discord
from food import food

f = open('discordbottoken', 'r')

client = discord.Client()
token = f.readline()
f.close()

@client.event
async def on_ready():
    print(client.user.id)
    print(client.user.name)
    print("ready")
    await client.change_presence(status=discord.Status.online, activity = discord.Game("!오늘급식 or !ㅇㄴㄱㅅ"))


@client.event
async def on_message(message):
    if message.content.startswith("!오늘급식") or message.content.startswith("!ㅇㄴㄱㅅ"):
        today = food(datetime.datetime.now().month, datetime.datetime.now().day)

        time = today[1].strip()
        diet = today[3].strip()
        calorie = today[4].strip()

        img = "이미지가 존재하지 않음"

        if len(today) == 6:
            img = "http://hansei.sen.hs.kr"+today[5].strip()
        
        await message.channel.send(f"```등록일: {time}\n식단: {diet}\n칼로리: {calorie}```\n{img}")


    if message.content.startswith("!내일급식") or message.content.startswith("!ㄴㅇㄱㅅ"):
            today = food(datetime.datetime.now().month, datetime.datetime.now().day + 1)

            time = today[1].strip()
            diet = today[3].strip()
            calorie = today[4].strip()

            img = "이미지가 존재하지 않음"

            if len(today) == 6:
                img = "http://hansei.sen.hs.kr"+today[5].strip()
            
            await message.channel.send(f"```등록일: {time}\n식단: {diet}\n칼로리: {calorie}```\n{img}")

client.run(token)
