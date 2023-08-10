from interactions import Client, Intents, listen, slash_command, SlashContext

import os

from dotenv import load_dotenv

import logging

load_dotenv()


dir_name = os.path.dirname(__file__))

logging.basicConfig(filename=dir_name + '/log.log', level=logging.INFO)
logging.info('loggggyloggg')

bot = Client(Intents=Intents.DEFAULT, debug_scope=os.getenv('TEST_SERVER_ID'))


@slash_command(name="make_error", description='makes an error')
async def make_an_error(ctx: SlashContext):
    try:
        s = 1 / 0
    except ZeroDivisionError as e:
        logging.info(f'logggg: {e}')
        await ctx.send('something went wrong')


@listen()
async def on_ready():
    print('Ready')
    print(f'This bot is owned by {bot.owner}')


bot.start(os.getenv('DISCORD_TOKEN'))
