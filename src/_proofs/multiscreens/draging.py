# https://stackoverflow.com/questions/45183914/tkinter-detecting-a-window-drag-event
import tkinter as tk

# root = tk.Tk()

# drag_id = ''


class Dragger:
    def __init__(self):
        self.drag_id = ''
        self.root = tk.Tk()

    def dragging(self, event):
        # global drag_id
        if event.widget is self.root:  # do nothing if the event is triggered by one of root's children
            if self.drag_id == '':
                # action on drag start
                print('start drag')
            else:
                # cancel scheduled call to stop_drag
                self.root.after_cancel(self.drag_id)
                print('dragging')
            # schedule stop_drag
            self.drag_id = self.root.after(100, self.stop_drag)

    def stop_drag(self):
        # global drag_id
        print('stop drag')
        # reset d0rag_id to be able to detect the start of next dragging
        self.drag_id = ''

    def start(self):
        self.root.bind('<Configure>', self.dragging)
        self.root.mainloop()


# root.bind('<Configure>', dragging)
# root.mainloop()

app = Dragger()
app.start()
