import ast

def read_data():
    data = dict()
    
    with open("user_data.txt","r",encoding = "UTF-8=sig") as f:
        filedata = f.read()
        if filedata != "":
            data = ast.literal_eval(filedata) #只能讀字典
            return data
        else: 
            return dict() #如果檔案沒東西則傳回空字典
        
def read_job():
    data = dict()
    
    with open("job_data.txt","r",encoding = "UTF-8=sig") as f:
        filedata = f.read()
        if filedata != "":
            data = ast.literal_eval(filedata) #只能讀字典
            return data
        else: 
            return dict() #如果檔案沒東西則傳回空字典
        
        
        
        
        
        

