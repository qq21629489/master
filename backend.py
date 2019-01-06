def menu(): 
    os.system("cls")
    print("人力銀行介面")
    print("工作列表")
    print("---------------------------")
    disp_job()
    print("---------------------------")
    print("1.註冊帳號與填寫履歷")
    print("2.登入")
    print("0.結束程式")
    print("---------------------------")
    
def ReadData(): #讀檔
    with open("password.txt","r",encoding = "UTF-8=sig") as f:
        filedata = f.read()
        if filedata != "":
            data = ast.literal_eval(filedata) #只能讀字典
            return data
        else: return dict() #如果檔案沒東西則傳回空字典
        
#account為帳號#
#password為0密碼#
#name為1姓名#
#birthday為2生日#
#phone為3電話#
#email為4信箱#
#job為5工作#
#company為6公司行號
#school為7學經歷#
def CreateAccount_data(): 
        account =input("請輸入帳號") 
        if account in data:
            print("{}帳號已存在!".format(account))
        else:
            password=input("請輸入密碼:")
            name=input("請輸入姓名")
            birthday=input("請輸入生日:西元年/月/日")
            phone=input("請輸入連絡電話")
            email=input("請輸入信箱")
            job=''
            company=''
            school=input("請輸入學經歷")
            list1=[password,name,birthday,phone,email,job,company,school] 
            data[account]=list1
            with open("password.txt","w",encoding="UTF-8-sig") as f:
                f.write(str(data))
            print("{}已被儲存完畢".format(account))

def Edit_job(): #刊登工作
    account =input("請輸入要修改的帳號")
    if not account in data:
        print("{} 帳號不存在!".format(account))
    job=input("請輸入要刊登的工作與地點:")
    company=input("請輸入你的公司行號")
    data[account][5]=job
    data[account][6]=company
    with open("password.txt","w",encoding="UTF-8-sig") as f:
        f.write(str(data))
    input("刊登完畢，請按Enter鍵返回主選單")
    
def disp_job(): #刊登的工作顯示在人力銀行的介面
    for account in data:
        print("{}\t{}".format(data[account][5],data[account][6]))

def disp_data(): #要應徵的工作可以看到聯絡方式
    for account in data:
        print("{}\t{}\t{}".format(data[account][5],data[account][6],data[account][4]))
        
def EditPassword_data(): #修改密碼
        account =input("請輸入要修改的帳號")
        if not account in data:
            print("{} 帳號不存在!".format(account))
        else:
            oldpassword =input("請輸入原密碼")
            if oldpassword != data[account][0]:
                print("密碼錯誤")
            else:
                password=input("請輸入新密碼:")
                data[account][0]=password
                with open("password.txt","w",encoding="UTF-8-sig") as f:
                    f.write(str(data))
                input("密碼更改完畢，請按Enter鍵返回主選單")


def Edit_data(): #修改履歷    
        account =input("請輸入要修改的帳號")
        if not account in data:
            print("{} 帳號不存在!".format(account))
        else:
            name=input("請輸入姓名:")
            birthday=input("請輸入生日:西元年/月/日")
            phone=input("請輸入連絡電話")
            email=input("請輸入信箱")
            data[account][1]=name
            data[account][2]=birthday
            data[account][3]=phone
            data[account][4]=email
            with open("password.txt","w",encoding="UTF-8-sig") as f:
                f.write(str(data))
            input("履歷更改完畢，請按Enter鍵返回主選單")

def Job_menu():
    os.system("cls")
    print("工作列表")
    print("工作\t地點\t聯絡方式")
    print("---------------------------")
    disp_data()
    print("---------------------------")        

def Login_menu():
    os.system("cls")
    print("工作列表")
    print("---------------------------")
    disp_job()
    print("---------------------------")
    print("1.修改履歷")
    print("2.修改密碼") 
    print("3.刊登工作")
    print("4.應徵工作")
    print("0.登出")
    print("---------------------------")

    
def Login(): #登入會員介面
    while True:
        account =input("請輸入你的帳號(Enter==>停止輸入)")
        if account=="":break
        if not account in data:
            print("{} 帳號不存在!".format(account))
            continue        
        password=input("請輸入密碼:")
        if password != data[account][0]:
            continue
        else:
            while True:
                print("會員介面")
                print("---------------------------")
                print("姓名:{}".format(data[account][1]))
                print("生日:{}".format(data[account][2]))
                print("電話:{}".format(data[account][3]))
                print("信箱:{}".format(data[account][4]))
                Login_menu()
                choice = int(input("請輸入妳的選擇:"))
                if choice==1:
                    Edit_data()
                elif choice==2:
                    EditPassword_data()
                elif choice==3:
                    Edit_job()
                elif choice==4:
                    while True:
                        Job_menu()
                        input()
                        break
                else:
                    break
        break

###主程式###
import os,ast
data=dict() #帳號密碼字典
data=ReadData()
while True:
    menu()
    choice = int(input("請輸入妳的選擇:"))
    print()
    if choice==1:
        CreateAccount_data()
    elif choice==2:
        Login()
    else:
        break
    
print("程式執行完畢")
