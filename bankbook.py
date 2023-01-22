import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import get_data
import put_data
import datetime

# サイン項目が選択された時


def sign_entry(event):
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
        date = datetime.datetime.fromtimestamp(
            trade_list[i].get('date').timestamp()).date()
        date = str(date).split('-')
        date = date[0]+'年'+date[1]+'月'+date[2]+'日'
        print(date)
        date_text = ttk.Label(trading_history_frame,
                              text=date, width=12, padding=[30, 5, 0, 5])
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
        # TODO sign.bind('<Button-1>', sign_entry)
        sign_text.grid(row=i+1, column=5)

    # 実行ボタン

    def execute():
        # これまでの入力をリストに入れる
        table_data = []
        for i in range(0, n):
            table_data.append([dates[i].get(),
                               deposits[i].get(),
                               withdraws[i].get(),
                               interests[i].get(),
                               totals[i].get(),
                               signs[i].get()
                               ])
        # pandas dataframeに変換
        df = pd.DataFrame(table_data, columns=[
                          '日付', '預ける', '引き出す', '利子', '合計', 'サイン',])

        # 結果表示
        output(df)

    button = ttk.Button(root,
                        text='保存',
                        padding=5,
                        command=execute)
    button.grid(row=1, column=0)
    root.mainloop()


def output(df):
    root = tk.Tk()
    root.title('保存内容')

    trading_history_frame = ttk.Frame(root, padding=5)
    trading_history_frame.grid(row=0, column=0)

    # ツリービューの作成
    tree = ttk.Treeview(trading_history_frame)

    # 列インデックスの作成
    tree['columns'] = (0, 1, 2, 3, 4, 5)
    # 表スタイルの設定(headingsは通常の表形式)
    tree['show'] = 'headings'
    # 各列の設定(インデックス,オプション(今回は幅を指定))
    for i in range(0, 6):
        tree.column(i, width=100)

    # 各列のヘッダー設定(インデックス,テキスト)
    tree.heading(0, text='日付')
    tree.heading(1, text='預ける')
    tree.heading(2, text='引き出す')
    tree.heading(3, text='利子')
    tree.heading(4, text='合計')
    tree.heading(5, text='サイン')

    for i in range(0, len(df)):
        date = df.iloc[i][0]
        deposit = df.iloc[i][1]
        withdraw = df.iloc[i][2]
        interest = df.iloc[i][3]
        total = df.iloc[i][4]
        sign = df.iloc[i][5]

        # レコードの作成
        # 1番目の引数-配置場所（表形式の表示ではブランクとする）
        # 2番目の引数-end:表の配置順序を最下部に配置
        # (行インデックス番号を指定することもできる)
        # 3番目の引数-values:レコードの値をタプルで指定する
        tree.insert('', 'end', values=(
            date, deposit, withdraw, interest, total, sign))

    # ツリービューの配置
    tree.grid(row=0)

    # 　保存ボタン
    def save():
        fld = tk.filedialog.askdirectory(initialdir='C:')
        df.to_csv(fld + '/table.csv', encoding='shift-jis', index=False)

    button = ttk.Button(root,
                        text='保存',
                        command=save)
    button.grid(row=2, pady=5)

    root.mainloop()


if __name__ == '__main__':
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
                            bg='#ffffff', command=trading_history)
    next_button.pack()

    root.mainloop()
