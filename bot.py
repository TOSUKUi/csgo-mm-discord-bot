import discord


token = "NTIzNjg1MjE1MzM2NTI5OTQy.DveNwA.bJNeBrI9PgTIaMbOxvBfFssqLLQ"
client = discord.Client()

@client.event
async def on_ready():
    print("ログインしました")


@client.event
async def on_message(message):
    if message.content.startswith("/csgo"):
        if client.user != message.author:
            await
            await client.send_message(message.channel, "同志")
    if "資本主義" in message.content:
        if client.user != message.author:
            await client.send_message(message.channel, "殺すぞ")

ddfvcef dispatch():

client.run(token)