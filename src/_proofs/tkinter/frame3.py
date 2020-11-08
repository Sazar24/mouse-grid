# http://effbot.org/tkinterbook/frame.htm
from tkinter import *

master = Tk()

Label(text="one").pack()

# RAISED='raised'
# SUNKEN='sunken'
# FLAT='flat'
# RIDGE='ridge'
# GROOVE='groove'
# SOLID = 'solid'
params = {'height': 12, 'bd': 1, 'relief': 'solid', 'width': 50, 'height': 50, 'cursor': 'iron_cross'}
RIDGE
separator = Frame(**params)
separator2 = Frame(**params)
separator3 = Frame(**params)
# separator.pack(fill=X, padx=5, pady=5)
# separator.grid(column=0, row=0)
# separator2.grid(column=1, row=1)
# separator3.grid(column=2, row=2)

# LEFT='left'
# TOP='top'
# RIGHT='right'
# BOTTOM='bottom'
separator.pack(fill='x', side='top')
separator2.pack(fill='x', side='left')
separator3.pack(fill='x', side='left')
Label(text="two").pack()

mainloop()
