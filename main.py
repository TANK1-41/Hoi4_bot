import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

client = commands.Bot(command_prefix="!")

allNations = ["afghanistan", "albania", "argentina", "australia", "austria", "belgium", "bhutan", "bolivia", "brazil",
              "british malaya", "british raj", "bulgaria", "chile", "china", "colombia", "communist china",
              "costa rica", "cuba", "czechoslovakia", "denmark", "dominican republic", "dominion of canada",
              "dutch east indies", "ecuador", "el salvador", "estonia", "ethiopia", "finland", "france", "german reich",
              "kingdom of greece", "guangxi clique", "guatemala", "haiti", "Honduras", "kingdom of hungary", "iran",
              "iraq", "ireland", "italy", "japan", "latvia", "liberia", "lithuania", "luxembourg", "manchukuo",
              "mengkukuo", "mexico", "mongolia", "nepal", "netherlands", "new zealand", "nicaragua", "norway", "oman",
              "panama", "paraguay", "peru", "philippines", "poland", "portugal", "romania", "saudi arabia", "shanxi",
              "siam", "sinkiang", "south africa", "soviet union", "spain", "sweden", "switzerland", "tannu tuva",
              "tibet", "turkey", "united kingdom", "united states", "uruguay", "venezuela", "xibei san ma", "yemen",
              "yugoslavia", "yunnan"]
claimedNations = []

playerNations = []

idPlayer = []

empty = []


@client.event
async def on_ready():
    print("bot is online")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("!h"))


@client.command()
async def ping(ctx):
    await ctx.send(f"pong! {round(client.latency * 1000)}ms")


@client.command(aliases=['c'])
async def claim(ctx, *, nation="none"):
    nation = nation.lower()
    if nation == "none":
        await ctx.send(f"Please pick a nation after !c or !claim. \n Ex. !c italy")
    else:
        if nation in allNations:
            i = 1
        else:
            i = 0
        if i == 1:
            if nation in claimedNations:
                index = claimedNations.index(nation)
                await ctx.send(f"Sorry that nation is already taken by {playerNations[index]}")
            else:
                claimedNations.append(nation)
                playerNations.append(str(ctx.message.author))
                idPlayer.append(ctx.message.author.id)
                await ctx.send(f"{ctx.message.author} claimed {nation}")

        elif i == 0:
            await ctx.send(
                f"That nation is not valid. You can find a list of nations here https://hoi4.paradoxwikis.com/Countries"
            )
        else:
            await ctx.send(f"Error please contact admin to fix fatal Error")


@client.command(aliases=['uc'])
async def unclaim(ctx, *, nation="none"):
    index = idPlayer.index(ctx.message.author.id)
    nation = claimedNations[index]
    claimedNations.pop(index)
    playerNations.pop(index)
    idPlayer.pop(index)
    await ctx.send(f"{nation} is once again available")


@client.command(aliases=['cn'])
async def claimed(ctx, *, nation="none"):
    if len(claimedNations) > 0:
        for index in range(len(claimedNations)):
            await ctx.send(f"{claimedNations[index]} is claimed by {playerNations[index]}")
    else:
        await ctx.send(f"No nations have been claimed yet")


@client.command(aliases=['uca'])
@commands.has_permissions(administrator=True)
async def unclaimall(ctx, *, nation="none"):
    print(len(claimedNations))
    x = len(claimedNations)
    x = x - 1
    while x >= 0:
        print(x)
        claimedNations.pop(x)
        playerNations.pop(x)
        idPlayer.pop(x)
        x = x - 1

    print(claimedNations, playerNations, idPlayer)
    await ctx.send(f"All nation claims cleared")


@client.command(aliases=['h'])
async def new(ctx, *, nation="none"):
    await ctx.send(
            f"**!c** or **!claim** followed by a nation is how you claim a nation\n"
            f"**!uc** or **!unclaim** will unclame all of your current claims\n"
             f"**!cn** or **!claimed** will show you all the nations currently claimed\n"
            f"**!uca** or **!unclaimall** is only available to administrators and will clear all claims\n"
                   )

client.run("token_here")
