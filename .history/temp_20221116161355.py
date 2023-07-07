import pandas as pd
import random
import numpy as np
import requests
import time
from bs4 import BeautifulSoup
import os
from wechatarticles import ArticlesInfo

appmsg_token = r'1192_oy57qhPVBcW989USn9Q1vDLPk6ujfoTAiy8cTccFpGmpR22RqPgEOwQsUDSJ0S_mzjeQYo4BEX5pKU32'
cookie = r"rewardsn=; wxtokenkey=777; wxuin=2817795206; devicetype=Windows10x64; version=6307001d; lang=zh_CN; appmsg_token=1192_oy57qhPVBcW989USn9Q1vDLPk6ujfoTAiy8cTccFpGmpR22RqPgEOwQsUDSJ0S_mzjeQYo4BEX5pKU32; pass_ticket=8hwrXYBB8OT6R+2ojjHn958b1rQ9JPDGoJG0ZgfYr1Hy1wgluoHv1DvRCzRjwF38; wap_sid2=CIbJ0L8KEooBeV9IQmFjb3RwWkdYd0d2QmhhNUNtTGVnMko4b25qdjVBVVhQMDBkMjhoSnhNMkMxM29hNlRHOEE0YjVxVUdNcFJVZHhDelpaMjhCTWREV3FlYURtTV9lNzBMbDRZNE9ZUUFka1VPUlFMRFFubEJSeHVIS2s1U3JsTEZpNVZGM3p5dzJZVVNBQUF+MNe10psGOA1AAQ=="
url_lis = ['https://mp.weixin.qq.com/s?t=pages/image_detail&__biz=MzIxNTg2MTA5NQ==&mid=2247487652&idx=1&sn=942f628499f6c18364f8e31e55017611&from=singlemessage&scene=1&subscene=10000&clicktime=1667478575&enterid=1667478575&ascene=1&devicetype=android-29&version=28000f3d&nettype=3gnet&abtest_cookie=AAACAA%3D%3D&lang=zh_CN&exportkey=n_ChQIAhIQF0HhpfJxnXz1doPUB8satBLvAQIE97dBBAEAAAAAALpdOaZt48QAAAAOpnltbLcz9gKNyK89dVj0m8a%2BTGrVZZOBE77ZqO2%2FDEn66LDjg2jBcXOgw8PhPg3yvA1Rs8A2XTtwlBc1Uwj0xRATwOfoD6jLC%2Bs3%2BKCgyWsHE4fiYEttqSUKUe1Izhj0QKgWPp9Xi7ADN%2F8wgPjVgIftGv31ILMa0z0K%2BvqeDfmod6jlKVrDN%2FTT79pTgDoSeVW%2BYv8lUQT7F4Z1CIrerYpGJBV49VRyXOlwjW7S%2FPpIjj7EHmxcvWYkoBFm5J1rhTv%2Fa4awLh8i6TchP702rXDWuuIjJEx3&pass_ticket=byG2rMu37cB6NI%2BOvQ9j6Y8bewhDAt7CjbRle4d5GztzatrbtkcphSIcvLql03nT&wx_header=3']
df0 = pd.DataFrame(url_lis,columns=['link'])
target_urls = df0 
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


df0.to_csv('WithToken\{}.csv'.format('test0'),encoding='utf-8',index=None)
print('>>> MISSION ACCOMPLISHED')
print(mistake_url)


