import datetime

from discord import embeds
from food import food

from confirm import holiday_check
from confirm import lastday_check

import discord
from discord.ext import commands

f = open('discordbottoken', 'r')

client = commands.Bot(command_prefix='!')
discordbottoken = f.readline()
f.close()

nothing_img = "https://p16-va-default.akamaized.net/img/musically-maliva-obj/1663611286516741~c5_720x720.jpeg"

@client.event
async def on_ready():
    print(client.user.id)
    print(client.user.name)
    print("ready")
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

        time = today['MLSV_YMD']
        diet = today['DDISH_NM'].replace('<br/>', ', ')
        calorie = today['CAL_INFO']

        embed = discord.Embed(title="오늘급식", description="오늘의 급식은?!?!?!", color=0xf29661)
        embed.add_field(name="식단", value=f"{diet}", inline=False)
        embed.add_field(name="칼로리", value=f"{calorie}", inline=False)
        embed.set_footer(text=f"등록일: {time}")

        await message.send(embed=embed)

    elif holiday_check(dt.day):
        embed = discord.Embed(title="오늘급식", description="..?", color=0xf15f5f).set_image(nothing_img)
        embed.add_field(name="오늘은 급식이 없습니다!", value="❌", inline=False)
        embed.set_footer(text=f"오늘 날짜: {dt.month}월 {dt.day}일")
        
        await message.send(embed=embed)

async def tomorrowlunch(message):
    dt = datetime.datetime.now()

    if lastday_check(dt.day + 1):
        embed = discord.Embed(title="다음달", description="다음달이라고요!?!?!?!", color=0xb7f0b1)
        embed.add_field(name="다음날 테스트를 위한 준비", value="test", inline=False)
        await message.send(embed=embed)

    elif not holiday_check(dt.day + 1):
        today = food(dt.month, dt.day + 1)

        time = today['MLSV_YMD']
        diet = today['DDISH_NM'].replace('<br/>', ', ')
        calorie = today['CAL_INFO']

        embed = discord.Embed(title="내일급식", description="내일 급식은?!?!?!", color=0xb7f0b1)
        embed.add_field(name="식단", value=f"{diet}", inline=False)
        embed.add_field(name="칼로리", value=f"{calorie}", inline=False)
        embed.set_footer(text=f"등록일: {time}")

        await message.send(embed=embed)

    elif holiday_check(dt.day + 1):
        embed = discord.Embed(title="내일급식", description="..?", color=0xf15f5f).set_image(nothing_img)
        embed.add_field(name="내일은 급식이 없습니다!", value="❌", inline=False)
        embed.set_footer(text=f"내일 날짜: {dt.month}월 {dt.day}일")
        
        await message.send(embed=embed)


client.run(discordbottoken)
