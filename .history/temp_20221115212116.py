import pandas as pd    #导入pandas库

data = pd.io.stata.read_stata('inputFileName.dta')   #读入待转换的文件名称
data.to_csv('outputFileName.csv')   #成功转换