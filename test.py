from whatnots.whatnot import Whatnot
from datetime import datetime
import os
import json
import aiohttp
import time
import nextcord
from  nextcord.ext  import commands
import asyncio
bot  =  commands.Bot()
intents  =  nextcord.Intents.default()
intents.members  =  True
intents.message_content  =  True
bot  =  commands.Bot(command_prefix=".",  intents=intents)
bot.remove_command('help')

async def checkforlive(self, ctx):
    await self

@bot.event
async def on_ready():
    print("working")

async def getwhatnotacc():
    async with Whatnot() as whatnot:
            await whatnot.login("dineshtalwadker@gmail.com", "Omshanti@2005")
            whatnot_user = await whatnot.get_user_by_id("1246084")
            return whatnot_user


async def getwhatnotlive():
    async with Whatnot() as whatnot:
        await whatnot.login("dineshtalwadker@gmail.com", "Omshanti@2005")
        whatnot_user = await whatnot.get_user_by_id("1246084")
        lives = await whatnot.get_user_lives(whatnot_user.id)
        return lives

@bot.command()
async def whatnot(ctx):
    whatnot_user = await getwhatnotacc()
    whatnot_live = await getwhatnotlive()
    print(whatnot_live)
    for live in whatnot_live:
            print(live.title)
            embedvar1 = nextcord.Embed(title="")
            
    embedvar = nextcord.Embed(title="[" + str(whatnot_user.username) + "](https://whatnot.com/user/" + whatnot_user.username + ") | whatnot \u200B", timestamp=datetime.utcnow(), description="**about me:**\n" + str(whatnot_user.bio) + "\n", color=0x5865F2)
    embedvar.set_image(whatnot_user.profile_url)
    embedvar.set_footer(text='\u200b',icon_url="https://i.imgur.com/uZIlRnK.png")
    embedvar.add_field(name='Seller Ratings', value=str(whatnot_user.seller_rating["numReviews"])+ ", Overall Rating: " + str(whatnot_user.seller_rating["overall"]))
    embedvar.add_field(name='Followers', value=whatnot_user.follower_count)
    embedvar.add_field(name='Following Count', value=whatnot_user.following_count, inline=True)
    
    await ctx.reply(embed=embedvar)    

@bot.command()
async def game(ctx, *, game):
    start_time = time.time()
    sess = aiohttp.ClientSession()
    querystring = {"title":str(game),"region":"us","offset":"0","limit":"10"}
    headers = { 
        "X-RapidAPI-Key": "d9530def8dmsh6dcb6776fae04afp146fe2jsn3cf4b9769aba   ",
        "X-RapidAPI-Host": "game-prices.p.rapidapi.com"
    }
    async with sess.get('https://game-prices.p.rapidapi.com/games',params=querystring, headers=headers) as resp:
        b = await resp.json()
        await sess.close()
        aa = json.dumps(b)
        a = json.loads(aa)
        price=""
        currency=""
        price=("**FREE**", str(a["games"][0]["currentLowestPrice"]))[price=="0"]
        currency=("", str(a["games"][0]["currency"]))[price=="0"]
        embedvar = nextcord.Embed(title=a["games"][0]["name"], timestamp=datetime.utcnow(), description="now available for " + price + " " + currency, color=0x5865F2)
        embedvar.set_footer(text='\u200b',icon_url="https://i.imgur.com/uZIlRnK.png")
        embedvar.add_field(name='Release Date', value=a["games"][0]["releaseDate"], inline=True)
        embedvar.add_field(name='Stores', value="available at [" + str(a["games"][0]["stores"][0]['seller']) + "](" + a["games"][0]["stores"][0]['url']+")", inline=True)
        print("--- %s seconds ---" % (time.time() - start_time))
        await ctx.reply(embed=embedvar)
        await sess.close()
 
bot.run(os.environ.get("TOKEN", 'MTAzODA4MjAxNTQ5MDIxNTk2Nw.Gz4jqx.rbgA1zbYN-MLl6c4udZZdQurIbATXSpxNPw_lY'))