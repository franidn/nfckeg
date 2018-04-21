from main import Notification
import telepot

class TelegramNotification(Notification):

    def __init__(self):
        super(TelegramNotification, self).__init__()
        self.bot = telepot.Bot('533989140:AAHAPIwVo_qGirPSU2SSUDyiFw4F5Gw9DUs')
        self.chat_id = "365077439"

    def notify(self, string):
        print("*****"+string+"*****")
        bot.sendMessage(self.chat_id, "NOT: "+string)
