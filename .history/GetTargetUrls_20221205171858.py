# -*- coding: utf-8 -*-
import requests
import time
import csv
import pandas as pd
import random

import time
print(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()))

'''
日期：
    2022/10-11
功能：
    获得目标公众号所有文章的链接
    登录自己的微信公众平台网页版，打开草稿箱，选择文字加入超链接，选择目标公众号，获得包，取token等数据
    需要更新的数据：
        fakeid    公众号唯一身份标识  开发射工具-网络-载荷
        token
        Cookie
参考文章：
    https://blog.csdn.net/jingyoushui/article/details/100109164
    CSDN博主「静幽水1」
'''


# 在这里更新请求头
# 在这里更新请求头
# 在这里更新请求头


def GetTargetUrls(Cookie, token, fakeid, account_name, sleep_time=3, start_page=0,post_count=0):
    # 目标url
    url = "https://mp.weixin.qq.com/cgi-bin/appmsg"

    # 使用Cookie，跳过登陆操作
    headers = {
        "Cookie": Cookie,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35",
    }

    # 构造请求头
    data = {
        "token": token,
        "lang": "zh_CN",
        "f": "json",
        "ajax": "1",
        "action": "list_ex",
        "begin": "0",
        "count": "5",
        "query": "",
        "fakeid": fakeid,  # 填写目标公众号的fakeid(公众号唯一标识)
        "type": "9",
    }

    content_list = []
    mistake = 0

    data["begin"] = 1 * 5
    content_json = requests.get(url, headers=headers, params=data).json()
    time.sleep(2 + random.random() * 2)
    # 获得总条目数量，每爬取一个条目，进行计数，条目够大后break
    content_json_pages = content_json['app_msg_cnt'] #一共有多少次推送

    print('正在处理公众号：{}\n推送数量：{}'.format(account_name, content_json_pages))
    post_count = post_count
    item_count = 0
    # post_count += start_page

    f0 = open('temp_{}.csv'.format(account_name),'w',encoding='utf-8',newline='')
    temp_writer = csv.writer(f0)

    for i in range(500):
        try:
            i += start_page
            if i == 696:
                break
            data["begin"] = i * 5
            time.sleep(sleep_time + random.random() * 10)  # 我不信睡十秒钟还被限制访问 2022.22.15睡200+秒
            # 使用get方法进行提交
            content_json = requests.get(url, headers=headers, params=data).json()
            if len(str(content_json)) > 150:
                print(str(content_json)[:150])
            else:
                print(content_json)
            # 返回了一个json，里面是每一页的数据
            # print(content_json)
            for item in content_json["app_msg_list"]:
                # 提取每页文章的标题及对应的url 填入DF
                items = []
                items.append(item["title"])
                items.append(item["link"])
                content_list.append(items)
                url0 = item["link"]
                url_lis = url0.split('&')
                post_index0 = int(url_lis[2][4:])
                item_count += 1
                if post_index0 == 1:
                    post_count += 1
                print(items)
                temp_writer.writerow(item["title"] + ',' +  item["link"])
            print('已经爬取{}页，{}条，{}次推送，剩余推送{}次'.format(i+1, item_count, post_count, content_json_pages - post_count))

            if post_count >= content_json_pages:
                print('正常完成公众号，跳出循环')
                break

            if content_json_pages - post_count <= 1:
                print('正常完成公众号，跳出循环')
                break
            #if len(content_json["app_msg_list"]) == 0:
             #   print('url返回msg_list为空，可能已经完成')


        except:
            print("程序出错，数据正在保存")
            print("出错信息如下：")
            content_json = requests.get(url, headers=headers, params=data).json()
            print(content_json)
            name = ['title', 'link']
            test = pd.DataFrame(columns=name, data=content_list)
            test.to_csv("TargetUrls\{}.csv".format(account_name), mode='w', encoding='utf-8')
            print(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()))
            print("保存成功")
            mistake = 1
            break

    if mistake == 0:
        print("程序运行未出错")
        name = ['title', 'link']
        test = pd.DataFrame(columns=name, data=content_list)
        test.to_csv("TargetUrls\{}.csv".format(account_name), mode='w', encoding='utf-8')
        print(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()))
        print("保存成功")



if __name__ == '__main__':
    Cookie = 'appmsglist_action_3909106468=card; appmsglist_action_3888765809=card; ua_id=qgQSOwwPYk6QNmhLAAAAADFui5MyU1nHfqiejgcJL_M=; mm_lang=zh_CN; ptui_loginuin=1306994173; RK=70epH0ERNU; ptcz=f2443493d205a388bd0061df132f40252aad3fc2d9b223a9f36a961fecfe1b45; pgv_pvid=4490214787; o_cookie=1306994173; pac_uid=1_1306994173; noticeLoginFlag=1; remember_acct=lisiyuansven%40foxmail.com; rewardsn=; wxtokenkey=777; _clck=3888765809|1|f66|0; wwapp.vid=; wwapp.cst=; wwapp.deviceid=; uuid=e26279f4edf700b34e08ccb13904d404; rand_info=CAESIDAQHGQs39LDMOtCa4JU++mwNiltWNBZBAcr0VkrFgf0; slave_bizuin=3888765809; data_bizuin=3888765809; bizuin=3888765809; data_ticket=ISD5OLYi8h+P757Sh87mnndAdP0uwyGTv3jytsv47PjAHUCEoCx5xe4kKKfe/bKb; slave_sid=ZjFkTEFwTzFhVEpYaGl2aUZWUU9EeXMzb013Z0dCZE8yUlQyMUdsRTZ5TFR0dUpwcVRqNXdJTjlfVlkxdlhkZVNlVFhtY3BHeURhd3lDTTZaOVNnQmhoeV8wQkUyZU5ueDBJR0xSc0xqT1FtbzdWUzFHcVA4YTR3cUxub0JwZUhueW1tdDMxRjNXUHE0S01q; slave_user=gh_6cae14a1a432; xid=4f4f7d02546b896fe39adaa68fdd0399'
    token = '285913115'
    fakeid = 'MzA5MjkwNDUyOA=='
    account_name = '东南学术1'
    sleep_time = 3
    start_page = 0
    GetTargetUrls(Cookie, token, fakeid, account_name, sleep_time=3, start_page=0)
