#-----Imports-----
import nextcord
from nextcord.ext import commands
from nextcord import Interaction
from nextcord.ext import application_checks
import json
import aiohttp
import time
import datetime

#-----Commands----- 
class slashcommands(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@nextcord.slash_command(name="game", description="get information about a game ex: (/game game-name)")
	async def game(self, ctx: Interaction, *, game):
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
			embedvar = nextcord.Embed(title=a["games"][0]["name"], timestamp=datetime.datetime.utcnow(), description="now available for " + price + " " + currency, color=0x5865F2)
			embedvar.set_footer(text='\u200b',icon_url="https://i.imgur.com/uZIlRnK.png")
			embedvar.add_field(name='Release Date', value=a["games"][0]["releaseDate"], inline=True)
			embedvar.add_field(name='Stores', value="available at [" + str(a["games"][0]["stores"][0]['seller']) + "](" + a["games"][0]["stores"][0]['url']+")", inline=True)
			print("--- %s seconds ---" % (time.time() - start_time))
			await ctx.reply(embed=embedvar)

	@nextcord.slash_command(name = 'purge', description = '❌ purge messages (Example: /purge 10)')
	@application_checks.has_permissions(administrator=True)
	async def purge(self, ctx: Interaction, amount: int):
		if amount > 100:
			embed = nextcord.Embed(
				title = '❌ Error',
				description = "woah, thats way too big /n try something below 100",
				color = nextcord.Color.red()
				)
			await ctx.send(embed = embed)
		else:
			await ctx.channel.purge(limit = amount)

			embed = nextcord.Embed(
				title = '❌ Purge',
				description = f'successfully purged {amount} messages',
				color = nextcord.Color.red()
			)

			await ctx.send(embed = embed)

	#Ban
	@nextcord.slash_command(name = 'ban', description = '❌Ban the user (Example: /ban @icarus or userid')
	@application_checks.has_permissions(administrator=True)
	async def ban(self, ctx: Interaction, user: nextcord.Member, reason: str = None):
		if reason is None:
			await user.ban()
			embed = nextcord.Embed(
				title = '❌Ban',
				description = f'{user.name} has been banned from {ctx.guild.name}.',
				color = nextcord.Color.red()
				)
			await ctx.send(embed = embed)
		else:
			await user.ban(reason = reason)
			embed = nextcord.Embed(
				title = '❌ Ban',
				description = f'{user.name} has been banned from {ctx.guild.name}. Reason: {reason}.',
				color = nextcord.Color.red()
				)

			await ctx.send(embed = embed)

	#Kick
	@nextcord.slash_command(name = 'kick', description = '❌ Kick the user (Example: /kick @icarus or userid')
	@application_checks.has_permissions(administrator=True)
	async def kick(self, ctx: Interaction, user: nextcord.Member, reason: str = None):

		if reason is None:

			await user.kick()

			embed = nextcord.Embed(
				title = '❌Kick',
				description = f'{user.name} has been kicked from {ctx.guild.name}.',
				color = nextcord.Color.red()
				)
			await ctx.send(embed = embed)
		else:
			await user.kick(reason = reason)
			embed = nextcord.Embed(
				title = '❌Kick',
				description = f'{user.name} has been kicked from {ctx.guild.name}. Reason: {reason}.',
				color = nextcord.Color.red()
				)
			await ctx.send(embed = embed)

	

#-----Run-----
def setup(bot):
	bot.add_cog(slashcommands(bot))