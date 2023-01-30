import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import get_data
import put_data
import firebase_admin
from firebase_admin import credentials


def sign_entry_check(event):
    print('サイン入力欄が選択された')

    # パスワード入力画面を表示させる
    root = tk.Tk()
    root.title('パスワード入力')
    root.geometry('380x200')
    password_label = tk.Label(root, text='パスワード：')
    password_label.place(x=50, y=80)
    password_input_field = tk.Entry(root)
    password_input_field.place(x=140, y=80)
    password_input_field.bind()

    def check_password():
        password = 'lOBo1999'
        input_value = password_input_field.get()
        print('パスワードチェック: ', input_value)
        if password == input_value:
            tk.messagebox.showinfo('メッセージ', '認証完了')
            root.destroy()
        else:
            tk.messagebox.showwarning('エラー', '誤ったパスワードです')

    button = tk.Button(root, text='送信', command=check_password)
    button.place(x=160, y=150)


def trading_history():

    frame.destroy()
    trading_history_frame = ttk.Frame(root)
    trading_history_frame.grid(row=0, column=0)

    get_data_list = get_data.get_data()
    trade_list = []
    for doc in get_data_list:
        trade_list.append(doc.to_dict())

    # 項目をつくる
    items = ['日付', '預ける', '引き出す', '利子', '合計', 'サイン']
    for i in range(0, len(items)):
        label_item = ttk.Label(trading_history_frame,
                               text=items[i], anchor=tk.CENTER)
        label_item.grid(row=0, column=i)

    n = len(trade_list)

    for i in range(0, n):
        date = trade_list[i].get('date')
        date_text = ttk.Label(trading_history_frame, text=date, width=12, anchor=tk.CENTER)
        date_text.grid(row=i+1, column=0)

    # 預ける項目
    for i in range(0, n):
        deposit = trade_list[i].get('deposit')
        deposit_text = ttk.Label(
            trading_history_frame, text=deposit, width=12, anchor=tk.CENTER)
        deposit_text.grid(row=i+1, column=1)

    # 引き出す項目
    for i in range(0, n):
        withdraw = trade_list[i].get('withdraw')
        withdraw_text = ttk.Label(
            trading_history_frame, text=withdraw, width=12, anchor=tk.CENTER)
        withdraw_text.grid(row=i+1, column=2)

    # 利子項目
    for i in range(0, n):
        interest = trade_list[i].get('interest')
        interest_text = ttk.Label(
            trading_history_frame, text=interest, width=12, anchor=tk.CENTER)
        interest_text.grid(row=i+1, column=3)

    # 合計項目

    for i in range(0, n):
        total = trade_list[i].get('total')
        total_text = ttk.Label(trading_history_frame,
                               text=total, width=12, anchor=tk.CENTER)
        total_text.grid(row=i+1, column=4)

    # サイン項目
    for i in range(0, n):
        sign = trade_list[i].get('sign')
        sign_text = ttk.Label(trading_history_frame,
                              text=sign, width=12, anchor=tk.CENTER)
        # TODO sign.bind('<Button-1>', sign_entry_check)
        sign_text.grid(row=i+1, column=5)

    button = ttk.Button(root,
                        text='入力',
                        padding=5,
                        command=put_data_entry)
    button.grid(row=1, column=0)
    root.mainloop()


def put_data_entry():
    root = tk.Tk()
    root.title('保存内容')
    root.geometry('625x150')
    items = ['日付', '預ける', '引き出す', '利子', '合計', 'サイン']
    for i in range(0, len(items)):
        label_item = ttk.Label(root,
                               text=items[i])
        label_item.grid(row=0, column=i)

    datetime_entry = ttk.Entry(root, width=10)
    datetime_entry.grid(row=1, column=0)
    deposit_entry = ttk.Entry(root, width=10)
    deposit_entry.grid(row=1, column=1)
    withdraw_entry = ttk.Entry(root, width=10)
    withdraw_entry.grid(row=1, column=2)
    interest_entry = ttk.Entry(root, width=10)
    interest_entry.grid(row=1, column=3)
    total_entry = ttk.Entry(root, width=10)
    total_entry.grid(row=1, column=4)
    sign_entry = ttk.Entry(root, width=10)
    sign_entry.bind('<ButtonPress>', sign_entry_check)
    sign_entry.grid(row=1, column=5)

    button = ttk.Button(root,
                        text='入力',
                        command= lambda : put_data.put_data(datetime_entry.get(), deposit_entry.get(), withdraw_entry.get(), interest_entry.get(), total_entry.get(), sign_entry.get()))
    button.place(x=265, y=100)

    root.mainloop()

if __name__ == '__main__':
    cred = credentials.Certificate("./dan-bankbook-firebase-adminsdk-hjd6u-8c0fe69935.json")
    firebase_admin.initialize_app(cred)
    
    root = tk.Tk()
    root.title('ダン通帳')
    root.geometry('700x482')
    frame = ttk.Frame(root)
    frame.pack(fill=tk.BOTH)
    canvas = tk.Canvas(frame, width=700, height=450)
    canvas.pack()
    back_image = tk.PhotoImage(file='back_image.png', width=700, height=450)
    canvas.create_image(0, 0, image=back_image, anchor=tk.NW)
    next_button = tk.Button(frame, text='取引ページへ',
                            bg='#ffffff', command=trading_history())
    next_button.pack()

    root.mainloop()
