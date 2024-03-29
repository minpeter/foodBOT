import datetime

from discord import embeds
from food import food

from confirm import holiday_check
from confirm import lastday_check

import discord
from discord.ext import commands

f = open('discordbottoken', 'r')

client = commands.Bot(command_prefix='!')
token = f.readline()
f.close()

nothing_img = 'https://images.rapgenius.com/d10e27e11d9ac778a5aa0f03d4012b99.500x500x1.png'

@client.event
async def on_ready():
    print(f"BOT ID : {client.user.id}")
    print(f"BOT name : {client.user.name}")
    print("========== ready ==========")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("!오늘급식 or !내일급식"))


@client.command(name='오늘급식')
async def callmsgl(message):
    await todaylunch(message)


@client.command(name='ㅇㄴㄱㅅ')
async def callmsgs(message):
    await todaylunch(message)


@client.command(name='내일급식')
async def callmsgtl(message):
    await tomorrowlunch(message)


@client.command(name='ㄴㅇㄱㅅ')
async def callmsgts(message):
    await tomorrowlunch(message)


async def todaylunch(message):
    dt = datetime.datetime.now()

    if not holiday_check(dt.day):
        today = food(dt.month, dt.day)

        embed = discord.Embed(title="오늘급식", description="오늘의 급식은?!?!?!", color=0xf29661)
        embed.add_field(name="식단", value=f"{today['diet']}", inline=False)
        embed.add_field(name="칼로리", value=f"{today['calorie']}", inline=False)
        embed.set_image(url=today['img'])
        embed.set_footer(text=f"등록일: {today['time']}")

        await message.send(embed=embed)

    elif holiday_check(dt.day):
        embed = discord.Embed(title="오늘급식", description="오늘은 급식이 없습니다!", color=0xf15f5f)
        embed.set_image(url=nothing_img)
        embed.set_footer(text=f"오늘 날짜: {dt.month}월 {dt.day}일")
        
        await message.send(embed=embed)


async def tomorrowlunch(message):
    dt = datetime.datetime.now()

    if lastday_check(dt.day + 1):
        embed = discord.Embed(title="다음달", description="아마도 오늘이 월말일꺼예요..", color=0xb7f0b1)
        embed.add_field(name="이 문구를 보는 경우 다음날 급식이가 작동하지 않을수 있어요...", value="정상이니 걱정말아요!", inline=False)
        await message.send(embed=embed)

    elif not holiday_check(dt.day + 1):
        today = food(dt.month, dt.day + 1)

        embed = discord.Embed(title="내일급식", description="내일 급식은?!?!?!", color=0xb7f0b1)
        embed.add_field(name="식단", value=f"{today['diet']}", inline=False)
        embed.add_field(name="칼로리", value=f"{today['calorie']}", inline=False)
        embed.set_image(url=today['img'])
        embed.set_footer(text=f"등록일: {today['time']}")

        await message.send(embed=embed)

    elif holiday_check(dt.day + 1):
        embed = discord.Embed(title="내일급식", description="내일은 급식이 없습니다!", color=0xf15f5f)
        embed.set_image(url=nothing_img)
        embed.set_footer(text=f"내일 날짜: {dt.month}월 {dt.day}일")
        
        await message.send(embed=embed)
    

client.run(token)
