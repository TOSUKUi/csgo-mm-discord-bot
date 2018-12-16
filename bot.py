import discord
import yaml
import pandas

secret = yaml.load(open("secret.yaml").read())
token = secret["token"]
client = discord.Client()

@client.event
async def on_ready():
    print("ログインしました")


@client.event
async def on_message(message):
    if message.content.startswith("/csgo"):
        if client.user != message.author:
            print(message.content) 
            print(message.content.split("\n"))
            #dispatch(message.context, status)
            await client.send_message(message.channel, "同志")
    if "資本主義" in message.content:
        if client.user != message.author:
            await client.send_message(message.channel, "殺すぞ")

# def dispatch(message, status):
#    meessage


client.run(token)