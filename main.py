import math
import discord
import mail
import os

client = discord.Client()
env = os.environ

DISCORD_TOKEN = env.get("DISCORD_TOKEN")
CHANS = env.get("DISCORD_CHANS")
if CHANS:
	CHANS = list(map(lambda x: int(x), CHANS.split(",")))
else:
	CHANS = []

@client.event
async def on_ready():
    print("Logged in")

@client.event
async def on_message(message):
	if message.channel.id not in CHANS:
		return

	text = message.content
	if len(text) > 0:
		remote_attachments = list(map(lambda x: x.url, message.attachments))
		
		print(text)
		print(remote_attachments)
		
		mail.send_email(text, remote_attachments)

client.run(DISCORD_TOKEN)