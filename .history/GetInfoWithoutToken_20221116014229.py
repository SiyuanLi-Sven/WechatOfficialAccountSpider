from cmath import nan
from mimetypes import init
import pandas as pd
import random
import numpy as np
import requests
import time
from bs4 import BeautifulSoup as bs


user_agent = [
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
    "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
    "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
    "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
    "UCWEB7.0.2.37/28/999",
    "NOKIA5700/ UCWEB7.0.2.37/28/999",
    "Openwave/ UCWEB7.0.2.37/28/999",
    "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
]

date = np.nan
have_chaolianjie = np.nan
have_cankaolaiyuan = np.nan
have_tupian1yinpin1shipin = np.nan
is_origin = np.nan

def get_date(html):
    global js_article
    bs_obj = bs(html,"html.parser")
    js_article = bs_obj.find('div', id='js_article').get_text()
    timestamp = int(html.split('ct = "')[1].split('";')[0].strip())
    ymd = time.localtime(timestamp)
    date = "{}-{}-{}".format(ymd.tm_year, ymd.tm_mon, ymd.tm_mday)
    return date


def have_newmedia(html):
    global js_article
    if 'xiumi' or 'powered by' or 'inline-block' or 'border-width' in js_article:
        return 1
    else:
        return 0


def get_chaolianjie(html):
    global js_article
    if 'js_view_source' in js_article:
        have_chaolianjie = 1
    else:
        have_chaolianjie = 0
    return have_chaolianjie


def get_tupian1yinpin1shipin(html):
    global js_article
    if 'img' or 'wxw_wechannel_video_context' or 'db music_card' or 'wx_video_play_opr'in js_article:
        tupian1yinpin1shipin = 1
    else:
        tupian1yinpin1shipin = 0
    return tupian1yinpin1shipin


def get_origin(html):
    if 'copyright_logo' in html:
        is_origin = 1
    else:
        is_origin = 0
    return is_origin



def GetInfoWithoutToken(account_name):
    '''
    参数:
        account_name 公众号名称，以数据说明文件为准
    功能：
        读取每个文章的不需要微信浏览器token就能读取的数据（日期、是否原创、是否有“阅读原文”链接、是否有图片or音频or视频）
        本函数输入account_name公众号名称后，读取根目录\TargetUrls\account_name.csv文件
        对该文件中的每个地址，读取相应的date、have_chaolianjie、have_tupian1yinpin1shipin、is_origin数据
        将结果写入根目录\WithoutToken\account_name.csv
    '''
    random.seed()
    df0 = pd.read_csv(r'TargetUrls\{}.csv'.format(account_name),encoding='utf-8')
    target_urls = df0['link']
    print(df0)

    count = 0
    wrong_urls = []
    for index,row in df0.iterrows():
        # try:
        time.sleep(random.random())
        headers = {'User-Agent': random.choice(user_agent)}
        count += 1

        url = row['link']
        print(url)

        # 拆分url，读取index信息
        # url大概长这样：http://mp.weixin.qq.com/s?__biz=MzA3ODk5NTAzNA==&mid=2652167532&idx=1&sn=6767fa09c596b6b69bcc736e06de57e9&chksm=845a3659b32dbf4ffdc75b9b514bbf8538f71e29431cf63c4b77c223b5cd4635d75f4aede403#rd
        # 我们按照&给split开，得到['http://mp.weixin.qq.com/s?__biz=MzA3ODk5NTAzNA==','mid=2652167532','idx=1','sn=6767fa09c596b6......]
        url_lis = url.split('&')
        df0.loc[index,'post_index'] = url_lis[2][4:]

        response = requests.get(url, headers=headers) # 开始请求url，获取并解析html
        html = response.text
        if df0.loc[index,'title'][-1] == '?':
            df0.loc[index,'title'] = df0.loc[index,'title'].strip('?')
        df0.loc[index,'date'] = get_date(html)
        df0.loc[index,'have_chaolianjie'] = get_chaolianjie(html)
        df0.loc[index,'have_newmedia'] = have_newmedia(html)
        df0.loc[index,'have_tupian1yinpin1shipin'] = get_tupian1yinpin1shipin(html)
        df0.loc[index,'is_origin'] = get_origin(html)
        print(df0.loc[index])
        print('已完成{}行,剩余{}行，完成度{}'.format(count,len(df0)-count,count/len(df0)))
        '''        except:
        if df0.loc[index,'title'][-1] == '?':
            df0.loc[index,'title'] = df0.loc[index,'title'].strip('?')
        df0.loc[index,'title'] = df0.loc[index,'title']
        df0.loc[index,'link'] = df0.loc[index,'link']
        df0.loc[index,'date'] = np.nan
        df0.loc[index,'have_chaolianjie'] = np.nan
        df0.loc[index,'have_tupian1yinpin1shipin'] = np.nan
        df0.loc[index,'is_origin'] = np.nan
        wrong_urls.append(url)
        print('###################\n###################\n###################\n出错url:' + url)'''

    df0.to_csv('WithoutToken\{}.csv'.format(account_name),encoding='utf-8',index=None)
    print(wrong_urls)


if __name__ == '__main__':
    print('haha')
    GetInfoWithoutToken('东岳论丛short2')