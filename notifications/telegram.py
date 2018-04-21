#https://www.youtube.com/watch?v=GJDHTdVGtqo


from main import Notification
import telegram
import time

class TelegramNotification(Notification):

    def __init__(self):
        super(TelegramNotification, self).__init__()
        self.bot = telegram.Bot(self.token = "536095288:AAFc4ojD_f4clr6tHXroO33E6qzB3FYM8AM")
        self.bot.updater = Updater(self.bot.token)
        #self.chat_id = "451372203"

    def notify(self, update, pass_chat_data=True):
        #Agafa el chat_id del usuari que pregunta
        update.message.chat_id
        #Envia el missatge demanat a l'usuari
        self.bot.sendMessage(chat_id = update.message.chat_id, text="hola")

if __name__ == "__main__":
    message = TelegramNotification()
    while True:
        message.notify()
        time.sleep(1)
