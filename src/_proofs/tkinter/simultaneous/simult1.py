# https://stackoverflow.com/questions/459083/how-do-you-run-your-own-code-alongside-tkinters-event-loop
import tkinter as tk
import threading
from time import sleep


class App(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.root.quit()

    def run(self):
        self.root = tk.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.callback)

        label = tk.Label(self.root, text="Hello World")
        label.pack()

        self.root.mainloop()


app = App()
print('Now we can continue running code while mainloop runs!')

for i in range(20):
    sleep(1)
    print(i)
