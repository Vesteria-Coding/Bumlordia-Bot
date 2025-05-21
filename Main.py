from discord.ext import commands as cmds
import discord
import asyncio
import random

intents = discord.Intents.all()
bot = cmds.Bot(command_prefix=r'//', intents=intents, case_insensitive=True)

# Setup
ALLOWED_USER_ID = 12345678901234567890 # Replace With Actual User ID
gif_urls = [
    "https://cdn.discordapp.com/attachments/1306727963433369681/1362954388867645532/wheres_my_toy_-_Made_with_Clipchamp.gif",
    "https://cdn.discordapp.com/attachments/1263420906034958358/1372297426781733004/BUMxLORD_bumxloTerrorLord.gif",
    "https://cdn.discordapp.com/attachments/1263420906034958358/1372297426462838834/BUMxLORD_bumxloRobloxRizzLord.gif",
    "https://cdn.discordapp.com/attachments/1263420906034958358/1372297426072764416/BUMxLORD_bumxloDespair_premium_trial.gif",
    "https://cdn.discordapp.com/attachments/1263420906034958358/1372297425158537337/BUMxLORD_bumxloDanceLord.gif"
]


def join_message(user_mention):
    welcome_messages = [
        f"Welcome to Bumlordia, {user_mention}! Our throne of couches awaits you.",
        f"Ahoy {user_mention}! You've docked at Bumlordia — no work, all weird.",
        f"Yo {user_mention}, welcome! Grab a beanbag and lower your expectations.",
        f"Hey {user_mention}, congrats! You’ve officially joined the lazy elite.",
        f"{user_mention} has arrived! Someone fetch the sacred sweatpants.",
        f"Welcome, {user_mention}! All hail the newest bum of Bumlordia!",
        f"{user_mention}, you just leveled up into Bumlord status.",
        f"Sup {user_mention}! Take a seat, preferably horizontal.",
        f"Welcome to Bumlordia, {user_mention}. The remote is lost forever.",
        f"Greetings, {user_mention}. May your snacks be endless and your pants optional.",
        f"{user_mention} has entered the chat! Finally, someone to blame!",
        f"Welcome, {user_mention}! The only rule here is… wait, we had rules?",
        f"Hi {user_mention}, here's your complimentary imaginary crown of laziness.",
        f"{user_mention} joined. Time to pretend we were doing something productive.",
        f"Welcome to Bumlordia, {user_mention}. We hope you didn’t come for ambition.",
        f"Look who crawled in—it's {user_mention}! Make yourself unmotivated.",
        f"Welcome {user_mention}, don’t worry, nobody here has their life together either.",
        f"New bum in town: {user_mention}! The couch cult welcomes you.",
        f"Greetings, {user_mention}. You’ve now been officially unproductive.",
        f"Say hello to {user_mention}, our newest expert in procrastination.",
        f"Welcome to Bumlordia, {user_mention}! Your responsibilities just left the chat.",
        f"Yo {user_mention}, chill is mandatory. Effort is optional.",
        f"Hey {user_mention}, welcome to the land of infinite naps.",
        f"What’s up, {user_mention}? We hope you brought snacks.",
        f"Enter {user_mention}, destroyer of motivation!",
        f"Welcome, {user_mention}! Kick off your shoes, and your goals.",
        f"Hi {user_mention}, we’ve been expecting you. Mostly because we expect nothing.",
        f"Welcome to Bumlordia, {user_mention}, population: still lying down.",
        f"New arrival: {user_mention}. Someone hand them the remote!",
        f"Sup {user_mention}! The floor is the new chair here.",
        f"Welcome, {user_mention}. Now let’s all pretend to do something.",
        f"Brace yourselves, {user_mention} has entered the kingdom of idle chaos!",
        f"{user_mention} just joined! Make room in the snack drawer.",
        f"New member alert! {user_mention}, prepare for extreme lounging.",
        f"{user_mention}, welcome to Bumlordia. Where dreams nap eternally.",
        f"Greetings, {user_mention}. Check your ambition at the door.",
        f"Welcome, {user_mention}, official Bumlord Trainee. First lesson: snoozing.",
        f"Yo {user_mention}, throw away your calendar. Time doesn’t work here.",
        f"Cheers {user_mention}! Time to do everything later. Or never.",
        f"{user_mention}, welcome to Bumlordia. It’s a lifestyle, not a phase.",
        f"Hey {user_mention}, you smell like potential… wasted potential.",
        f"Welcome, {user_mention}. You bring the bum, we bring the lordia.",
        f"What's good, {user_mention}? Nothing. That’s the point.",
        f"Welcome, {user_mention}. You’ve entered the realm of legendary loafers.",
        f"{user_mention}, the Couch Tribunal will see you now.",
        f"Welcome to Bumlordia, {user_mention}. Hope you like naps and nonsense.",
        f"Yooo {user_mention}, you're now legally allowed to do nothing here.",
        f"New challenger: {user_mention}! Challenge: sit still forever.",
        f"{user_mention} just joined. Things might change. But probably won’t.",
        f"Welcome {user_mention}, the last place before your productivity died.",
        f"Ah, {user_mention}! Our next bum-in-training has arrived!",
        f"Welcome, {user_mention}. You're among slackers now.",
        f"{user_mention}, you’ve entered the realm of chaotic comfort.",
        f"Bow before {user_mention}, the new Duke of Duvets!",
        f"Welcome to Bumlordia, {user_mention}. May your willpower rest in peace.",
        f"Greetings {user_mention}, please leave your ambitions at the door.",
        f"{user_mention} is here! Hide the responsibilities!",
        f"Welcome {user_mention}, we're legally obligated to pretend we care.",
        f"You’ve made it, {user_mention}. Now do absolutely nothing with pride.",
        f"What’s poppin, {user_mention}? Hopefully not effort.",
        f"Oh snap, it’s {user_mention}! Time to reset productivity to 0.",
        f"Welcome {user_mention}, you’ll fit right in doing absolutely nothing.",
        f"Praise be, {user_mention} has joined the ranks of the recumbent!",
        f"{user_mention} arrived. Work ethic exited.",
        f"Hi {user_mention}, welcome to Bumlordia. May your bed be ever warm.",
        f"Welcome, {user_mention}. We're all mad here. Mostly lazy, but mad too.",
        f"{user_mention} just rolled in. Someone hand them the snack scepter.",
        f"Hey {user_mention}, Bumlordia’s motto: 'Later sounds good.'",
        f"What’s up {user_mention}? Not our motivation, that’s for sure.",
        f"Welcome to Bumlordia, where {user_mention} now holds a sacred potato chip.",
        f"Oh look, a wild {user_mention} appeared. It used *Sit*! It’s super effective.",
        f"Cheers, {user_mention}. You're now among the horizontally inclined.",
        f"Welcome, {user_mention}. The Wi-Fi is strong, the ambition is not.",
        f"Hey {user_mention}, don’t worry—we don’t *do* things here.",
        f"Ahoy {user_mention}, may your couch never betray you.",
        f"Welcome, {user_mention}. Side quests only. Main quests are too hard.",
        f"{user_mention}, great news! You're now one of *us*.",
        f"Welcome to the lair, {user_mention}. Our socks may not match, but our vibes do.",
        f"Hark! {user_mention} has entered. Let the memes flow like soda.",
        f"It’s {user_mention}! Do they bring motivation? Nope? Perfect.",
        f"Welcome {user_mention}, a new soul to procrastinate with.",
        f"Make way for {user_mention}, conqueror of couch cushions!",
        f"Hey {user_mention}, you now share custody of the community pizza stain.",
        f"Welcome {user_mention}. Please don’t ask for structure or schedules.",
        f"Sup {user_mention}. Time is fake, and so are our plans.",
        f"What’s that smell? Oh, it’s {user_mention}! Smells like greatness... or pizza.",
        f"Hello {user_mention}, you now have free access to all of our collective nonsense.",
        f"Welcome, {user_mention}. Warning: Side effects may include severe laziness.",
        f"Welcome aboard, {user_mention}. Set sail for snack island!",
        f"Yo {user_mention}, the fridge is empty but our hearts are full.",
        f"Ahoy {user_mention}, welcome to the ship of chill. It doesn’t move.",
        f"Greetings {user_mention}. Step over the pile of dreams—we don’t use them.",
        f"Look alive, {user_mention}! Just kidding. Go back to lounging.",
        f"Welcome {user_mention}, where ambition goes to take a nap.",
        f"It’s {user_mention}! Time to increase the bum population by 1.",
        f"{user_mention}, you’ve unlocked Bumlord Mode. Passive XP only.",
        f"Behold! {user_mention}, the chosen one who shall sit among bums.",
        f"Welcome {user_mention}, you're now a professional nap consultant.",
        f"Make way for {user_mention}, destroyer of to-do lists!",
        f"New update: {user_mention} joined. Still no bug fixes.",
        f"Congrats {user_mention}, you've entered the most chaotic chill zone ever.",
        f"Hey {user_mention}, welcome to the infinite loop of 'I'll do it later.'",
        f"{user_mention} has joined the cult—uhh, community of Bumlordia.",
        f"It’s a bird! It’s a plane! Nope, just {user_mention} with chips.",
        f"All rise for... wait, no. Never mind. Sit down, {user_mention}.",
        f"Welcome {user_mention}. Motivation is optional. Naps are mandatory.",
        f"Look who finally joined—{user_mention}! Slackers unite!",
        f"Hey {user_mention}, your destiny lies somewhere between nap and snack.",
        f"You made it, {user_mention}. Now let’s accomplish absolutely nothing together.",
        f"Welcome {user_mention}, hope your back is ready for 12 hours of sitting.",
        f"{user_mention}, we’re like family. Dysfunctional and online too much.",
        f"Incoming transmission: {user_mention} has joined the sleepover of chaos.",
        f"Welcome {user_mention}, we don’t stand for anything. Literally.",
        f"Hi {user_mention}, welcome to Bumlordia, where effort is illegal.",
        f"New arrival detected: {user_mention}. Lower expectations accordingly.",
        f"Welcome to Bumlordia, {user_mention}, population: professional procrastinators.",
        f"Yeehaw {user_mention}, this lazy rodeo just got realer.",
        f"New legend joined: {user_mention}, the Unbothered.",
        f"Welcome {user_mention}. Remember: if you’re moving, you’re trying too hard.",
        f"Oh look, it’s {user_mention}! Let’s do nothing about it.",
        f"Greetings, {user_mention}. You're just in time to miss everything.",
        f"Welcome {user_mention}. The Bum Council acknowledges your chill.",
        f"Presenting... {user_mention}! The nap champion of 2025!",
        f"{user_mention}, welcome. May your snack crumbs find peace in our couch crevices.",
        f"Alert: {user_mention} has joined. Resume loafing.",
        f"What’s good, {user_mention}? Definitely not our productivity levels.",
        f"Hey {user_mention}, all schedules were burned at the gate.",
        f"Welcome {user_mention}, please deposit all effort at the entrance.",
        f"{user_mention}, the Bumlords await your terrible memes.",
        f"Yo {user_mention}, let’s collectively not finish that thing we started.",
        f"Hey hey {user_mention}, come waste time with the best of us!",
        f"{user_mention}, come for the chaos, stay because you’re too lazy to leave.",
        f"Bumlordia welcomes {user_mention}! We expect the bare minimum.",
        f"{user_mention}, this server runs on vibes, not plans.",
        f"Glad you’re here, {user_mention}! We’re not doing anything, and that’s okay.",
        f"Welcome {user_mention}. Your chill license has been activated.",
        f"Ah, {user_mention}. Another noble procrastinator joins the fold.",
        f"Hey {user_mention}, no pressure. Just eternal low pressure.",
        f"Welcome to Bumlordia, {user_mention}, where every day is Sunday afternoon.",
        f"You're here, {user_mention}. That's... something.",
        f"Join us, {user_mention} Together, we shall rule the Couchverse!",
        f"Welcome {user_mention}. Sorry we didn’t clean up. It’s our aesthetic.",
        f"Incoming: {user_mention}! Please don’t expect structure.",
        f"Hi {user_mention}, you’re not late—we’re just always early for tomorrow.",
        f"Yo {user_mention}, you bring the lazy, we bring the nonsense.",
        f"Welcome to the kingdom, {user_mention}. The kingdom of chill.",
        f"Hey {user_mention}, it's okay. We don't know what we're doing either.",
        f"Welcome, {user_mention}. Take a nap. You’ve earned it by arriving.",
        f"Oh good, {user_mention}'s here. The vibes are now legally certified.",
        f"Hark, {user_mention} has arrived! Someone pass them the lore. And chips.",
        f"{user_mention}, welcome. The only thing we raise here is eyebrows.",
        f"Welcome to Bumlordia, {user_mention}. The final destination of your productivity journey.",
        f"Welcome to Bumlordia, {user_mention}! The official afterparty of [twitch.tv/bumxlord](https://www.twitch.tv/bumxlord)",
        f"Ahoy {user_mention}! You’ve landed in the Discord port of Bumxlord's streamship.",
        f"Yo {user_mention}, welcome! The VODs are muted, but the chaos is eternal.",
        f"Hey {user_mention}, congrats! You’ve unlocked Bumlordia’s Discord DLC.",
        f"{user_mention} has arrived! Someone ping the emote summoning circle.",
        f"Welcome, {user_mention}! You’ve officially crossed from Twitch chat into the realm of bums.",
        f"{user_mention}, you just rage-quit real life and joined the post-stream nap zone.",
        f"Sup {user_mention}! You made it from Twitch to Discord — now lower your expectations.",
        f"Welcome to the Discord lair, {user_mention}. Sponsored by accidental mutes and unmodded chaos.",
        f"Greetings, {user_mention}. You’ve entered Bumlordia’s extended universe.",
        f"{user_mention} has entered the Discord! Someone drop a !welcome in spirit.",
        f"Welcome, {user_mention}! The only goal here is to post memes and dodge pings.",
        f"Hi {user_mention}, glad you subbed to the vibe and joined the server too.",
        f"{user_mention} joined. Time to relive the scuffed stream in text form.",
        f"Welcome to Bumlordia, {user_mention}. Don’t worry, Twitch didn’t prepare you for this.",
        f"Look who crawled in from chat—it's {user_mention}! Drop an emote and get comfy.",
        f"Welcome {user_mention}, no stream delay here—just delayed responsibilities.",
        f"New bum in the server: {user_mention}! The couch cult grows stronger.",
        f"Greetings, {user_mention}. You’ve entered post-stream purgatory.",
        f"Say hello to {user_mention}, our newest expert in clipping bad decisions.",
        f"Welcome to Bumlordia, {user_mention}! No alerts here, just unfiltered nonsense.",
        f"Yo {user_mention}, chill is mandatory. And yes, we do judge lurkers lovingly.",
        f"Hey {user_mention}, welcome to the land of disconnected voice chats.",
        f"What’s up, {user_mention}? Hope your notifications are off.",
        f"Enter {user_mention}, destroyer of serious discussion threads.",
        f"Welcome, {user_mention}! Kick off your shoes, and mute general.",
        f"Hi {user_mention}, we’ve been expecting you. Twitch chat sent us a warning.",
        f"Welcome to Bumlordia, {user_mention}, population: Discord degenerates.",
        f"New arrival: {user_mention}. Someone @everyone—just kidding, don’t.",
        f"Sup {user_mention}! You’ve found the only channel that’s worse than Twitch spam.",
        f"Welcome, {user_mention}. Now let’s all pretend we’re productive between streams.",
        f"Brace yourselves, {user_mention} just joined. Mods are typing…",
        f"{user_mention} just joined! Someone hand them the ping shield.",
        f"New member alert! {user_mention}, prepare for emoji-based communication only.",
        f"{user_mention}, welcome to Bumlordia. No streams here—just stream energy.",
        f"Greetings, {user_mention}. Please stow your ambition and react to the welcome post.",
        f"Welcome, {user_mention}, official Bumlord Trainee. First test: survive the memes.",
        f"Yo {user_mention}, throw away your Twitch schedule. This is chaos unscripted.",
        f"Cheers {user_mention}! Time to do everything later. Or forget completely.",
        f"{user_mention}, welcome to Bumlordia. Home of late streams and early chaos.",
        f"Hey {user_mention}, you smell like potential… mod material? Kidding.",
        f"Welcome, {user_mention}. You bring the chat, we bring the chaos.",
        f"What's good, {user_mention}? Nothing but emotes and inside jokes.",
        f"Welcome, {user_mention}. The only rules here are twitch emotes and sarcasm.",
        f"{user_mention}, the Chat Tribunal will see you now.",
        f"Welcome to Bumlordia, {user_mention}. May your internet stay stable.",
        f"Yooo {user_mention}, you're now legally allowed to spam emotes here.",
        f"New challenger: {user_mention}! Challenge: survive the voice channels.",
        f"{user_mention} just joined. Things might get worse. Or better.",
        f"Welcome {user_mention}, the last place before your sleep schedule dies.",
        f"Ah, {user_mention}! Our next chat warrior has arrived!",
        f"Welcome, {user_mention}. You're among chat legends now.",
        f"{user_mention}, you’ve entered the realm of GIF wars.",
        f"Bow before {user_mention}, the new Duke of Discord!",
        f"Welcome to Bumlordia, {user_mention}. May your ping be low and your memes dank.",
        f"Greetings {user_mention}, please leave your seriousness at the door.",
        f"{user_mention} is here! Hide your spoilers!",
        f"Welcome {user_mention}, we're legally obligated to give you a channel.",
        f"You’ve made it, {user_mention}. Now do absolutely nothing but chat.",
        f"What’s poppin, {user_mention}? Hopefully not drama.",
        f"Oh snap, it’s {user_mention}! Time to reset the chat to chaos mode.",
        f"Welcome {user_mention}, you’ll fit right in spamming nonsense.",
        f"Praise be, {user_mention} has joined the ranks of the chatters!",
        f"{user_mention} arrived. Serious talk exited.",
        f"Hi {user_mention}, welcome to Bumlordia. May your mic never cut out.",
        f"Welcome, {user_mention}. We're all weird here. Mostly weird.",
        f"{user_mention} just rolled in. Someone hand them the chat wheel!",
        f"Hey {user_mention}, Bumlordia’s motto: 'Spam first, ask questions later.'",
        f"What’s up {user_mention}? Not moderation, that’s for sure.",
        f"Welcome to Bumlordia, where {user_mention} now holds a sacred emote.",
        f"Oh look, a wild {user_mention} appeared. It used *Spam*! It’s super effective.",
        f"Cheers, {user_mention}. You're now among the ping warriors.",
        f"Welcome, {user_mention}. The notifications are endless, the sleep is scarce.",
        f"Hey {user_mention}, don’t worry—we don’t *do* voice chats here.",
        f"Ahoy {user_mention}, may your headset never disconnect.",
        f"Welcome, {user_mention}. Side quests only. Main quests are a myth.",
        f"{user_mention}, great news! You're now one of *us*.",
        f"Welcome to the lair, {user_mention}. Our keyboard warriors salute you.",
        f"Hark! {user_mention} has entered. Let the memes fly freely.",
        f"It’s {user_mention}! Do they bring snacks? Nope? Perfect.",
        f"Welcome {user_mention}, a new soul to meme with.",
        f"Make way for {user_mention}, conqueror of unread messages!",
        f"Hey {user_mention}, you now share custody of the spam folder.",
        f"Welcome {user_mention}. Please don’t ask for voice channel etiquette.",
        f"Sup {user_mention}. Time is fake, and so are our admin powers.",
        f"What’s that sound? Oh, it’s {user_mention}! Sounds like chaos.",
        f"Hello {user_mention}, you now have free access to all our inside jokes.",
        f"Welcome, {user_mention}. Warning: Side effects may include extreme laughter.",
        f"Welcome aboard, {user_mention}. Set sail for the meme ocean!",
        f"Yo {user_mention}, the chat is wild but your presence is wilder.",
        f"Ahoy {user_mention}, welcome to the ship of banter. It doesn’t sink.",
        f"Greetings {user_mention}. Step over the chat logs—we don’t read them.",
        f"Look alive, {user_mention}! Just kidding. Chill and spam.",
        f"Welcome {user_mention}, where drama goes to die.",
        f"It’s {user_mention}! Time to increase the chat activity by 1.",
        f"{user_mention}, you’ve unlocked Meme Lord Mode. Passive XP only.",
        f"Behold! {user_mention}, the chosen one who shall meme among legends.",
        f"Welcome {user_mention}, you're now a professional chat clown.",
        f"Make way for {user_mention}, destroyer of serious conversations!",
        f"New update: {user_mention} joined. Still no moderation.",
        f"Congrats {user_mention}, you've entered the most chaotic chat ever.",
        f"Hey {user_mention}, welcome to the infinite loop of spam and memes.",
        f"{user_mention} has joined the cult—uhh, community of Bumlordia Discord.",
        f"It’s a bird! It’s a plane! Nope, just {user_mention} with pings.",
        f"All rise for... wait, no. Never mind. Sit down, {user_mention}.",
        f"Welcome {user_mention}. Moderation is optional. Memes are mandatory.",
        f"Look who finally joined—{user_mention}! Chat wars intensify.",
        f"Hey {user_mention}, your destiny lies somewhere between ping and meme.",
        f"You made it, {user_mention}. Now let’s accomplish absolutely nothing but chat together.",
        f"Welcome {user_mention}, hope your mic is unmuted for once.",
        f"{user_mention}, we’re like family. Dysfunctional and online 24/7.",
        f"Incoming transmission: {user_mention} has joined the voice channel of chaos.",
        f"Welcome {user_mention}, we don’t talk here. We meme.",
        f"Hi {user_mention}, welcome to Bumlordia, where modding is a myth.",
        f"New arrival detected: {user_mention}. Ping accordingly.",
        f"Welcome to Bumlordia, {user_mention}, population: professional ping abusers.",
        f"Yeehaw {user_mention}, this spam rodeo just got realer.",
        f"New legend joined: {user_mention}, the Unmuted.",
        f"Welcome {user_mention}. Remember: if you’re typing, you’re trying too hard.",
        f"Oh look, it’s {user_mention}! Let’s meme about it.",
        f"Greetings, {user_mention}. You're just in time to miss everything important.",
        f"Welcome {user_mention}. The Chat Council acknowledges your spam.",
        f"Presenting... {user_mention}! The ping champion of 2025!",
        f"{user_mention}, welcome. May your pings never go unnoticed.",
        f"Alert: {user_mention} has joined. Resume spamming.",
        f"What’s good, {user_mention}? Definitely not the mods.",
        f"Hey {user_mention}, all mute buttons were burned at the gate.",
        f"Welcome {user_mention}, please deposit all seriousness at the entrance.",
        f"{user_mention}, the Chat Lords await your terrible memes.",
        f"Yo {user_mention}, let’s collectively not finish that chat topic.",
        f"Hey hey {user_mention}, come waste time with the best of us!",
        f"{user_mention}, come for the memes, stay because you’re too lazy to leave.",
        f"Bumlordia welcomes {user_mention}! We expect the bare minimum in chat.",
        f"{user_mention}, this server runs on memes, not plans.",
        f"Glad you’re here, {user_mention}! We’re not doing anything productive.",
        f"Welcome {user_mention}. Your spam license has been activated.",
        f"Ah, {user_mention}. Another noble memer joins the fold.",
        f"Hey {user_mention}, no pressure. Just eternal ping pressure.",
        f"Welcome to Bumlordia, {user_mention}, where every day is meme day.",
        f"You're here, {user_mention}. That’s... something.",
        f"Join us, {user_mention}. Together, we shall rule the Chatverse!",
        f"Welcome {user_mention}. Sorry we didn’t clean up. It’s our aesthetic.",
        f"Incoming: {user_mention}! Please don’t expect order.",
        f"Hi {user_mention}, you’re not late—we’re just always early for tomorrow.",
        f"Yo {user_mention}, you bring the memes, we bring the chaos.",
        f"Welcome to the kingdom, {user_mention}. The kingdom of banter.",
        f"Hey {user_mention}, it's okay. We don't know what we're doing either.",
        f"Welcome, {user_mention}. Take a break. You’ve earned it by arriving.",
        f"Oh good, {user_mention}'s here. The chat is now certified chaotic.",
        f"Hark, {user_mention} has arrived! Someone pass them the lore. And pings.",
        f"{user_mention}, welcome. The only thing we raise here is volume.",
        f"Welcome to Bumlordia, {user_mention}. The final destination of your sanity.",
    ]
    return random.choice(welcome_messages)

# Bot Setup
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, cmds.CommandNotFound):
        await ctx.send("That command doesn't exist. Try '//commands' to see available commands.")
    else:
        # Optional: log or raise unhandled errors
        raise error

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name='︱welcome')
    if channel:
        await channel.send(join_message(member.mention))

# Bot Commands
@bot.command(name='welcome')
async def welcome(ctx, user: discord.Member):
    await ctx.send(f'{user.mention} Welcome To The Server!')

@bot.command(name='youtube')
async def youtube(ctx):
    await ctx.send('https://www.youtube.com/@DIGIT4LBUMLORD')

@bot.command(name='twitch')
async def twitch(ctx):
    await ctx.send('https://www.twitch.tv/bumxlord')

@bot.command(name='cat')
async def cat(ctx):
    await ctx.send('ᓚᘏᗢ')

@bot.command(name='cat2')
async def cat2(ctx):
    await ctx.send('ฅ^•ﻌ•^ฅ')

@bot.command(name='bunny')
async def bunny(ctx):
    await ctx.send(r'''
(\(\
( -.-)
o_(")(")
''')

@bot.command(name='ping')
async def ping(ctx):
    latency = bot.latency * 1000
    await ctx.send(f'Pong! `{latency:.2f}ms`')

@bot.command(name='gif')
async def send_random_gif(ctx):
    random_gif_url = random.choice(gif_urls)
    embed = discord.Embed(title=f"Here's a random GIF!")
    embed.set_image(url=random_gif_url)
    await ctx.send(embed=embed)

@bot.command(name='rules')
async def rules(ctx):
    embed = discord.Embed(
        title="Server Rules",
        description="Please read and follow these rules carefully:",
        color=discord.Color.red()
    )
    embed.add_field(name="1. Place Holder For Title", value="Place Holder For Description", inline=False)
    embed.add_field(name="2. Place Holder For Title", value="Place Holder For Description", inline=False)
    embed.add_field(name="3. Place Holder For Title", value="Place Holder For Description", inline=False)
    embed.add_field(name="4. Place Holder For Title", value="Place Holder For Description",inline=False)
    embed.add_field(name="5. Place Holder For Title", value="Place Holder For Description", inline=False)
    embed.add_field(name="6. Place Holder For Title", value="Place Holder For Description", inline=False)
    embed.add_field(name="7. Place Holder For Title", value="Place Holder For Description", inline=False)
    embed.add_field(name="8. Place Holder For Title", value="Place Holder For Description", inline=False)
    embed.add_field(name="9. Place Holder For Title", value="Place Holder For Description", inline=False)
    embed.add_field(name="10. Place Holder For Title", value="Place Holder For Description", inline=False)
    # embed.add_field(name="6. Place Holder For Title", value="Place Holder For Description", inline=False)
    embed.set_footer(text="Thanks for being part of Bumlordia!")
    await ctx.send(embed=embed)

@bot.command(name='bans')
@cmds.has_permissions(ban_members=True)
async def bans(ctx):
    bans = [ban async for ban in ctx.guild.bans()]
    await ctx.send(f"{len(bans)} Members Have Been Banned From This Server.")

@bot.command(name='stop')
async def restricted_command(ctx):
    if ctx.author.id == ALLOWED_USER_ID:
        await ctx.send("Stoping Bot")
        await bot.close()
    else:
        await ctx.send("You do not have permission to use this command.")

@bot.command(name='commands')
async def commands(ctx):
    await ctx.send('''
```//commands | list all commands
//welcome | welcomes pinged user
//ping | sends ping of the bot
//twitch | prints twitch link
//youtube | prints youtube link
//gif | print random gif
//cat | ᓚᘏᗢ
//cat2 | ฅ^•ﻌ•^ฅ
//bunny | sends bunny
//bans | sends number of bans
//rules | sends rules```''')

bot.run('PUT_YOUR_BOT_TOKEN_HERE')
