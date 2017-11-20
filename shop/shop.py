import discord
from discord.ext import commands
import requests
from .utils.dataIO import dataIO, fileIO
from cogs.utils import checks

class shop:
    """Legend Family Shop for credits"""

    def __init__(self, bot):
        self.bot = bot
        self.banks = dataIO.load_json('data/economy/bank.json')
        self.clash = dataIO.load_json('cogs/tags.json')

    async def updateClash(self):
        self.clash = dataIO.load_json('cogs/tags.json')

    async def _add_roles(self, member, role_names):
        """Add roles"""
        server = member.server
        roles = [discord.utils.get(server.roles, name=role_name) for role_name in role_names]
        try:
            await self.bot.add_roles(member, *roles)
        except discord.Forbidden:
            raise
        except discord.HTTPException:
            raise

    async def _remove_roles(self, member, role_names):
        """Remove roles"""
        server = member.server
        roles = [discord.utils.get(server.roles, name=role_name) for role_name in role_names]
        try:
            await self.bot.remove_roles(member, *roles)
        except:
            pass

    async def _is_member(self, member):
        server = member.server
        botcommander_roles = [discord.utils.get(server.roles, name=r) for r in ["Member"]]
        botcommander_roles = set(botcommander_roles)
        author_roles = set(member.roles)
        if len(author_roles.intersection(botcommander_roles)):
            return True
        else:
            return False
            
    async def _is_rare(self, member):
        server = member.server
        botcommander_roles = [discord.utils.get(server.roles, name=r) for r in ["Rare™"]]
        botcommander_roles = set(botcommander_roles)
        author_roles = set(member.roles)
        if len(author_roles.intersection(botcommander_roles)):
            return True
        else:
            return False
            
    async def _is_epic(self, member):
        server = member.server
        botcommander_roles = [discord.utils.get(server.roles, name=r) for r in ["Epic™"]]
        botcommander_roles = set(botcommander_roles)
        author_roles = set(member.roles)
        if len(author_roles.intersection(botcommander_roles)):
            return True
        else:
            return False

    async def _is_legendary(self, member):
        server = member.server
        botcommander_roles = [discord.utils.get(server.roles, name=r) for r in ["LeGeNDary™"]]
        botcommander_roles = set(botcommander_roles)
        author_roles = set(member.roles)
        if len(author_roles.intersection(botcommander_roles)):
            return True
        else:
            return False

    def bank_check(self, user, amount):
        bank = self.bot.get_cog('Economy').bank
        if bank.account_exists(user):
            if bank.can_spend(user, amount):
                return True
            else:
                return False
        else:
            return False

    @commands.command(pass_context=True, no_pm=True)
    @checks.is_owner()
    async def sendpayouts(self, ctx):
        """Payout money for clanchest and donations."""

        server = ctx.message.server
        author = ctx.message.author
        perCrown = 300
        perDonation = 15

        await self.updateClash()

        bank = self.bot.get_cog('Economy').bank
        banks = list(self.banks['374596069989810176'])
            
        for key in range(0,len(banks)):
            if banks[key] in self.clash:
                try:
                    profiletag = self.clash[banks[key]]['tag']
                    profiledata = requests.get('http://api.cr-api.com/profile/'+profiletag, timeout=10).json()
                      
                    if profiledata['clan'] is None:
                        pass
                    else: 
                        clantag = profiledata['clan']['tag']
                        clandata = requests.get('http://api.cr-api.com/clan/{}'.format(clantag), timeout=10).json()

                        clan_tag = []
                        clan_donations = []
                        clan_clanChestCrowns = []
                        for x in range(0, len(clandata['members'])):
                            clan_tag.append(clandata['members'][x]['tag'])
                            clan_donations.append(clandata['members'][x]['donations'])
                            clan_clanChestCrowns.append(clandata['members'][x]['clanChestCrowns'])

                        index = clan_tag.index(profiletag)
                        amount = (clan_donations[index]*perDonation) + (clan_clanChestCrowns[index]*perCrown)

                        user = discord.utils.get(ctx.message.server.members, id = banks[key])

                        pay = bank.get_balance(user) + amount
                        bank.set_credits(user, pay)

                        await self.bot.send_message(user,"Hello " + user.name + ", take these credits for the " + str(clan_donations[index]) + " donations and " + str(clan_clanChestCrowns[index]) + " crowns you contributed to your clan this week. (+" + str(amount) + " credits!)")

                except Exception as e:
                    #await self.bot.say("Unable to send payout")
                    await self.bot.say(e)

    @commands.group(pass_context=True)
    async def buy(self, ctx):
        """Buy different items from the legend shop"""
        author = ctx.message.author

        await self.bot.type()

        if ctx.invoked_subcommand is None:
            await self.bot.send_file(ctx.message.channel, 'FIF5sug.png')

    @buy.command(pass_context=True, name="1")
    async def buy_1(self):


        server = ctx.message.server
        author = ctx.message.author
        legendServer = ["374596069989810176"]

        if server.id not in legendServer:
            await self.bot.say("This command can only be executed in the LeGeND Family Server")
            return

        allowed = await self._is_member(author)

        if not allowed:
            await self.bot.say("You cannot use the store, you must be a member of the family. Type !contact to ask for help.")
            return

        await self.bot.say("Command not ready yet, please contact @GR8#7968 to purchase it for you.")

    @buy.command(pass_context=True, name="2")
    async def buy_2(self):


        server = ctx.message.server
        author = ctx.message.author
        legendServer = ["374596069989810176"]

        if server.id not in legendServer:
            await self.bot.say("This command can only be executed in the LeGeND Family Server")
            return

        allowed = await self._is_member(author)

        if not allowed:
            await self.bot.say("You cannot use the store, you must be a member of the family. Type !contact to ask for help.")
            return

        await self.bot.say("Command not ready yet, please contact @GR8#7968 to purchase it for you.")

    @buy.command(pass_context=True, name="3")
    async def buy_3(self):

        server = ctx.message.server
        author = ctx.message.author
        legendServer = ["374596069989810176"]

        if server.id not in legendServer:
            await self.bot.say("This command can only be executed in the LeGeND Family Server")
            return

        allowed = await self._is_member(author)

        if not allowed:
            await self.bot.say("You cannot use the store, you must be a member of the family. Type !contact to ask for help.")
            return

        await self.bot.say("Command not ready yet, please contact @GR8#7968 to purchase it for you.")

    @buy.command(pass_context=True, name="4")
    async def buy_4(self , ctx):
        """ Buy Rare Role from the shop """
        server = ctx.message.server
        author = ctx.message.author
        legendServer = ["374596069989810176"]

        if server.id not in legendServer:
            await self.bot.say("This command can only be executed in the LeGeND Family Server")
            return

        allowed = await self._is_member(author)

        if not allowed:
            await self.bot.say("You cannot use the store, you must be a member of the family. Type !contact to ask for help.")
            return

        rare = await self._is_rare(author)
        epic = await self._is_epic(author)
        legendary = await self._is_legendary(author)

        if rare or epic or legendary:
            await self.bot.say("You are already have a special role. Type !contact to ask for help.")
            return

        if self.bank_check(author, 50000):
            bank = self.bot.get_cog('Economy').bank
            pay = bank.get_balance(author) + 50000
            bank.set_credits(author, pay)
            await self._add_roles(author,["Rare™"])
            await self.bot.say("Congratulations, you are now a **Rare™**")
        else:
            await self.bot.say("You do not have enough credits to buy this role. Type !contact to ask for help.")

    @buy.command(pass_context=True, name="5")
    async def buy_5(self , ctx):
        """ Buy Epic Role from the shop """
        server = ctx.message.server
        author = ctx.message.author
        legendServer = ["374596069989810176"]

        if server.id not in legendServer:
            await self.bot.say("This command can only be executed in the LeGeND Family Server")
            return

        allowed = await self._is_member(author)

        if not allowed:
            await self.bot.say("You cannot use the store, you must be a member of the family. Type !contact to ask for help.")
            return

        rare = await self._is_rare(author)
        epic = await self._is_epic(author)
        legendary = await self._is_legendary(author)

        if not rare:
            await self.bot.say("You need to have **Rare™** to buy this role. Type !contact to ask for help.")
            return    

        if epic or legendary:
            await self.bot.say("You are already have a special role. Type !contact to ask for help.")
            return

        if self.bank_check(author, 100000):
            bank = self.bot.get_cog('Economy').bank
            pay = bank.get_balance(author) + 100000
            bank.set_credits(author, pay)
            await self._add_roles(author,["Epic™"])
            await self.bot.say("Congratulations, you are now a **Epic™**")
        else:
            await self.bot.say("You do not have enough credits to buy this role. Type !contact to ask for help.")
        
    @buy.command(pass_context=True, name="6")
    async def buy_6(self , ctx):
        """ Buy Legendary Role from the shop """

        server = ctx.message.server
        author = ctx.message.author
        legendServer = ["374596069989810176"]

        if server.id not in legendServer:
            await self.bot.say("This command can only be executed in the LeGeND Family Server")
            return

        allowed = await self._is_member(author)

        if not allowed:
            await self.bot.say("You cannot use the store, you must be a member of the family. Type !contact to ask for help.")
            return

        rare = await self._is_rare(author)
        epic = await self._is_epic(author)
        legendary = await self._is_legendary(author)

        if not epic:
            await self.bot.say("You need to have **Epic™** to buy this role. Type !contact to ask for help.")
            return    

        if legendary:
            await self.bot.say("You are already have a special role. Type !contact to ask for help.")
            return

        if self.bank_check(author, 250000):
            bank = self.bot.get_cog('Economy').bank
            pay = bank.get_balance(author) + 250000
            bank.set_credits(author, pay)
            await self._add_roles(author,["LeGeNDary™"])
            await self.bot.say("Congratulations, you are now a **LeGeNDary™**")
        else:
            await self.bot.say("You do not have enough credits to buy this role. Type !contact to ask for help.")

def setup(bot):
    bot.add_cog(shop(bot))
