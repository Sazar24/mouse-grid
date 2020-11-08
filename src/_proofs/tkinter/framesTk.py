# source: https://www.youtube.com/watch?v=D8-snVfekto
import tkinter as tk

HEIGHT = 700
WIDTH = 800

root = tk.Tk()

# canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
# canvas.pack()

# frame = tk.Frame(root, bg='blue', bd='12', highlightbackground='green', borderwidth=16)
# # widget.config(highlightbackground=COLOR)
# frame.config(highlightbackground='black')
# frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
frame1 = tk.Frame(root, bg='green', highlightbackground='green', borderwidth=16)
frame2 = tk.Frame(root, bg='blue', highlightbackground='blue', borderwidth=5)
frame3 = tk.Frame(root, bg='blue', highlightbackground='blue', borderwidth=5)
frame1.grid(column=0, row=0, sticky='nesw')
frame2.grid(column=1, row=1, sticky='nesw')
frame3.grid(column=2, row=2, sticky='nesw')

button1 = tk.Button(frame1, text='Test button', bg='gray', fg='red')
button1.pack()
button2 = tk.Button(frame2, text='Test button', bg='gray', fg='red')
button2.pack()

root.mainloop()
