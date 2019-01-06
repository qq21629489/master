import tkinter as tk
import tkinter.messagebox
import window_login
import fuction

   
def start_window_main():
    
    # 主視窗-登入鈕事件
    def user_login():
        # 取得使用者資料
        user_data = fuction.read_data()
        
        if var_account.get() == "":
            pass
        elif var_account.get() not in user_data:
            tkinter.messagebox.showerror("錯誤", "帳號不存在！")
        elif var_password.get() != user_data[var_account.get()][0]:
            tkinter.messagebox.showerror("錯誤", "密碼錯誤！")
        else:
            tkinter.messagebox.showinfo("歡迎", "登入成功！")
            window_main.destroy()
            window_login.start_window_login(var_account.get())
            
    # 主視窗-註冊鈕事件
    def user_register():
    
        def confirm_register():
            user_data = fuction.read_data()
            
            if var_new_account.get() in user_data:
                tkinter.messagebox.showerror("錯誤", "帳號已存在！")
            elif var_new_password.get() == "" or var_new_name.get() == "" or var_new_age.get() == "" or var_new_phone.get() == "" or var_new_resume.get() == "":
                tkinter,tkinter.messagebox.showerror("錯誤", "尚有資料未填寫！")
            else:
                tmp_list = [var_new_password.get(), var_new_name.get(), var_new_age.get(), var_new_phone.get(), var_new_resume.get(), [], []]
                user_data[var_new_account.get()] = tmp_list
            
                with open("user_data.txt", "w", encoding="UTF-8-sig") as f:
                    f.write(str(user_data))
        
                tkinter.messagebox.showinfo("恭喜", "註冊成功！")
                window_register.grab_release()
                window_register.destroy()
        
        # # 註冊視窗基本設定
        window_register = tk.Toplevel(window_main)
        window_register.title("註冊")
        window_register.geometry("400x700")
        window_register.resizable(width=False, height=False)
        window_register.grab_set()
        
        # 註冊視窗-帳號
        var_new_account = tk.StringVar()
        var_new_account.set("example@mail")
        
        lab_account_reg = tk.Label(window_register, text="帳號：", font=("Arial", 16), width=10, height=1, anchor="e")
        lab_account_reg.place(height=50, width=120, x=10, y=30)
        
        entry_account_reg = tk.Entry(window_register, font=("Arial", 12), width=10, textvariable=var_new_account)
        entry_account_reg.place(height=30, width=200, x=130, y=40)
        
        # 註冊視窗-密碼
        var_new_password = tk.StringVar()
        
        lab_password_reg = tk.Label(window_register, text="密碼：", font=("Arial", 16), width=10, height=1, anchor="e")
        lab_password_reg.place(height=50, width=120, x=10, y=80)
        
        entry_password_reg = tk.Entry(window_register, font=("Arial", 12), width=10, textvariable=var_new_password)
        entry_password_reg.place(height=30, width=200, x=130, y=90)
        
        # 註冊視窗-姓名
        var_new_name = tk.StringVar()
        
        lab_name_reg = tk.Label(window_register, text="姓名：", font=("Arial", 16), width=10, height=1, anchor="e")
        lab_name_reg.place(height=50, width=120, x=10, y=130)
        
        entry_name_reg = tk.Entry(window_register, font=("Arial", 12), width=10, textvariable=var_new_name)
        entry_name_reg.place(height=30, width=200, x=130, y=140)
        
        # 註冊視窗-年齡
        var_new_age = tk.StringVar()
        
        lab_age_reg = tk.Label(window_register, text="年齡：", font=("Arial", 16), width=10, height=1, anchor="e")
        lab_age_reg.place(height=50, width=120, x=10, y=180)
        
        entry_age_reg = tk.Entry(window_register, font=("Arial", 12), width=10, textvariable=var_new_age)
        entry_age_reg.place(height=30, width=200, x=130, y=190)
        
        # 註冊視窗-電話
        var_new_phone = tk.StringVar()
        
        lab_phone_reg = tk.Label(window_register, text="電話：", font=("Arial", 16), width=10, height=1, anchor="e")
        lab_phone_reg.place(height=50, width=120, x=10, y=230)
        
        entry_phone_reg = tk.Entry(window_register, font=("Arial", 12), width=10, textvariable=var_new_phone)
        entry_phone_reg.place(height=30, width=200, x=130, y=240)
        
        # 註冊視窗-履歷表
        var_new_resume = tk.StringVar()
        
        lab_resume_reg = tk.Label(window_register, text="履歷表：", font=("Arial", 16), width=10, height=1, anchor="e")
        lab_resume_reg.place(height=50, width=120, x=10, y=280)
        
        entry_resume_reg = tk.Entry(window_register, font=("Arial", 12), width=10, textvariable=var_new_resume)
        entry_resume_reg.place(height=300, width=260, x=70, y=330)
        
        # 註冊視窗-確認
        btn_confirm = tk.Button(window_register, text="確認註冊", font=("Arial", 16), width=20, height=1, command=confirm_register)
        btn_confirm.place(height=30, width=100, x=230, y=650)
    
    # # 主視窗基本設定
    window_main = tk.Tk()
    window_main.title("104人力銀行")
    window_main.geometry("600x480")
    window_main.resizable(width=False, height=False)
    
    # 主視窗-標題
    lab_title = tk.Label(window_main, text="104 人力銀行", font=("Arial", 32), width=20, height=1)
    lab_title.place(height=100, width=300, x=150, y=50)
    
    # 主視窗-帳號
    var_account = tk.StringVar()
    var_account.set("example@mail")
    
    lab_account = tk.Label(window_main, text="帳號：", font=("Arial", 16), width=10, height=1)
    lab_account.place(height=50, width=100, x=150, y=170)
    
    entry_account = tk.Entry(font=("Arial", 12), width=10, textvariable=var_account)
    entry_account.place(height=30, width=200, x=230, y=180)
    
    # 主視窗-密碼
    var_password = tk.StringVar()
    
    lab_password = tk.Label(window_main, text="密碼：", font=("Arial", 16), width=10, height=1)
    lab_password.place(height=50, width=100, x=150, y=220)
    
    entry_password = tk.Entry(font=("Arial", 12), width=10, show="*", textvariable=var_password)
    entry_password.place(height=30, width=200, x=230, y=230)
    
    # 主視窗-註冊鈕
    btn_register = tk.Button(window_main, text="註冊", font=("Arial", 16), width=10, height=1, command=user_register)
    btn_register.place(height=30, width=50, x=230, y=280)
    
    # 主視窗-登入鈕
    btn_login = tk.Button(window_main, text="登入", font=("Arial", 16), width=10, height=1, command=user_login)
    btn_login.place(height=30, width=50, x=380, y=280)
    
    window_main.mainloop()
