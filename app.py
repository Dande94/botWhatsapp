#1. Importar as bibliotecas necessárias
import pywhatkit
import keyboard
import time
from datetime import datetime
#2. definir quais contatos iremos enviar as mensagens
contatos = ['+5547999999999','+5547999999999']
#3. Definir intervalo de envio
while len(contatos) >= 1:
    #enviar mensagens
    pywhatkit.sendwhatmsg(contatos[0],'Teste do bot para whatsapp!' , datetime.now().hour,datetime.now().minute +2)
    del contatos[0]
    time.sleep(60)
    keyboard.press_and_release('ctrl + w')
#4. Testar