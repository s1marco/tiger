from datetime import datetime
import random
import telebot
import time
from pytz import timezone
import os
from dotenv import load_dotenv

load_dotenv()  # carregar as variáveis do .env

api_key = os.getenv('BOT_TOKEN')
chat_id = int(os.getenv('CHAT_ID'))
LINK_SITE = 'https://lf-egito.com/?id=526959639'

bot = telebot.TeleBot(api_key)



while True:
    try:
        tz = timezone('America/Sao_Paulo')
        now = datetime.now(tz)
        h = now.hour
        m = now.minute
        s = now.second

        print(f'{h:02d}:{m:02d}:{s:02d}')

        numero_aleatorio1 = random.randint(1, 10)
        numero_aleatorio2 = random.randint(1, 10)

        # Envie a foto (coloque BOT_TIGER.jpg na mesma pasta do script)
        with open('BOT_TIGER.jpeg', 'rb') as photo:
            bot.send_photo(
                chat_id=chat_id,
                photo=photo,
                caption=f'''
⚠️SINAL ENTREGUE⚠️ 

🔥 QUENTE: {numero_aleatorio1} X NORMAL

🔥 QUENTE: {numero_aleatorio2} X TURBO

⏰VÁLIDO POR 4 MIN⏰

{LINK_SITE}
''',
                parse_mode='MARKDOWN'
            )

        time.sleep(240)  # espera 4 minutos

        bot.send_message(
            chat_id=chat_id,
            text='''💰 tempo encerrado 💰 
procurando novo sinal...
''',
            parse_mode='MARKDOWN',
            disable_web_page_preview=True
        )

        time.sleep(60)  # espera 1 minuto antes de repetir

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        time.sleep(10)  # espera 10 segundos antes de tentar novamente
