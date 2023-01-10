# サンプルコード
import tkinter as tk
from tkinter import ttk

# 列の識別名を指定
column = ('日付', '預け額', '引き出し額', '利子', '合計', '名前')
# メインウィンドウの生成
root = tk.Tk()
root.title('Score List')
root.geometry('700x400')
# Treeviewの生成
tree = ttk.Treeview(root, columns=column)
# 列の設定
tree.column('#0',width=0, stretch='no')
tree.column('日付', anchor='center', width=80)
tree.column('預け額',anchor='center', width=130)
tree.column('引き出し額', anchor='center', width=130)
tree.column('利子', anchor='center', width=130)
tree.column('合計', anchor='center', width=130)
tree.column('名前', anchor='center', width=80)
# 列の見出し設定
tree.heading('#0',text='')
tree.heading('日付', text='日付',anchor='center')
tree.heading('預け額', text='預け額', anchor='w')
tree.heading('引き出し額',text='引き出し額', anchor='center')
tree.heading('利子',text='利子', anchor='center')
tree.heading('合計',text='合計', anchor='center')
tree.heading('名前',text='名前', anchor='center')
# レコードの追加
tree.insert(parent='', index='end', iid=0 ,values=(1, 'KAWASAKI',80, 8, 88, '長江'))
tree.insert(parent='', index='end', iid=1 ,values=(2,'SHIMIZU', 90, 9, 99, '長江'))
tree.insert(parent='', index='end', iid=2, values=(3,'TANAKA', 45, 4, '49', '長江'))
tree.insert(parent='', index='end', iid=3, values=(4,'OKABE', 60, 6, 66, '長江'))
tree.insert(parent='', index='end', iid=4, values=(5,'MIYAZAKI', 99, '9', 108, '長江'))
# ウィジェットの配置
tree.pack(pady=10)

root.mainloop()