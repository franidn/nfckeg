from main import Notification
import telepot

class TelegramNotification(Notification):

    def __init__(self):
        super(TelegramNotification, self).__init__()
        self.bot = telepot.Bot('536095288:AAFc4ojD_f4clr6tHXroO33E6qzB3FYM8AM')
        self.chat_id = "451372203"

    def notify(self, string):
        print("*****"+string+"*****")
        self.bot.sendMessage(self.chat_id, "NOT: "+string)

if __name__ == "__main__":
    message = TelegramNotification()
    while True:
        message.notify ("hola")
        time.sleep(1)
