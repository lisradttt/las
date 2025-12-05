from config import API_ID, API_HASH, MONGO_DB_URL, user, dev, call, logger, logger_mode, botname, GROUP as GROUPOWNER, CHANNEL as CHANNELOWNER, OWNER, OWNER_NAME
from pymongo import MongoClient
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from motor.motor_asyncio import AsyncIOMotorClient as _mongo_client_

mo = MongoClient()
mo = MongoClient(MONGO_DB_URL)
moo = mo["data"]
Bots = moo.alli
bot_name = moo.bot_name
channeldb = moo.ch
CHANNEL = {}
groupdb = moo.gr
GROUP = {}
channeldbsr = moo.chsr
CHANNELsr = {}
groupdbsr = moo.grsr
GROUPsr = {}
botss = Bots
dev = {}
devname = {}
boot = {}
mustdb = moo.must
must = {}
video_db = moo.vid
video_src = {}

def dbb():
    global db
    db = {}

dbb()

# Developer Id
async def get_dev(bot_username):
  devv = dev.get(bot_username)
  if not devv:
   Bots = botss.find({})
   for i in Bots:
       bot = i["bot_username"]
       if bot == bot_username:
         devo = i["dev"]
         dev[bot_username] = devo
         return devo
  return devv

# Developer Name
async def get_dev_name(client, bot_username):
  devv = devname.get(bot_username)
  if not devv:
   Bots = botss.find({})
   for i in Bots:
       bot = i["bot_username"]
       if bot == bot_username:
         devo = i["dev"]
         devo = await client.get_chat(devo)
         devo = devo.first_name
         devname[bot_username] = devo
         return devo
  return devv


# Bot Name
async def get_bot_name(bot_username):
      name = botname.get(bot_username)
      if not name:
        bot = bot_name.find_one({"bot_username": bot_username})
        if not bot:
            return "ميمو"
        botname[bot_username] = bot["bot_name"]
        return bot["bot_name"]
      return name

async def set_bot_name(bot_username: dict, BOT_NAME: str):
    botname[bot_username] = BOT_NAME
    bot_name.update_one({"bot_username": bot_username}, {"$set": {"bot_name": BOT_NAME}}, upsert=True)

# Bot group
async def get_group(bot_username):
      name = GROUP.get(bot_username)
      if not name:
        bot = groupdb.find_one({"bot_username": bot_username})
        if not bot:
            return GROUPOWNER 
        GROUP[bot_username] = bot["group"]
        return bot["group"]
      return name

async def set_group(bot_username: dict, group: str):
    GROUP[bot_username] = group
    groupdb.update_one({"bot_username": bot_username}, {"$set": {"group": group}}, upsert=True)

# Bot channel
async def get_channel(bot_username):
      name = CHANNEL.get(bot_username)
      if not name:
        bot = channeldb.find_one({"bot_username": bot_username})
        if not bot:
            return CHANNELOWNER 
        CHANNEL[bot_username] = bot["channel"]
        return bot["channel"]
      return name

async def set_channel(bot_username: dict, channel: str):
    CHANNEL[bot_username] = channel
    channeldb.update_one({"bot_username": bot_username}, {"$set": {"channel": channel}}, upsert=True)


# sr group
async def get_groupsr(bot_username):
      name = GROUPsr.get(bot_username)
      if not name:
        bot = groupdbsr.find_one({"bot_username": bot_username})
        if not bot:
            return GROUPOWNER 
        GROUPsr[bot_username] = bot["groupsr"]
        return bot["groupsr"]
      return name

async def set_groupsr(bot_username: dict, groupsr: str):
    GROUPsr[bot_username] = groupsr
    groupdbsr.update_one({"bot_username": bot_username}, {"$set": {"groupsr": groupsr}}, upsert=True)

# sr channel
CHANNELsr = {}

async def get_channelsr(bot_username: str) -> str:
    """الحصول على قناة البوت مع التخزين المؤقت"""
    
    # التحقق من التخزين المؤقت أولاً
    if bot_username in CHANNELsr:
        return CHANNELsr[bot_username]
    
    # البحث في قاعدة البيانات إذا لم يكن في التخزين المؤقت
    bot = channeldbsr.find_one({"bot_username": bot_username})
    
    if not bot:
        return CHANNELOWNER
    
    # تخزين في الذاكرة المؤقتة وإرجاع النتيجة
    CHANNELsr[bot_username] = bot["channelsr"]
    return bot["channelsr"]

async def set_channelsr(bot_username: dict, channelsr: str):
    CHANNELsr[bot_username] = channelsr
    channeldbsr.update_one({"bot_username": bot_username}, {"$set": {"channelsr": channelsr}}, upsert=True)

@Client.on_message(filters.command("• تعين قناة البوت •", ""))
async def set_botch(client: Client, message):
  if message.chat.username in OWNER:
   NAME = await client.ask(message.chat.id, "ارسل رابط القناه البوت الجديدة", filters=filters.text)
   channel = NAME.text
   bot_username = client.me.username
   await set_channel(bot_username, channel)
   await message.reply_text("**تم تعين قناه البوت بنجاح -**")
   return

@Client.on_message(filters.command("• تعين مجموعة البوت •", ""))
async def set_botgr(client: Client, message):
  if message.chat.username in OWNER:
   NAME = await client.ask(message.chat.id, "ارسل رابط الجروب الجديد", filters=filters.text)
   group = NAME.text
   bot_username = client.me.username
   await set_group(bot_username, group)
   await message.reply_text("**تم تعين مجموعه البوت بنجاح -**")
   return


@Client.on_message(filters.command("• تعين قناة السورس •", ""))
async def set_botchsr(client: Client, message):
  if message.chat.username in OWNER:
   NAME = await client.ask(message.chat.id, "ارسل رابط القناه البوت الجديدة", filters=filters.text)
   channelsr = NAME.text
   bot_username = client.me.username
   await set_channelsr(bot_username, channelsr)
   await message.reply_text("**تم تعين قناه السورس بنجاح -**")
   return

@Client.on_message(filters.command("• تعين مجموعة السورس •", ""))
async def set_botgrsr(client: Client, message):
  if message.chat.username in OWNER:
   NAME = await client.ask(message.chat.id, "ارسل رابط الجروب الجديد", filters=filters.text)
   groupsr = NAME.text
   bot_username = client.me.username
   await set_groupsr(bot_username, groupsr)
   await message.reply_text("**تم تعين مجموعه السورس بنجاح -**")
   return


#Mongo db
async def get_data(client):
   mongodb = _mongo_client_(MONGO_DB_URL)
   bot_username = client.me.username
   mongodb = mongodb[bot_username]
   return mongodb


# Assistant Client
async def get_userbot(bot_username):
  userbot = user.get(bot_username)
  if not userbot:
   Bots = botss.find({})
   for i in Bots:
       bot = i["bot_username"]
       if bot == bot_username:
         session = i["session"]
         userbot = Client("KERO", api_id=API_ID, api_hash=API_HASH, session_string=session)
         user[bot_username] = userbot
         return userbot
  return userbot

# Call Client
async def get_call(bot_username):
  calll = call.get(bot_username)
  if not calll:
   Bots = botss.find({})
   for i in Bots:
       bot = i["bot_username"]
       if bot == bot_username:
         userbot = await get_userbot(bot_username)
         callo = PyTgCalls(userbot, cache_duration=100)
         await callo.start()
         call[bot_username] = callo
         return callo
  return calll

# app Client
async def get_app(bot_username: str):
    # التحقق من التخزين المؤقت أولاً
    if bot_username in boot:
        return boot[bot_username]
    
    try:
        # البحث عن البوت في قاعدة البيانات
        bot_data = botss.find_one({"bot_username": bot_username})
        
        if not bot_data:
            print(f"Bot {bot_username} not found in database")
            return None
        
        # إنشاء تطبيق العميل
        token = bot_data["token"]
        app = Client(
            "KERO",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=token,
            plugins=dict(root="KERO")
        )
        
        # تخزين في الذاكرة المؤقتة
        boot[bot_username] = app
        return app
        
    except Exception as e:
        print(f"Error in get_app for {bot_username}: {e}")
        return None


# Logger
async def get_logger(bot_username):
  loggero = logger.get(bot_username)
  if not loggero:
   Bots = botss.find({})
   for i in Bots:
       bot = i["bot_username"]
       if bot == bot_username:
         loggero = i["logger"]
         logger[bot_username] = loggero
         return loggero
  return loggero


async def get_logger_mode(bot_username):
  logger = logger_mode.get(bot_username)
  if not logger:
   Bots = botss.find({})
   for i in Bots:
       bot = i["bot_username"]
       if bot == bot_username:
         logger = i["logger_mode"]
         logger_mode[bot_username] = logger
         return logger
  return logger

async def must_join(bot_username):
      name = must.get(bot_username)
      if not name:
        bot = mustdb.find_one({"bot_username": bot_username})
        if not bot:
            return "معطل"
        must[bot_username] = bot["getmust"]
        return bot["getmust"]
      return name

async def set_must(bot_username: dict, m: str):
    if m == "• تعطيل الاشتراك الإجباري •":
      ii = "معطل"
    else:
      ii = "مفعل"
    must[bot_username] = ii
    mustdb.update_one({"bot_username": bot_username}, {"$set": {"getmust": ii}}, upsert=True)


async def get_video_source(bot_username):
    name = video_src.get(bot_username)
    if not name:
      bot = video_db.find_one({"bot_username": bot_username})
      if not bot:
        return None
      video_src[bot_username] = bot.get("video_source")
      return bot.get("video_source")
    return name


async def set_video_source(bot_username: dict, VID_SO: str):
    video_src[bot_username] = VID_SO
    video_db.update_one({"bot_username": bot_username}, {"$set": {"video_source": VID_SO}}, upsert=True)


async def set_dev_user(bot_username: dict, dev_user: int):
    # update the developer of a bot in the Bots collection
    Bots.update_one({"bot_username": bot_username}, {"$set": {"dev": dev_user}}, upsert=True)

@Client.on_message(filters.command(["• تعطيل الاشتراك الإجباري •", "• تفعيل الاشتراك الإجباري •"], ""))
async def set_join_must(client: Client, message):
  if message.chat.username in OWNER:
   bot_username = client.me.username
   m = message.command[0]
   await set_must(bot_username, m)
   if message.command[0] == "• تعطيل الاشتراك الإجباري •":
     await message.reply_text("**تم تعطيل الاشتراك الإجباري بنجاح -**")
   else:
     await message.reply_text("**تم تفعيل الاشتراك الإجباري بنجاح -**")
   return
