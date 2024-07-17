import telebot
# import pyodbc
from flask import Flask, request
from telebot import types


# Reemplaza 'YOUR_TOKEN' con el token que obtuviste de BotFather

TOKEN = '6658284964:AAFB4OJO8xBUZhw70H-AqCzHG-I5rPKTiIU'


bot = telebot.TeleBot(TOKEN)

# Crear una aplicación Flask para el webhook
app = Flask(__name__)
# Manejar el comando '/start'###########################################

@bot.message_handler(commands=['start'])
def send_welcome(message):
  bot.send_message(message.chat.id, "¡Hola! Soy Boty Asistente de la empresa Milmat technologi")
  bot.send_message(message.chat.id, "Elige una opcion:\n1) Si quieres suscribirte a un grupo utiliza el comando: /grupos\n2) Si eres socio y quieres modificar algo utiliza el comando: /socios\n3) Si quieres quieres ser socio utiliza el comando: /registroSocio", parse_mode='HTML')

###########################



@bot.message_handler(commands=['btn'])
def send_btn(message):
    markup = types.InlineKeyboardMarkup()
    itembtn1 = types.InlineKeyboardButton('Equipo 1', callback_data='equipo1')
    itembtn2 = types.InlineKeyboardButton('Equipo 2', callback_data='equipo2')
    markup.add(itembtn1, itembtn2)
    bot.send_message(message.chat.id, "¿Quién crees que ganará?", reply_markup=markup)


# SIEMPRE SE EJECUTA PERO CUANDO PRESIONAN LOS BOTONES DE INLINEKEYBOARDBUTTON()
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'equipo1':
         # bot.send_message(call.message.chat.id, "Has presionado el Botón 1. Realizando acción específica...")
        accion_btn_equipos(call)
    elif call.data == 'equipo2':
        accion_btn_equipos(call)
    elif call.data == 'yape':
        # Acción específica para el boton de yape
        bot.send_message(call.message.chat.id, "ELEGISTE Yape")
    elif call.data == 'bebacoin':
        # Acción específica para el boton de BEBACOIN
        bot.send_message(call.message.chat.id, "Elegiste un bebacoin")

def accion_btn_equipos(call):
    # print("Acción del Botón 1 ejecutada")
    markup = types.InlineKeyboardMarkup()
    itembtn1 = types.InlineKeyboardButton('Yape', callback_data='yape')
    itembtn2 = types.InlineKeyboardButton('bebacoin', callback_data='bebacoin')
    markup.add(itembtn1, itembtn2)
    bot.send_message(call.message.chat.id, f"Apoya a  { call.data }", reply_markup=markup)





# Manejar los mensajes de texto generaal ####################################################

@bot.message_handler(func=lambda message: True)
def echo_message(message):
  bot.reply_to(message, f"Eh recibido <b>{message.text}</b>", parse_mode = "HTML")
###############################################################################################



# Configurar la ruta del webhook
@app.route(f'/{TOKEN}', methods=['POST'])

def webhook():

  update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))

  bot.process_new_updates([update])

  return "OK"



# Establecer el webhook utilizando serveo de ubuntu/linux

def set_webhook_serveo():

  #serveo_url = "https://e1ebf9db18a5859c29fe6b642aa7b167.serveo.net"

  localtunnel_url = "https://yummy-cities-exist.loca.lt" #SERVIDOR LOCAL con localtunnel de node 

  bot.remove_webhook()

  bot.set_webhook(url=f'{localtunnel_url}/{TOKEN}')

  print(f"Webhook URL: {localtunnel_url}/{TOKEN}")


# Iniciar la aplicación Flask y el bot

if __name__ == "__main__":

  set_webhook_serveo()

  app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))

