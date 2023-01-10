# サンプルコード
import tkinter as tk
from tkinter import ttk

def up_price():
    selected = tree.focus()
    temp = tree.item(selected, 'values')
    sal_up = float(temp[2]) + float(temp[2]) * 0.1
    tree.item(selected, values=(temp[0], temp[1], sal_up))

# メインウィンドウの生成
root = tk.Tk()
root.title("レコード値の変更")
# Treeviewの生成
tree = ttk.Treeview(root, columns=(1, 2, 3), show='headings', height=8)
# 列の見出し設定
tree.heading(1, text="id")
tree.heading(2, text="vegetable")
tree.heading(3, text="price")
# レコードの追加
tree.insert(parent='', index=0, iid=0, values=(1, "onion", 30.00))
tree.insert(parent='', index=1, iid=1, values=(2, "cabbage", 150.00))
tree.insert(parent='', index=2, iid=2, values=(3, "carrot", 80.00))
tree.insert(parent='', index=3, iid=3, values=(4, "eggplant", 100.00))
# Buttonの生成
button = tk.Button(root, text='Increment Price', command=up_price)
# Styleの設定
style = ttk.Style()
style.theme_use("default")
style.map("Treeview")
# ウィジェットの配置
tree.pack()
button.pack()

root.mainloop()