import os
import pandas as pd

'''
这个程序用来讲fillder抓包的内容转换成csv
fillder抓包是为了模拟微信电脑客户端来访问公众号文章链接，以期得到token，获得withtoken数据
在fillder的script的BeforeRespone添加如下JS代码：
        //这里以下为添加
        if(oSession.host == 'mp.weixin.qq.com'&&oSession.url.match('getappmsgext'))
        {
            var filename = "E:/filter.txt";
    
            var logContent = oSession.fullUrl;
            var logWhat = oSession.RequestHeaders + "\n";
            var sw : System.IO.StreamWriter;
            if (System.IO.File.Exists(filename)){  //是否有该文件夹  
                sw = System.IO.File.AppendText(filename);   //有添加
                sw.Write(logContent);
                sw.Write(logWhat);
            }
            else{
                sw = System.IO.File.CreateText(filename);  //没有创建
                sw.Write(logContent);
                sw.Write(logWhat);
            }
            sw.Close();
            sw.Dispose();
        }
        //这里以上为添加
'''

lis_fakeid = []
lis_appmsg_token = []
lis_cookie = []

lines = open(r'WithToken\filter.txt').readlines()
count = 0
for line in lines:
    count += 1
    if count == 1:
        #print(line.split('&')[9])
        lis_appmsg_token.append(line.split('&')[9][13:])
    if count == 10:
        print(line[8:])
        lis_cookie.append(line[8:])
    if count == 14:
        #print(line.split('&')[0][-16:])
        lis_fakeid.append(line.split('&')[0][-16:])

    if line == '\n':
        print("################")
        count = 0

df0 = pd.DataFrame([lis_fakeid,lis_appmsg_token,lis_cookie])
df0 = df0.T
df0.columns = ['fajeid','appmsg_token','cookie']
#columns=['fajeid','appmsg_token','cookie']
print(df0)
df0.to_csv('wechat_toukens.csv')

'''
输出的csv文件由token、cookie，但没有文件名，需要用fakeid与公众号名称对应。
这里我嫌麻烦用excel的vlookup手动操作。
excel打开utf-8编码的文件需要‘工具栏-数据-从csv’，可以自动识别。
'''