#coding utf-8
import os,sys
import tkinter
from tkinter import ttk 
from tkinter import filedialog
from tkinter import messagebox
import img_modification

def ask_input():
    #参照ボタン
    path = filedialog.askdirectory()
    input_path.set(path)

def ask_output():
    #参照ボタン
    paths = filedialog.askdirectory()
    output_path.set(paths)


def app():
    #縮小実行ボタンの動作
    input_dir = input_path.get()
    output_dir = output_path.get()
    mag_val = int(EditBox.get())
    img_modification.shrink(mag_val, input_dir, output_dir)
    messagebox.showinfo("完了", "完了しました。")


if __name__ == '__main__':
    main_win = tkinter.Tk()
    main_win.title('File shrink') 

    main_frm = ttk.Frame(main_win)
    main_frm.grid(column=0, row=0, sticky=tkinter.NSEW, padx=5, pady=10)

    
    input_label = ttk.Label(main_frm, text="input>>")
    input_path = tkinter.StringVar()
    input_box = ttk.Entry(main_frm, width = 30, textvariable=input_path)
    input_btn = ttk.Button(main_frm, text="参照", command=ask_input)

    input_label.grid(column=0, row=0, pady=10)
    input_box.grid(column=1, row=0, sticky=tkinter.EW, padx=5)
    input_btn.grid(column=2, row=0)

    #output
    output_label = ttk.Label(main_frm, text="output>>")
    output_path = tkinter.StringVar()
    output_box = ttk.Entry(main_frm, width = 30, textvariable=output_path)
    output_btn = ttk.Button(main_frm, text="参照", command=ask_output)

    output_label.grid(column=0, row=1, pady=10)
    output_box.grid(column=1, row=1, sticky=tkinter.EW, padx=5)
    output_btn.grid(column=2, row=1)

    #magnification value
    EditBox_label = ttk.Label(main_frm, text="縮小倍率")
    EditBox = ttk.Entry(main_frm, width=5)

    EditBox_label.grid(column=0, row=2)
    EditBox.grid(column=1, row=2, sticky=tkinter.EW, padx=5)

    #shrink
    app_btn = ttk.Button(main_frm, text="実行", command=app)
    app_btn.grid(column=1, row=3)

    #row.columnconfigure(0, weight=1)
    #row.rowconfigure(0, weight=1)
    #row.columnconfigure(1, weight=1)

    main_win.columnconfigure(0, weight=1)
    main_win.rowconfigure(0, weight=1)
    main_frm.columnconfigure(1, weight=1)
    
    main_win.mainloop()

