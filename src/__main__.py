import datetime
from tkinter import *

from mylib.Common import GetData, DrawPlot, DrawCandle, data

def click_btn_2a():
    button_2a['text'] = 'clicked'

def selected():
    indices = lst_b.curselection()
    selections = '\n'.join([lst_b.get(i) for i in indices])
    sel_v.set(f'{selections}')


if __name__ == '__main__':

    root = Tk()  

    # ----------- Create Window ----------- #
    root.title('PyStockChart')   # Title
    root.geometry('1200x750')        # size

    # ----------- Set Frame ----------- #
    frame1 = Frame(root, width=350, height=250)  # Label
    frame2 = Frame(root, width=350, height=250)  # Button, Entry
    frame3 = Frame(root, width=350, height=250)  # chart
    frame4 = Frame(root, width=350, height=250)  # RadioButton
    frame5 = Frame(root, width=350, height=250)  # Spinbox
    frame6 = Frame(root, width=350, height=250)  # Listbox
    frame7 = Frame(root, width=350, height=250)  # Canvas
    frame8 = Frame(root, width=350, height=250)  # Canvas button
    frame9 = Frame(root, width=350, height=250)  # Photoimage
    
    # Frame size fix
    frame1.propagate(False)
    frame2.propagate(False)
    frame6.propagate(False)
    frame7.propagate(False)
    frame8.propagate(False)
    frame9.propagate(False)

    # Frame grid
    frame1.grid(row=0, column=0)
    frame2.grid(row=0, column=1)
    frame3.grid(row=0, column=2)
    frame4.grid(row=1, column=0)
    frame5.grid(row=1, column=1)
    frame6.grid(row=1, column=2)
    frame7.grid(row=2, column=0)
    frame8.grid(row=2, column=1)
    frame9.grid(row=2, column=2)


    # ---------- Widget allocation  ----------- #
    # == label(Frame1) == # 
    dt = datetime.datetime.now()
    label_1a = Label(frame1, text=dt.strftime('%A, %B %d, %Y'), font=('', 14), bg='#ccccff', fg='#ff0000')
    label_1a.pack(padx=5, pady=10)

    # == Entry(Frame2) & Show charts == # 
    entry_2b = Entry(frame2, width=14)
    text = StringVar()
    button_2b = Button(frame2, text='Put Ticker',
                command=lambda: [text.set(entry_2b.get()), 
                                 GetData(text.get(), data), 
                                 DrawCandle(data, frame4),
                                 DrawPlot(data, frame3)
                                 ])
    label_2b = Label(frame2, textvariable=text, font=('System', 14))
    entry_2b.pack()
    button_2b.pack()
    label_2b.pack()

    root.mainloop()