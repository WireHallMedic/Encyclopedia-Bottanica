import discord
import os
from data_loader import input_text_parser
from data_loader import input_image_parser

image_path = "./images"
text_path = "./text"

token = open("token.txt", "r").read()

# change cwd in case this is called from shell script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# create data objects, reading in data
text_data = input_text_parser(text_path)
file_data = input_image_parser(image_path)

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')
    
@client.event
async def on_message(message):
   """
   Main work method, called whenever someone posts a message
   """
   # don't respond to self, empty messages, or messages that don't start with a bang
   if message.author == client.user or \
      len(message.content) == 0 or \
      message.content[0] != '!':
      return
   out_str = None
   out_file = None
   # clean message
   cmd = message.content[1:].strip().lower()
   
   # user requests table of contents
   if cmd == "contents" or cmd == "toc":
      out_str = f"I have information on the following categories:\n{text_data.get_contents()}\n" + \
         f"and can share the following files:\n{file_data.get_contents()}"
   else:
      # get usual output
      out_str = text_data.get(cmd)
      out_file = file_data.get(cmd)
   
   # print results
   if out_file != None:
      await message.channel.send(file=out_file)
   if out_str != None:
      await message.channel.send(out_str)

# fire this bad boy up
client.run(token)