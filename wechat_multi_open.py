# -*- coding: utf-8 -*-
#Created on Fri May  3 17:59:57 2025
#微信多开助手 v1.0
#@Author: simon
#@Email: scoln@foxmail.com
#@Date: 2025-05-10
#@Version: 1.0.0
#@License: MIT License
#@Copyright: Copyright (c) 2025 simon


import tkinter as tk
from tkinter import filedialog
import os

def find_wechat_path():
    # 常见微信安装路径
    possible_paths = [
        "C:\\Program Files (x86)\\Tencent\\WeChat\\WeChat.exe",
        "C:\\Program Files\\Tencent\\WeChat\\WeChat.exe",
        os.path.expanduser("~\\AppData\\Local\\Tencent\\WeChat\\WeChat.exe"),
        "D:\\Program Files (x86)\\Tencent\\WeChat\\WeChat.exe",
        "D:\\Program Files\\Tencent\\WeChat\\WeChat.exe"
    ]
    
    # 检查路径是否存在
    for path in possible_paths:
        if os.path.exists(path):
            return path
    
    # 如果都找不到，让用户选择
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askopenfilename(
        title="请选择微信安装路径",
        filetypes=[("微信程序", "WeChat.exe")]
    )
    return path

def open_wechat(count):
    wechat_path = find_wechat_path()
    if not wechat_path:
        tk.messagebox.showerror("错误", "未找到微信程序路径")
        return
    
    for _ in range(count):
        os.startfile(wechat_path)

def main():
    root = tk.Tk()
    root.title("125微信多开工具")
    
    # 标题
    title_label = tk.Label(root, text="选择微信启动次数：", font=("Arial", 12))
    title_label.grid(row=0, column=0, columnspan=4, pady=10)
    
    # 双开按钮
    double_btn = tk.Button(root, text="双开", command=lambda: open_wechat(2))
    double_btn.grid(row=1, column=0, padx=5)
    
    # 三开按钮
    triple_btn = tk.Button(root, text="三开", command=lambda: open_wechat(3))
    triple_btn.grid(row=1, column=1, padx=5)
    
    # 输入框
    entry = tk.Entry(root, width=5)
    entry.grid(row=1, column=2, padx=5)
    
    # 确认按钮
    confirm_btn = tk.Button(root, text="确认", command=lambda: open_wechat(int(entry.get())))
    confirm_btn.grid(row=1, column=3, padx=5)
    
    # 注意事项
    note_label = tk.Label(root, text="注意：请在多开前关闭已运行的微信程序。", fg="red")
    note_label.grid(row=2, column=0, columnspan=4, pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main()