import telebot
from telebot import types
admin='1620749704'
token='5675428066:AAFw4t8H-RNl-RsIqtX6BJ9IXlwKS85kX_I'
ID='5520660259'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
 
 ya =types.InlineKeyboardMarkup(row_width=1)
 gg=types.InlineKeyboardButton('استاذ أنور باشغيوان',callback_data='gg')
 uu=types.InlineKeyboardButton('استاذ بسّام الكثيري',callback_data='uu')
 mm=types.InlineKeyboardButton('استاذ عبدالله باسيف',callback_data='mm')

 ya.add(gg,uu,mm)
 bot.send_message(message.chat.id,"مرحبا بك عزيزي الطالب في بوت رأيكم يهمنا 👋🏻"



"قم باختيار المعلم الذي تريد ايصال الرساله السرية اليه 👇🏻",reply_markup=ya)
@bot.callback_query_handler(func=lambda call:True)
def yahy(call):
 message=call.data
 if message=='gg':
  
  bot.send_message(call.message.chat.id,'ارسل الان الرسالة')
  @bot.message_handler(content_types=['text'])
  def hh(call):
   msg1 = (call.text)
   bot.send_message(admin,msg1)
   bot.send_message(call.chat.id,'تم استلام رسالتك شكرا لك على تعاونك ♥')
   
   
 if message=='uu':
  
  bot.send_message(call.message.chat.id,'ارسل الان الرسالة')
  @bot.message_handler(content_types=['text'])
  def hh(call):
   msg2 = (call.text)
   bot.send_message(ID,msg2)
   bot.send_message(call.chat.id,'تم استلام رسالتك شكرا لك على تعاونك ♥')


 if message=='mm':
  
  bot.send_message(call.message.chat.id,'ارسل الان الرسالة')
  @bot.message_handler(content_types=['text'])
  def hh(call):
   msg3 = (call.text)
   bot.send_message(admin,msg3)
   bot.send_message(call.chat.id,'تم استلام رسالتك شكرا لك على تعاونك ♥')

bot.infinity_polling(True)
