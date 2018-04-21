from main import Notification
import time

class MockNotification(Notification):

        def __init__(self):
            super(MockNotification, self).__init__()

        def notify(self, string):
            print("*****"+string+"*****")

if __name__ == "__main__":
    message = MockNotification()
    while True:
        message.notify ("hola")
        time.sleep(1)
