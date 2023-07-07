import pandas as pd
import os 

Folder_Path= 'TargetUrls' # 获取源目标文件夹
SaveFile_Path='TargetUrls'  # 拼接后要保存的文件路径  
SaveFile_Name='SCF_all.csv'    #合并后要保存的文件名字

os.chdir(Folder_Path)
file_list = os.listdir()

#  遍历读取文件夹中的每一个文件
fileStart = 1
fileEnd = len(file_list)
for i in range(fileStart,fileEnd):
    df = pd.read_csv(Folder_Path + '/' + file_list[i], 
               encoding = "utf8")
    df = df[1]
    df.to_csv (SaveFile_Path + '/' + SaveFile_Name,
               encoding = "utf8",
               index = False,
               header = True,#如果对每个文件的标题另外有需求，需要对header变量进行指定
               mode = 'a')
    print('共合并%i个CSV文件'% len(file_list))
