# -- coding: utf-8 --**
import pandas as pd
import random
import numpy as np
import requests
import time
from bs4 import BeautifulSoup
import os
from wechatarticles import ArticlesInfo
import csv


def main(book_name,appmsg_token,cookie):
    global temp_writer
    try:
        df0 = pd.read_csv('WithoutToken/{}.csv'.format(book_name), encoding='utf-8')
        df0 = df0.reindex(index=df0.index[::-1])
        df0 = df0.loc[3139:]
        target_urls = df0['link']
        print(df0)

        count = 0
        mistake_url = []
        wrong_urls = []
        for index,row in df0.iterrows():
            try:
                count += 1
                time.sleep(1+random.random()*2) # 设置休眠时长
                article_url = row['link']
                print('总长度：{} 已完成：{} 比例：{} 期望时间：{}min'.format(len(article_url),count,count/len(article_url),-(count-len(article_url))*1.5/60))
                print(book_name + article_url)
                #article_url = 'https://mp.weixin.qq.com/s?__biz=MzIxNTg2MTA5NQ==&mid=2247487721&idx=1&sn=1f45070e3668e11ac9e6ab50a3d5415b&chksm=979082e1a0e70bf7d5dd6f60780f0bec15a390734d1d2fd96cd41c2c2d2ff9edf9d262360a29&token=2048984886&lang=zh_CN#rd'
                test = ArticlesInfo(appmsg_token, cookie)
                # print(test)
                comments = test.comments(article_url)
                read_num, like_num, old_like_num = test.read_like_nums(article_url)
                #print("comments:")
                #print(comments['elected_comment'])
                print("read_like_num:", read_num, like_num, old_like_num)
                df0.loc[index,'read_num'] = read_num
                df0.loc[index,'like_num'] = like_num
                df0.loc[index,'old_like_num'] = old_like_num
 
                #下面是评论的数据
                lis_content = []
                lis_like_num = []
                lis_auther_reply = []
                lis_auther_like_num = []
                if comments.__contains__('elected_comment'):
                    if len(comments['elected_comment']) > 0:
                        for i in comments['elected_comment']:
                            print(i)
                            lis_content.append(i['content'].replace('\n',''))
                            lis_like_num.append(str(i['like_num']))
                            if i.__contains__('reply_new') and i['reply_new'].__contains__('reply_list'):
                                if i['reply_new']['reply_list'] != []:
                                    lis_auther_reply.append(i['reply_new']['reply_list'][0]['content'].replace('\n',''))
                                    lis_auther_like_num.append(str(i['reply_new']['reply_list'][0]['reply_like_num']))
                                else:
                                    lis_auther_reply.append('nan')
                                    lis_auther_like_num.append('nan')
                    
                    print(lis_content,end='')
                    print(lis_like_num,end='')
                    print(lis_auther_reply,end='')
                    print(lis_auther_like_num)

                    df0.loc[index,'lis_content'] = '☀'.join(lis_content)
                    df0.loc[index,'lis_content_like_num'] = '☀'.join(lis_like_num)
                    df0.loc[index,'lis_auther_reply'] = '☀'.join(lis_auther_reply)
                    df0.loc[index,'lis_auther_like_num'] = '☀'.join(lis_auther_like_num)
                    #print('已完成：{}\n比例：{}'.format(count,count/len(target_urls)))
                    temp_writer.writerow(df0.loc[index])
                
                else:
                    df0.loc[index,'read_num'] = np.nan
                    df0.loc[index,'like_num'] = np.nan
                    df0.loc[index,'old_like_num'] = np.nan
                    df0.loc[index,'content'] = np.nan
                    print(lis_content,end='')
                    print(lis_like_num,end='')
                    print(lis_auther_reply,end='')
                    print(lis_auther_like_num)
                    temp_writer.writerow(df0.loc[index])
                    

            except:
                df0.loc[index,'read_num'] = 'nan'
                df0.loc[index,'like_num'] = 'nan'
                df0.loc[index,'old_like_num'] = 'nan'
                df0.loc[index,'content'] = 'nan'
                df0.loc[index,'like_num'] = 'nan'
                df0.loc[index,'lis_content'] = 'nan'
                df0.loc[index,'lis_content_like_num'] = 'nan'
                df0.loc[index,'lis_auther_reply'] = 'nan'
                df0.loc[index,'lis_auther_like_num'] = 'nan'
                print('Mistake were made when handling url' + article_url)
                mistake_url.append(article_url)
                temp_writer.writerow(df0.loc[index])
                raise

        df0.to_csv('WithToken\{}.csv'.format(book_name),encoding='utf-8',index=None)
        print('>>> MISSION ACCOMPLISHED')
        print(mistake_url)
    except:
        raise
        df0.to_csv('WithToken\{}.csv'.format(book_name), encoding='utf-8', index=None)
        print('>>> MISSION ACCOMPLISHED')
        print(mistake_url)


if __name__ == '__main__':
# 登录微信PC端获取文章信息
    f0 = open('temp_save3.csv','w',encoding='utf-8',newline='')
    temp_writer = csv.writer(f0)

    #appmsg_token = r'1194_ORhf0h9GviWCsT6CsN_K9aQg6SdIbM4_6Q2ir1yjanMPFaJwewgsAg30Jrgivy-93IzDCffOZHFYbK4V'
    #cookie = r"rewardsn=; wxtokenkey=777; wxuin=2817795206; devicetype=Windows10x64; version=6307001d; lang=zh_CN; appmsg_token=1194_ORhf0h9GviWCsT6CsN_K9aQg6SdIbM4_6Q2ir1yjanMPFaJwewgsAg30Jrgivy-93IzDCffOZHFYbK4V; pass_ticket=nY/ZW/ri3f4Ine/AESkpoW0Ere6DVMaFWbdbceujcCJSs3phtiVXTWnqFilRfQ7X; wap_sid2=CIbJ0L8KEooBeV9ITDJvb2lBTXV5enJYaFhEbGVlME9uLXNHSU4tWFF1OHZfQk5iMDdqM0U5WHlnd085cXl6N3ZxU1hWeTBmMjRncHFzbjRlUGpncnN3SDBDZWV1XzBpUkV4Y0FGeWJyeldOQ1hoQ05WMlZCUzctM2VHRGNVTEdXTWlBdVlqQW5SVUU0Y1NBQUF+MKqunpwGOA1AAQ=="
    #main('B中国社会科学',appmsg_token,cookie)

    lis_address = os.listdir('WithoutToken')
    df0 = pd.read_csv(r'WithToken\Tokens.csv',encoding='ANSI')
    print(df0)
    for index,row in df0.iterrows():
        print('正在进行：{}'.format(row['期刊名称']))
        print(row['appmsg_token'].strip('\n').strip('\"'))
        print(row['cookie'].strip('\n').strip('\"').strip('\n'))
        main(row['期刊名称'],row['appmsg_token'].strip('\n').strip('\"').strip('\n'),row['cookie'].strip('\n').strip('\"').strip('\n')) 
