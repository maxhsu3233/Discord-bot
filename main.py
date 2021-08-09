import discord
from discord import user
from discord.ext import commands
import random
import os
import json
from discord.ext.commands import Bot

client = commands.Bot(command_prefix='$')


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('$help'))

    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))


@client.event
async def on_member_join(member):
    print(f'{member} Has join unofficial how exciting')


@client.event
async def on_member_remove(member):
    print(f'{member} left the server so sad')


@client.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(client.latency * 1000)}ms')


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    randomresponse = ['It is a duhhhhh.',
                      'I highly doubt that is true',
                      'Without a doubt it is a yes',
                      'what kind of question is that? It is a yes',
                      'Im so sorry but its a no',
                      'the person who made this bot wants to say yes',
                      'Sorry im tired try again later thanks',
                      'do you really mean that question?',
                      'NAh',
                      'fine, yes',
                      'im so sorry it does not work like that']
    await ctx.send(f'Question: {question}: {random.choice(randomresponse)}')


@client.command()
async def clear(ctx, amount=20):
    await ctx.channel.purge(limit=amount)


@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)


@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.guild.send(f'We have banned {user.name}#{user.discriminator}')


@client.command()
async def unban(ctx, *, member, member_name=None):
    banned_users = await ctx.guild.bans()
    member.name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

@client.command(aliases=['lg'])
async def ladygagaquiz(ctx):
    Ladygagaquiz = ['What is lady gagas real name ',
                      'When was the song Bad romance made',
                      'Does lady gaga have songs that are titled in german',
                      'what is her gender',
                      'Rate lady gaga 1 - 10',
                      'Does Lady gaga have a spouse',
                      'Lady gaga likes kingston',
                      'Lady gaga is weird',
                      'What does her name mean',
                      'Doesnt Lady gaga be LG that company',
                      'try again']
    await ctx.send(f'{random.choice(Ladygagaquiz)}')

@client.command(name="randomembed")
async def randomembed(ctx):
  embed = discord.Embed(
    title="random words",
    description="things and yolk make poos and that your banana",
    color=discord.Color.blue()
  )

  embed.add_field(name="Poop", value="poo peee toilet four one five minus four poo is yummy yum yum", inline=False)
  embed.add_field(name="cheese", value="cheese labeese sneeze peeze leeze vomit soz wrong word", inline=False)
  await ctx.send(embed=embed)

@client.command()
async def namemeaning(ctx):
  embed = discord.Embed(
    title="Name meaning",
    description="What does a name mean",
    color=discord.Color.red()
  )

  embed.add_field(name="Jack", value="A nice but weird guy", inline=False)
  embed.add_field(name="Jake", value="A nice guy a gamer but somtimes harrases people", inline=False)
  embed.add_field(name="Tom", value="asks people for stuff",inline=False)
  embed.add_field(name="Max", value="A annoying and gamer type guy", inline=False)
  embed.add_field(name="oliver", value="elf army", inline=False)
  embed.add_field(name="Thomas", value="a twin", inline=False)
  embed.add_field(name="issac", value="He will laugh", inline=False)
  embed.add_field(name="Logan", value="From the hollow *hollow* .........", inline=False)
  embed.add_field(name="Mason", value="Stone worker", inline=False)
  embed.add_field(name="Carter", value="Driver of a Cart", inline=False)
  embed.add_field(name="Brooklyn", value="The new york dude", inline=False)
  embed.add_field(name="Zac", value="Cool dude", inline=False)
  embed.add_field(name="Aiden", value="Little fire", inline=False)
  embed.add_field(name="Flynn", value="The red hair", inline=False)
  await ctx.send(embed=embed)

  @client.command()
  async def Namemeaning(ctx):
      embed = discord.Embed(
          title="Name meaning",
          description="What does a name mean",
          color=discord.Color.red()
      )

      embed.add_field(name="Jack", value="A nice but weird guy", inline=False)
      embed.add_field(name="Jake", value="A nice guy a gamer but somtimes harrases people", inline=False)
      embed.add_field(name="Tom", value="asks people for stuff", inline=False)
      embed.add_field(name="Max", value="A annoying and gamer type guy", inline=False)
      embed.add_field(name="oliver", value="elf army", inline=False)
      embed.add_field(name="Thomas", value="a twin", inline=False)
      embed.add_field(name="issac", value="He will laugh", inline=False)
      embed.add_field(name="Logan", value="From the hollow *hollow* .........", inline=False)
      embed.add_field(name="Mason", value="Stone worker", inline=False)
      embed.add_field(name="Carter", value="Driver of a Cart", inline=False)
      embed.add_field(name="Brooklyn", value="The new york dude", inline=False)
      embed.add_field(name="Zac", value="Cool dude", inline=False)
      embed.add_field(name="Aiden", value="Little fire", inline=False)
      embed.add_field(name="Flynn", value="The red hair", inline=False)
      await ctx.send(embed=embed)

@client.command(aliases=['rq'])
async def requirements(ctx):
    await ctx.send('Please note the bot does have some requirements too continue some of its commands the bot needs the server too enable embeds and give the bot perms we are really happy you chose us too be the bot but you have too follow the bot requirements too continue. we hope you enjoy the bot and thanks for all of your cooperation')

@client.command(aliases=['m'])
async def meme(ctx):
    meme = ['https://tenor.com/buExR.gif',
            'https://tenor.com/view/happy-they-see-me-rolling-they-hating-ride-a-turtle-adorable-cats-gif-16476656',
            'https://tenor.com/bn7ye.gif',
            'https://tenor.com/vVYN.gif',
            'https://tenor.com/K7ll.gif',
            'https://tenor.com/view/sus-imposter-among-us-among-sus-trollface-gif-21441519',
            'https://tenor.com/view/boiled-soundcloud-boiled-boiled-irl-boiled-utsc-boiled-cheesestick-agem-soundcloud-gif-20049996',
            'https://tenor.com/view/wow-omg-shocked-terrified-scared-gif-15766648',
            'https://tenor.com/view/wow-oh-wow-surprised-gasp-wife-swap-gif-16775374',
            'https://tenor.com/view/omg-oh-my-god-wow-gif-11411674',
            'https://tenor.com/view/jagyasini-jagyasini-singh-omg-omg-wow-omg-really-gif-14834363',
            'https://tenor.com/view/girl-cute-amazing-talent-run-gif-9504567',
            'https://tenor.com/view/judging-gif-4584572',
            'https://tenor.com/view/judging-judge-thinking-charlie-dellosa-hmm-gif-17580888',
            'https://tenor.com/view/dhar-mann-merobloxnoob-merobloxnoob-dhar-mann-hey-merobloxnoob-fam-hey-dhar-mann-fam-gif-22334200',
            'https://tenor.com/view/partha-dhar-bartha-gif-19055243',
            'https://tenor.com/view/were-here-excited-smile-hurrah-happy-gif-15725375',
            'https://tenor.com/view/running-hug-embrace-i-miss-you-good-to-see-you-again-gif-15965620',
            'https://tenor.com/view/forrest-gump-running-me-when-im-late-tom-hanks-gif-5144739',
            'https://tenor.com/view/fat-herobrine-minecraft-dance-funny-gif-14606354',
            'https://tenor.com/view/fat-fitness-workout-gif-17480720',
            'https://tenor.com/view/bongo-fat-tapping-cute-are-too-much-feel-full-gif-14201477',
            'https://tenor.com/view/window-car-closing-avoid-woman-gif-5103710',
            'https://tenor.com/view/michael-rosenbaum-buddy-impastor-impastor-gi-fs-window-jump-gif-5581015',
            'https://tenor.com/view/michael-rosenbaum-lex-luthor-smallville-lex-gif-14780135',
            'https://tenor.com/view/i-am-the-villain-of-the-story-michael-rosenbaum-smallville-lex-luthorr-superman-gif-14762724']

    await ctx.send(f'{random.choice(meme)}')

client.run('ODc0MTIyOTMzMTAxMDIzMzAy.YRCYaw.ytwhwupyuQuhO-fZ0Gi8158oSh4')
