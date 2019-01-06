import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
import window_main
import fuction


def start_window_login(login_user):
    # 取得使用者資料
    user_data = fuction.read_data()
    
    # 取得工作資料
    job_data = fuction.read_job()
    
    # 登入視窗-修改履歷表事件
    def rewrite_data():

        def confirm_rewrite_data():
            if var_rewrite_password.get() == "" or var_rewrite_name.get() == "" or var_rewrite_age.get() == "" or var_rewrite_phone.get() == "" or var_rewrite_resume.get() == "":
                tkinter.messagebox.showerror("錯誤", "尚有資料未填寫！")
            else:    
                tmp_lsit = [var_rewrite_password.get(), var_rewrite_name.get(), var_rewrite_age.get(), var_rewrite_phone.get(), var_rewrite_resume.get()]
                user_data[login_user] = tmp_lsit
                
                with open("user_data.txt", "w", encoding="UTF-8-sig") as f:
                    f.write(str(user_data))
                
                tkinter.messagebox.showinfo("恭喜", "修改成功！")
                window_rewrite_data.grab_release()
                window_rewrite_data.destroy()
                window_login.destroy()
                start_window_login(login_user)
            
        # # 修改視窗基本設定
        window_rewrite_data = tk.Toplevel(window_login)
        window_rewrite_data.title("修改資料")
        window_rewrite_data.geometry("400x700")
        window_rewrite_data.resizable(width=False, height=False)
        window_rewrite_data.grab_set()
        
        # 修改視窗-帳號
        lab_account_rewrite = tk.Label(window_rewrite_data, text="帳號：", font=("Arial", 16), width=10, height=1, anchor="e")
        lab_account_rewrite.place(height=50, width=120, x=10, y=30)
        
        lab_account = tk.Label(window_rewrite_data, font=("Arial", 16), width=10, text=login_user, anchor="w")
        lab_account.place(height=30, width=200, x=130, y=40)
        
        # 修改視窗-密碼
        var_rewrite_password = tk.StringVar()
        var_rewrite_password.set(user_data[login_user][0])
        
        lab_password_rewrite = tk.Label(window_rewrite_data, text="密碼：", font=("Arial", 16), width=10, height=1, anchor="e")
        lab_password_rewrite.place(height=50, width=120, x=10, y=80)
        
        entry_password_rewrite = tk.Entry(window_rewrite_data, font=("Arial", 12), width=10, textvariable=var_rewrite_password)
        entry_password_rewrite.place(height=30, width=200, x=130, y=90)
        
        # 修改視窗-姓名
        var_rewrite_name = tk.StringVar()
        var_rewrite_name.set(user_data[login_user][1])
        
        lab_name_rewrite = tk.Label(window_rewrite_data, text="姓名：", font=("Arial", 16), width=10, height=1, anchor="e")
        lab_name_rewrite.place(height=50, width=120, x=10, y=130)
        
        entry_name_rewrite = tk.Entry(window_rewrite_data, font=("Arial", 12), width=10, textvariable=var_rewrite_name)
        entry_name_rewrite.place(height=30, width=200, x=130, y=140)
        
        # 修改視窗-年齡
        var_rewrite_age = tk.StringVar()
        var_rewrite_age.set(user_data[login_user][2])
        
        lab_age_rewrite = tk.Label(window_rewrite_data, text="年齡：", font=("Arial", 16), width=10, height=1, anchor="e")
        lab_age_rewrite.place(height=50, width=120, x=10, y=180)
        
        entry_age_reg = tk.Entry(window_rewrite_data, font=("Arial", 12), width=10, textvariable=var_rewrite_age)
        entry_age_reg.place(height=30, width=200, x=130, y=190)
        
        # 修改視窗-電話
        var_rewrite_phone = tk.StringVar()
        var_rewrite_phone.set(user_data[login_user][3])
        
        lab_phone_rewrite = tk.Label(window_rewrite_data, text="電話：", font=("Arial", 16), width=10, height=1, anchor="e")
        lab_phone_rewrite.place(height=50, width=120, x=10, y=230)
        
        entry_phone_rewrite = tk.Entry(window_rewrite_data, font=("Arial", 12), width=10, textvariable=var_rewrite_phone)
        entry_phone_rewrite.place(height=30, width=200, x=130, y=240)
        
        # 修改視窗-履歷表
        var_rewrite_resume = tk.StringVar()
        var_rewrite_resume.set(user_data[login_user][4])
        
        lab_resume_rewrite = tk.Label(window_rewrite_data, text="履歷表：", font=("Arial", 16), width=10, height=1, anchor="e")
        lab_resume_rewrite.place(height=50, width=120, x=10, y=280)
        
        entry_resume_rewrite = tk.Entry(window_rewrite_data, font=("Arial", 12), width=10, textvariable=var_rewrite_resume)
        entry_resume_rewrite.place(height=300, width=260, x=70, y=330)
        
        # 修改視窗-確認
        btn_confirm = tk.Button(window_rewrite_data, text="確認修改", font=("Arial", 16), width=20, height=1, command=confirm_rewrite_data)
        btn_confirm.place(height=30, width=100, x=230, y=650)
    
    
    # 登入視窗-新增工作事件
    def add_job():

        def confirm_add_job():
            # 取得工作資料
            job_data = fuction.read_job()
            
            if var_job_name.get() == "" or var_job_address.get() == "" or var_job_salary.get() == "" or var_job_owner.get() == "" or var_job_phone.get() == "" or var_job_data.get() == "":
                tkinter.messagebox.showerror("錯誤", "尚有資料未填寫！")
            else:
                tmp_list = [login_user, var_job_name.get(), var_job_address.get(), var_job_salary.get(), var_job_owner.get(), var_job_phone.get(), var_job_data.get(), []]
                
                for i in range(1, 101, 1):
                    if i not in job_data:
                        print(i)
                        job_data[i] = tmp_list

                        with open("job_data.txt", "w", encoding="UTF-8-sig") as f:
                            f.write(str(job_data))
                         
                        user_data = fuction.read_data()
                        user_data[login_user][5].append(i)
                           
                        with open("user_data.txt", "w", encoding="UTF-8-sig") as f:
                            f.write(str(user_data))
                            
                        tkinter.messagebox.showinfo("恭喜", "工作新增成功！")
                        window_add_job.grab_release()
                        window_add_job.destroy()
                        window_login.destroy()
                        start_window_login(login_user)
                        
                        break
                    elif i == 100:
                        tkinter.messagebox.showerror("錯誤", "已達新增上限！")
                        window_add_job.grab_release()
                        window_add_job.destroy()
                        window_login.destroy()
                        start_window_login(login_user)
         
        # # 新增工作視窗基本設定
        window_add_job = tk.Toplevel(window_login)
        window_add_job.title("新增工作")
        window_add_job.geometry("400x700")
        window_add_job.resizable(width=False, height=False)
        window_add_job.grab_set()
        
        # 新增工作視窗-工作名稱
        var_job_name = tk.StringVar()
 
        lab_job_name = tk.Label(window_add_job, text="工作名稱：", font=("Arial", 16), width=10, height=1, anchor="e")
        lab_job_name.place(height=50, width=120, x=10, y=30)
        
        entry_job_name = tk.Entry(window_add_job, font=("Arial", 12), width=10, textvariable=var_job_name)
        entry_job_name.place(height=30, width=200, x=130, y=40)
        
        # 新增工作視窗-工作位置
        var_job_address = tk.StringVar()
        
        lab_job_address = tk.Label(window_add_job, text="地點：", font=("Arial", 16), width=10, height=1, anchor="e")
        lab_job_address.place(height=50, width=120, x=10, y=80)
        
        entry_job_address = tk.Entry(window_add_job, font=("Arial", 12), width=10, textvariable=var_job_address)
        entry_job_address.place(height=30, width=200, x=130, y=90)
        
        # 新增工作視窗-薪資
        var_job_salary = tk.StringVar()
        
        lab_job_salary = tk.Label(window_add_job, text="薪資：", font=("Arial", 16), width=10, height=1, anchor="e")
        lab_job_salary.place(height=50, width=120, x=10, y=130)
        
        entry_job_salary = tk.Entry(window_add_job, font=("Arial", 12), width=10, textvariable=var_job_salary)
        entry_job_salary.place(height=30, width=200, x=130, y=140)
        
        # 新增工作視窗-聯絡人
        var_job_owner = tk.StringVar()
        var_job_owner.set(user_data[login_user][1])
        
        lab_job_owner = tk.Label(window_add_job, text="聯絡人：", font=("Arial", 16), width=10, height=1, anchor="e")
        lab_job_owner.place(height=50, width=120, x=10, y=180)
        
        entry_job_owner = tk.Entry(window_add_job, font=("Arial", 12), width=10, textvariable=var_job_owner)
        entry_job_owner.place(height=30, width=200, x=130, y=190)
        
        # 新增工作視窗-電話
        var_job_phone = tk.StringVar()
        var_job_phone.set(user_data[login_user][3])
        
        lab_job_phone = tk.Label(window_add_job, text="聯絡電話：", font=("Arial", 16), width=10, height=1, anchor="e")
        lab_job_phone.place(height=50, width=120, x=10, y=230)
        
        entry_job_phone = tk.Entry(window_add_job, font=("Arial", 12), width=10, textvariable=var_job_phone)
        entry_job_phone.place(height=30, width=200, x=130, y=240)
        
        # 新增工作視窗-簡介
        var_job_data = tk.StringVar()
        
        lab_job_data = tk.Label(window_add_job, text="簡介：", font=("Arial", 16), width=10, height=1, anchor="e")
        lab_job_data.place(height=50, width=120, x=10, y=280)
        
        entry_job_data = tk.Entry(window_add_job, font=("Arial", 12), width=10, textvariable=var_job_data)
        entry_job_data.place(height=300, width=260, x=70, y=330)
        
        # 新增工作視窗-確認
        btn_confirm = tk.Button(window_add_job, text="確認新增", font=("Arial", 16), width=20, height=1, command=confirm_add_job)
        btn_confirm.place(height=30, width=100, x=230, y=650)
        
    
    # 登入視窗-登出事件
    def user_logout():
        logout_check = tkinter.messagebox.askquestion("登出", "確定要離開嗎？")
        
        if logout_check == "yes":
            window_login.destroy()
            window_main.start_window_main()
             
    def my_job():
        def my_job_display():
            '''
            var_my_job_select = tk.StringVar()
            
            cb_my_job_select = ttk.Combobox(window_my_job, textvariable=var_my_job_select, font=("Arial", 16), width=100)
            
            list_my_job_select_applier = []
            
            cb_my_job_select['values'] = list_my_job_select_applier
            
            
            
            cb_my_job_select.place(height=30, width=300, x=15, y=70)
        
            # 選擇顯示工作按鈕
            btn_job_display = tk.Button(window_my_job, text="顯示應徵者", font=("Arial", 13), width=20, height=1, command=my_job_display)
            btn_job_display.place(height=30, width=100, x=330, y=70)
            '''
        
        # # 我的工作視窗基本設定
        window_my_job = tk.Toplevel(window_login)
        window_my_job.title("我的工作")
        window_my_job.geometry("450x300")
        window_my_job.resizable(width=False, height=False)
        window_my_job.grab_set()
        
        # 我的工作顯示
        var_my_job = tk.StringVar()
        
        list_my_job_num = user_data[login_user][5]
        list_my_job = []
        
        for i in range(0, len(list_my_job_num)):
            list_my_job.append(job_data[list_my_job_num[i]][1])
        
        cb_my_job = ttk.Combobox(window_my_job, textvariable=var_my_job, font=("Arial", 16), width=100)
        
        cb_my_job['values'] = list_my_job
        
        cb_my_job.place(height=30, width=300, x=15, y=20)
        
        '''
        # 選擇顯示工作按鈕
        btn_job_display = tk.Button(window_my_job, text="顯示工作", font=("Arial", 16), width=20, height=1, command=my_job_display)
        btn_job_display.place(height=30, width=100, x=330, y=20)
        ''' 
        
        
    def my_apply():
        def my_apply_dsiplay():
            pass
        
        # # 我的應徵視窗基本設定
        window_my_apply = tk.Toplevel(window_login)
        window_my_apply.title("我的應徵")
        window_my_apply.geometry("450x300")
        window_my_apply.resizable(width=False, height=False)
        window_my_apply.grab_set()
        
        # 我的應徵顯示
        var_my_job = tk.StringVar()
        
        list_my_apply_num = user_data[login_user][6]
        list_my_apply = []
        
        for i in range(0, len(list_my_apply_num)):
            list_my_apply.append(job_data[list_my_apply_num[i]][1])
        
        
        cb_my_job = ttk.Combobox(window_my_apply, textvariable=var_my_job, font=("Arial", 16), width=100)
        
        cb_my_job['values'] = list_my_apply
        
        cb_my_job.place(height=30, width=300, x=15, y=20)
         
        '''
        # 選擇顯示工作按鈕
        btn_job_display = tk.Button(window_my_apply, text="顯示應徵", font=("Arial", 16), width=20, height=1, command=my_apply_dsiplay)
        btn_job_display.place(height=30, width=100, x=330, y=20)
        '''
        
    def job_display():
        # 顯示工作
        if var_job_select.get() != '':
            tmp_select = list_job.index(var_job_select.get()) + 1
            
            txt_job_name = job_data[tmp_select][1]
            txt_job_address = job_data[tmp_select][2]
            txt_job_salary = job_data[tmp_select][3]
            txt_job_owner = job_data[tmp_select][4]
            txt_job_phone = job_data[tmp_select][5]
            txt_job_info = job_data[tmp_select][6]
        
            lab_job_name = tk.Label(window_login, text="工作名稱：" + txt_job_name, font=("Arial", 16), width=10, height=1, anchor="w")
            lab_job_name.place(height=30, width=300, x=150, y=70)
            
            lab_job_address = tk.Label(window_login, text="地點：" + txt_job_address, font=("Arial", 16), width=10, height=1, anchor="w")
            lab_job_address.place(height=30, width=300, x=150, y=120)
            
            lab_job_salary = tk.Label(window_login, text="薪資：" + txt_job_salary, font=("Arial", 16), width=10, height=1, anchor="w")
            lab_job_salary.place(height=30, width=300, x=150, y=170)
            
            lab_job_owner = tk.Label(window_login, text="聯絡人：" + txt_job_owner, font=("Arial", 16), width=10, height=1, anchor="w")
            lab_job_owner.place(height=30, width=300, x=150, y=220)
            
            lab_job_phone = tk.Label(window_login, text="連絡電話：" + txt_job_phone, font=("Arial", 16), width=10, height=1, anchor="w")
            lab_job_phone.place(height=30, width=300, x=150, y=270)
            
            lab_job_info = tk.Label(window_login, text="簡介：" + txt_job_info, font=("Arial", 16), width=10, height=1, anchor="w")
            lab_job_info.place(height=30, width=300, x=150, y=320)
    # 登入視窗-應徵工作事件
    def apply_job():
        if var_job_select.get() != '':
            tmp_select = list_job.index(var_job_select.get()) + 1
            
            if tmp_select in job_data:
                    
                if login_user == job_data[tmp_select][0]:
                    tkinter.messagebox.showerror("錯誤", "這是您新增的工作！")
                elif login_user in job_data[tmp_select][7]:
                    tkinter.messagebox.showerror("錯誤", "您已應徵此工作！")
                else:
                    job_data[tmp_select][7].append(login_user)
                    tkinter.messagebox.showinfo("恭喜", "您已成功應徵！")
                    
                    with open("job_data.txt","w",encoding="UTF-8-sig") as f:
                        f.write(str(job_data))
                        
                    user_data = fuction.read_data()
                    user_data[login_user][6].append(tmp_select)
                       
                    with open("user_data.txt", "w", encoding="UTF-8-sig") as f:
                        f.write(str(user_data))
        
    # # 登入視窗基本設定
    window_login = tk.Tk()
    window_login.title("登入畫面")
    window_login.geometry("600x480")
    window_login.resizable(width=False, height=False)
    
    # 登入視窗-使用者圖像
    cv_user_image = tk.Canvas(window_login, bg="gray")
    cv_user_image.place(height=100, width=100, x=10, y=10)
    
    # 登入視窗-使用者姓名
    lab_user_name = tk.Label(window_login, text=user_data[login_user][1], font=("Arial", 16), width=10, height=1, anchor="w")
    lab_user_name.place(height=30, width=100, x=10, y=120)
    
    # 登入視窗-使用者年齡
    lab_user_name = tk.Label(window_login, text=user_data[login_user][2] + "歲", font=("Arial", 16), width=10, height=1, anchor="w")
    lab_user_name.place(height=30, width=100, x=10, y=150)
    
    # 登入視窗-修改資料鈕
    btn_rewrite_resume = tk.Button(window_login, text="修改資料", font=("Arial", 16), width=20, height=1, command=rewrite_data)
    btn_rewrite_resume.place(height=30, width=100, x=10, y=190)
    
    # 登入視窗-新增工作鈕
    btn_add_job = tk.Button(window_login, text="新增工作", font=("Arial", 16), width=20, height=1, command=add_job)
    btn_add_job.place(height=30, width=100, x=10, y=230)
    
    # 登入視窗-我的工作鈕
    btn_my_job = tk.Button(window_login, text="我的工作", font=("Arial", 16), width=20, height=1, command=my_job)
    btn_my_job.place(height=30, width=100, x=10, y=270)
    
    # 登入視窗-我的應徵鈕
    btn_my_apply = tk.Button(window_login, text="我的應徵", font=("Arial", 16), width=20, height=1, command=my_apply)
    btn_my_apply.place(height=30, width=100, x=10, y=310)
    
    # 登入視窗-登出鈕
    btn_logout = tk.Button(window_login, text="登出", font=("Arial", 16), width=20, height=1, command=user_logout)
    btn_logout.place(height=30, width=100, x=10, y=430)
    
    # 登入視窗-應徵工作鈕
    btn_apply_job = tk.Button(window_login, text="應徵工作", font=("Arial", 16), width=20, height=1, command=apply_job)
    btn_apply_job.place(height=30, width=100, x=470, y=430)
    
    # 刊登工作顯示-by ComboBox
    var_job_select = tk.StringVar()
    
    list_job = []
    
    for i in range(1, len(job_data) + 1, 1):
        if i in job_data:
            list_job.append(job_data[i][1])
            
    cb_job_display = ttk.Combobox(window_login, textvariable=var_job_select, font=("Arial", 16), width=100)
    cb_job_display['values'] = list_job
    cb_job_display.place(height=30, width=300, x=150, y=20)
    
    # 選擇顯示工作按鈕
    btn_job_display = tk.Button(window_login, text="顯示工作", font=("Arial", 16), width=20, height=1, command=job_display)
    btn_job_display.place(height=30, width=100, x=470, y=20)
    
    #
    window_login.mainloop()
