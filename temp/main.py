import pandas as pd
import numpy as np
import Url2Html
import time
import random

'''
主程序
调用各模块以实现整个功能
'''

def get_html(form_path):
    '''
    根据url保存文章的html
    '''


def main():
    df0 = pd.read_csv('北京社会科学.csv')
    target_urls = df0['link']
    print(df0)
    uh = Url2Html.Url2Html()
    count = 1
    wrong = 0
    for url in target_urls:
        count += 1
        time.sleep(1+random.random()*2)
        print(url)
        try:
            s = uh.run(url, mode=4)
            print(s)
        except:
            wrong += 1
            print(count)
            print('出错url：{}\n出错次数：{}\n出错比例：{}\n'.format(url,wrong,wrong/count))
            pass
    get_html()

main()