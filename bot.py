import discord
import yaml
import pandas as pd

secret = yaml.load(open("secret.yaml").read())
token = secret["token"]
client = discord.Client()
prev_state = pd.DataFrame({}, columns=["map", "author", "mix", "opponent_mix", "server"])
@client.event
async def on_ready():
    print("ログインしました")


@client.event
async def on_message(message):
    global prev_state
    if message.content.startswith("/csgo"):
        if client.user != message.author:
            prev_state, view = dispatch(message, prev_state)
            await client.send_message(message.channel, embed=view)
    if "資本主義" in message.content:
        if client.user != message.author:
            await client.send_message(message.channel, "殺すぞ")

def dispatch(message, state):
    permit_action = ["add", "delete", "list" , "help", "reset"]
    message_list = message.content.split("\n")
    action = message_list[0].split(" ")[1]

    if action == "add":
        return add(merge_dict(yaml.load("\n".join(message_list[1:])), {"author": message.author.name}), state)
    elif action == "delete":
        return delete(merge_dict(yaml.load("\n".join(message_list[1:])), {"author": message.author.name}), state)
    elif action == "list":
        return show(state)
    elif action == "help":
        return __help(state)
    elif action == "reset":
        return reset(state)
    else:
        return __help(state)

def merge_dict(x, y):
    return {**x, **y}

def add(body, state):
    next_state = state.append(body, ignore_index=True) if body["author"] not in state["author"].values else state
    view = discord.Embed(title="CSGO MM BOT add")
    for index, val in next_state.iterrows():
        view.add_field(name=val["author"].name, value=list(val))
    return next_state, view

def delete(body, state):
    next_state = state[state["author"] != body] 
    view = discord.Embed(title="CSGO MM BOT add")
    for index, val in next_state.iterrows():
        view.add_field(name=val["author"].name, value=list(val))
    return next_state, view
    
def show(state):
    next_state = state
    view = discord.Embed(title="CSGO MM BOT add")
    for index, val in next_state.iterrows():
        view.add_field(name=val["author"].name, value=list(val))
    return next_state, discord.Embed(title="list")
    
def __help(state):
    return state, discord.Embed(title="help")

def reset(state):
    return state, discord.Embed(title="reset")

client.run(token)