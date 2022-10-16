import telebot
from telebot import types
admin='1620749704'
token='5701926726:AAFFlP7Us_BywcUvm0fuCNQHY4J8OiM8WGU'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
	
	ya =types.InlineKeyboardMarkup()
	gg=types.InlineKeyboardButton('صف الاول',callback_data='gg')
	uu=types.InlineKeyboardButton('الصف الثاني',callback_data='uu')
	mm=types.InlineKeyboardButton('الصف الثالث',callback_data='mm')

	ya.add(gg,uu,mm)
	bot.send_message(message.chat.id,'اهلا بك في البوت',reply_markup=ya)
@bot.callback_query_handler(func=lambda call:True)
def yahy(call):
	message=call.data
	if message=='gg':
		ga=types.InlineKeyboardMarkup()
		b=types.InlineKeyboardButton('استاذ احمد',callback_data='b')
		c=types.InlineKeyboardButton('استاذ محمد',callback_data='c')
		ga.add(b,c)
		bot.send_message(call.message.chat.id,'اختر',reply_markup=ga)
	if message=='b':
		bot.send_message(call.message.chat.id,'ارسل الان الرسالة')
		@bot.message_handler(content_types=['text'])
		def hh(call):
			bot.forward_message(admin,call.chat.id,call.id)
			bot.send_message(call.chat.id,'تم ارسال الرسالة انتظر الرد')
	
	if message=='c':
		bot.send_message(call.message.chat.id,'ارسل الان الرسالة')
		@bot.message_handler(content_types=['text'])
		def hh(call):
			bot.forward_message(admin,call.chat.id,call.id)
			bot.send_message(call.chat.id,'تم ارسال الرسالة انتظر الرد')
		
		
		
	
	if message=='uu':
		l=types.InlineKeyboardMarkup()
		v=types.InlineKeyboardButton('استاذ عبد الكريم',callback_data='v')
		m=types.InlineKeyboardButton('احمد محمد',callback_data='m')
		l.add(v,m)
		bot.send_message(call.message.chat.id,'اختر',reply_markup=l)
	if message=='v':
		bot.send_message(call.message.chat.id,'ارسل الان الرسالة')
		@bot.message_handler(content_types=['text'])
		def hh(call):
			bot.forward_message(admin,call.chat.id,call.id)
			bot.send_message(call.chat.id,'تم ارسال الرسالة انتظر الرد')
		if message=='m':
			bot.send_message(call.message.chat.id,"ارسل الان الرسالة")
			@bot.message_handler(content_types=['text'])
			def hh(call):
				bot.forward_message(admin,call.chat.id,call.id)
				bot.send_message(call.chat.id,'تم ارسال الرسالة انتظر الرد')
	if message=='mm':
		h=types.InlineKeyboardMarkup()
		z=types.InlineKeyboardButton('استاذ شاكر',callback_data='z')
		s=types.InlineKeyboardButton('استاذ علي',callback_data='s')
		h.add(z,s)
		bot.send_message(call.message.chat.id,'اختر',reply_markup=h)
	if message=='z':
		bot.send_message(call.message.chat.id,'ارسل الان الرسالة')
		@bot.message_handler(content_types=['text'])
		def hh(call):
			bot.forward_message(admin,call.chat.id,call.id)
			bot.send_message(call.chat.id,'تم ارسال الرسالة انتظر الرد')
			
	if message=='s':
		bot.send_message(call.message.chat.id,'ارسل الان الرسالة')
		@bot.message_handler(content_types=['text'])
		def hh(call):
			bot.forward_message(admin,call.chat.id,call.id)
			bot.send_message(call.chat.id,'تم ارسال الرسالة انتظر الرد')

		

	

bot.infinity_polling(True)