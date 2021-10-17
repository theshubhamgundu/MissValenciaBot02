import random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from cinderella import dispatcher
from cinderella.modules.disable import DisableAbleCommandHandler

ABUSE_STRINGS = (
    "Madharchod",
    "Behenchod ",
    "Harami",
    "Betichod",
    "Randi",
    "Randibaaz",
    "Lund lele mera",
    "Chut marlunga teri",
    "Lund ke saudagar",
    "Gand ke chhed",
    "Lund ke tope",
    "Rakheil",
    "Chinnal",
    " Maa ke lode",
    "Maa ka bhosda fadu teri",
    "Behen ke lode",
    "Teri behen me bhosde me kutte ka lund",
    "100 baap ki najayas aulad",
    "Teri behen ki chut me kutte ka lund",
    "Jhaant ke pille",
    "Madharchod jhaant ke baal baap ko mat sikha lowde",
    "Teri behan ki geeli chut pe roller chala dunga or road bana dunga randi ki paidaish",
    "BH33N K LODEE DUSRO KI KMAYI KHAANE WALE JHAANTH SE PILLE BAN OWNER TERII MAA KA BHOXDAA MAAR K TUJHEE OWNER BNATA HUN MAA K LODEE 😁😁 AUKAAT BNA FADDEBAJI  KI BHEN K LODEE",
)

SONG_STRINGS = (
    "🎶 Kisi Ki Muskuraahaton Pe Ho Nisaar... Kisi Ka Dard Mil Sake To Le Udhaar... Kisi Ke Vaaste Ho Tere Dil Men Pyaar... Jeena Isi Ka Naam Hai... 🎶.",
    "🎶 Maana Apani Jeb Se Fakeer Hain... Phir Bhi Yaaron... Dil Ke Ham... Ameer Hain... Maana Apani Jeb... Se Fakeer Hain... Phir Bhi Yaaron... Dil Ke Ham Ameer Hain... 🎶",
    "🎶 Shikwa nahin kisi se, kisi se gila nahin... Naseeb mein nahin tha jo humko mila nahin... 🎶", 
    "🎶 Ajeeb dastan hai yeh Kahan shuru kahan khatam... Yeh manzile hai kaunsi Na voh samajh sake na hum... 🎶", 
    "🎶 Yaara teri yaari ko Maine to khuda maana, Yaad karegi duniya Tera mera afsana... Tere jaisa yaar kahan, Kahan aisa yaarana Yaad karegi duniya Tera mera afsana... 🎶", 
    "🎶 Tum sath ho ya na ho kya fark hai.... bedard thi jindagi bedard hai.... 🎶", 
    "🎶 Kabra pe mushkura ke khadi ho jindagi aise marna hai mujhe... 🎶", 
    "🎶 Mauka Milega To Ham Bta Denge,, Tumhe Kitna Pyaar Karte Hai Sanam… 🎶", 
    "🎶 Pal bhar ke liye koi hume pyaar karle, Jhoota hi sahi... 🎶", 
    "🎶 Aadmi musafir hai aata hai jaata hai... Aate jaate raste me yade chhod jaata hai... 🎶", 
    "🎶 Main zindagi ka saath nibhata chala gaya... Har fikar ko dhuen mein udata chala gaya... Barbadiyon ka shauq manana fizul tha... Barbadiyon ka jashan manata chala gaya... 🎶", 
    "🎶 Khush rahe tu sada Yeh duwaa hai meri... Bewafa hi sahi Dilruba hai meri... 🎶", 
    "🎶 Aise khenche dil ke penche Gale hi pad gayi oye... Nashe si chadh gayi oye Kudi nashe si chad gayi... Patang si lad gayi oye.. Kudi patang si lad gayi... 🎶", 
)

@run_async
def abuse(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(ABUSE_STRINGS))
    else:
      message.reply_text(random.choice(ABUSE_STRINGS))

@run_async
def sing(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(SONG_STRINGS))
    else:
      message.reply_text(random.choice(SONG_STRINGS))

__help__ = """
- /abuse : Abuse someone in hindi.
- /sing : First lines of some random hindi Songs.
"""

__mod_name__ = "EXTRAS"

ABUSE_HANDLER = DisableAbleCommandHandler("abuse", abuse)
SING_HANDLER = DisableAbleCommandHandler("sing", sing)

dispatcher.add_handler(ABUSE_HANDLER)
dispatcher.add_handler(SING_HANDLER)
