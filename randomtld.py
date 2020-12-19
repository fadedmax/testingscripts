import voxelbotutils as utils
import random

class PingCommand(utils.Cog):

    @utils.command()
    async def randomtld(self, ctx:utils.Context, name:str):
        """
        Random TLD with a name
        """
        async with self.bot.session.get('http://data.iana.org/TLD/tlds-alpha-by-domain.txt') as r:
            text = await r.text()

        # split domain into lines
        domaintlds = text.strip().split('\n')

        # get a random TLD
        randomdomain = random.choice(domaintlds)

        # make it lowercase
        domainlower = randomdomain.lower()

        await ctx.send(f{name}.{domainlower}")


def setup(bot:utils.Bot):
    x = PingCommand(bot)
    bot.add_cog(x)
