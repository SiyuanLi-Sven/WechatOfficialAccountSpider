import pandas as pd
import random
import numpy as np
import requests
import time
from bs4 import BeautifulSoup
import os
from wechatarticles import ArticlesInfo

appmsg_token = r'1189_dDAOjplX00Yx05Z%2BeDQwKbHPhLnsoh9fw2YL4Ku2LpqxRznsZz5MjIYwxqB2DQN3NnLcRwp7jHQvoU7v'
cookie = r"rewardsn=; wxtokenkey=777; wxuin=2817795206; devicetype=Windows10x64; version=6307001d; lang=zh_CN; pass_ticket=Wfl1bCq0U9FHub67O4URVj/rPRWUd4jaH0F1qNOiIQSStmC1Ip7JI9zONgRW43La; appmsg_token=1189_dDAOjplX00Yx05Z%2BeDQwKbHPhLnsoh9fw2YL4Ku2LpqxRznsZz5MjIYwxqB2DQN3NnLcRwp7jHQvoU7v; wap_sid2=CIbJ0L8KEooBeV9ITWJGRVFpeXFpd0xDN1dGdlh6eGxqbTZfN3B3b1lRQTBPMDV5a3B1R3d6TmI1VUMzSC15dFZvZF9DWFN4bENGSEFkR01fMmpzTjhFdXQyaDlJOUpYVktTdmtUUXNEeGllUk1tWnowaGtQa2hIeXdZdkU5UFE2VGlNaGJHcjZ6TVU0TVNBQUF+MIrz/JoGOA1AAQ=="
url_lis = ['']
target_urls = df0['link']
print(df0)

count = 0
mistake_url = []
wrong_urls = []
for index,row in df0.iterrows():
    try:
        count += 1
        time.sleep(random.random()*5) # 设置休眠时长
        article_url = row['link']
        print(article_url)
        # article_url = 'https://mp.weixin.qq.com/s?t=pages/image_detail&__biz=MzIxNTg2MTA5NQ==&mid=2247487639&idx=1&sn=559246e1286018c888397655060dca8f&from=singlemessage&scene=1&subscene=10000&clicktime=1667146102&enterid=1667146102&ascene=1&devicetype=android-29&version=28000f3d&nettype=WIFI&abtest_cookie=AAACAA%3D%3D&lang=zh_CN&exportkey=n_ChQIAhIQ8n9clpE%2FsYp2kOOsViRZGRLvAQIE97dBBAEAAAAAAKboDrHUtwUAAAAOpnltbLcz9gKNyK89dVj0gzC3OrToLxzEPxppbyGVicd%2FXxNa4cMgYD%2Ft3zMBHTf0PZl%2FoYpGDpFosy9fYP1OeB8FQBEDh72X5jGW4qCxk%2BAYyYN50BR%2Ft4UBzRMVL9I9uYi3OuqjfwdwhjfrfTzJjW2jqv4Wi0AvEFEiCJ05XWPV88A%2FRpjw6QcfrJL%2BDgYSW1tXbSKWlsRhjYjFT4Yz5slVuizxdrBsSWZjjAwJJ%2BCBBD%2BwhmnIv350SkI7jc7AMac1OkgBL7p8KxmIwTAx7OK6f3GGAQnS&pass_ticket=ftrovc9LuK63sKUoaDGURQiqd%2FJDHNUno7Lto362UVSob8CM%2FGnGmYcu5v7dFJ6c&wx_header=3'
        test = ArticlesInfo(appmsg_token, cookie)
        comments = test.comments(article_url)
        read_num, like_num, old_like_num = test.read_like_nums(article_url)
        print("comments:")
        print(comments['elected_comment'])
        print("read_like_num:", read_num, like_num, old_like_num)
        df0.loc[index,'read_num'] = read_num
        df0.loc[index,'like_num'] = like_num
        df0.loc[index,'old_like_num'] = old_like_num

        lis_content = []
        lis_like_num = []
        lis_auther_reply = []
        lis_auther_like_num = []

        if len(comments['elected_comment']) > 0:
            for i in comments['elected_comment']:
                lis_content.append(i['content'])
                lis_like_num.append(i['like_num'])
        print(lis_content)
        print(lis_like_num)

        df0.loc[index,'content'] = '$'.join(lis_content)
        df0.loc[index,'content_like_num'] = '$'.join(lis_like_num)
        print('已完成：{}\n比例：{}'.format(count,count/len(target_urls)))
    except:
        df0.loc[index,'read_num'] = np.nan
        df0.loc[index,'like_num'] = np.nan
        df0.loc[index,'old_like_num'] = np.nan
        df0.loc[index,'content'] = np.nan
        df0.loc[index,'like_num'] = np.nan
        mistake_url.append(article_url)


df0.to_csv('WithToken\{}.csv'.format(book_name),encoding='utf-8',index=None)
print('>>> MISSION ACCOMPLISHED')
print(mistake_url)


