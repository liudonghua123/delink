#!/usr/bin/python3

import tkinter as tk
from tkinter import X, YES, END, TOP, LEFT, RIGHT

from core import transcode

class App(tk.Frame):
    fields = '真实地址', '迅雷下载', '网际快车', 'QQ旋风'

    def __init__(self, master):
        tk.Frame.__init__(self, master, height=60, width=80)
        self.master.bind('<Return>', (lambda _, e=None: self.query()))
        self.entries = self.makeform(App.fields)
        self.querybutton = tk.Button(self.master, text='转换', command=self.query)
        self.querybutton.pack(side=LEFT, padx=5, pady=5)
        self.clearbutton = tk.Button(self.master, text='清空', command=self.clear)
        self.clearbutton.pack(side=LEFT, padx=5, pady=5)

    def query(self):
        def set_text(field, text):
            field.delete(0, END)
            field.insert(0, text)

        for ent in self.entries:
            text = ent.get()
            if len(text) > 0:
                for f, t in zip(self.entries, transcode(text)):
                    set_text(f, t)
                break

    def clear(self):
        for ent in self.entries:
            ent.delete(0, END)

    def makeform(self, fields):
        entries = []
        for field in fields:
            row = tk.Frame(self.master)
            lab = tk.Label(row, width=6, text=field, anchor='w')
            ent = tk.Entry(row)
            row.pack(side=TOP, fill=X, padx=5, pady=5)
            lab.pack(side=LEFT)
            ent.pack(side=RIGHT, expand=YES, fill=X)
            entries.append(ent)
        return entries

def main():
    root = tk.Tk()
    root.minsize(500, 200)
    root.title('Delink')
    App(root).pack(expand=True, fill='both')
    root.mainloop()

if __name__ == '__main__':
    main()
