import GetTargetUrls
import pandas as pd
import time

Cookie = 'appmsglist_action_3909106468=card; appmsglist_action_3888765809=card; appmsglist_action_3939421254=card; appmsglist_action_3867712421=card; appmsglist_action_3870777659=card; appmsglist_action_3940423674=card; appmsglist_action_3873514537=card; ua_id=qgQSOwwPYk6QNmhLAAAAADFui5MyU1nHfqiejgcJL_M=; mm_lang=zh_CN; ptui_loginuin=1306994173; RK=70epH0ERNU; ptcz=f2443493d205a388bd0061df132f40252aad3fc2d9b223a9f36a961fecfe1b45; pgv_pvid=4490214787; o_cookie=1306994173; pac_uid=1_1306994173; noticeLoginFlag=1; remember_acct=lisiyuansven%40foxmail.com; iip=0; fqm_pvqid=938a7635-027c-4ab1-adf2-8e70fbf73adb; rewardsn=; wxtokenkey=777; wwapp.vid=; wwapp.cst=; wwapp.deviceid=; uin=o1306994173; skey=@EW743pE72; uuid=767b813b7f1f601cc6a00076541445c3; rand_info=CAESICZwGXEdAxktQwdDymZD1bGnYvyhX2RorziHMYw+aXa9; slave_bizuin=3939421254; data_bizuin=3939421254; bizuin=3939421254; data_ticket=1pEwoHH9SEJnRasDdU/bS9TOvAcwZQS+LvKcfYLfWGVJR0V41uW0qhSAOxK87N+i; slave_sid=T2tUVDJIZVhrQjNQRDNEVDBpN1UwRlhQTjBfWldOaGRvdENpcEs0NzhxVTM2RW1Zd19ZR1VLTElwaF9wQUpwNmVQZTBLdmZubkRJTTNtbkhQWHh4eDhCS3JqY3pCZzFLM3hpdWNfM1EzSU5icko4Z29GQ1VZZkpmZ1lWeU1Dc3hMMVh4ajBWeUZ5ZUlnQ0pr; slave_user=gh_bc61089a9399; xid=a39386197b498735fb6679980e3d8d50; _clck=3939421254|1|f6v|0'
token = '1025955981'

lis0 = [
    # '东岳论丛',
    # '读书杂志',
    # '福建社会科学院福建论坛杂志2',que
    # '甘肃社会科学',
    # '广东社会科学',
    # '贵州社会科学',
    # '国外社会科学',
    # '河北学刊',
    # '江海学刊',
    # '江汉论坛',
    # '江淮论坛杂志社',
    # '江苏社会科学',
    # '江西社会科学',
    # '开放时代',
    # '南京社会科学',
    # '内蒙古社会科学',
    # '思想战线（思想战线THINKING）',
    # '探索与争鸣（探索与争鸣杂志）',
    # '天津社会科学',
    # '文化纵横',
    # '文史哲（文史哲杂志）',
    # '新疆社会科学（新疆社会科学杂志社）',
    # '学海（学海杂志）',
    # '学术界（学术界杂志社）',
    # '学术论坛（学术论坛杂志社）',
    # '学术研究'
    ######
    # '广西社会科学（广西社会科学杂志社）',
    # '河南社会科学',
    # '湖北社会科学（湖北社会科学杂志）',
    # '湖南社会科学（湖南省社会科学院）',
    # '兰州学刊',
    # '理论月刊',
    # '社会科学家（社会科学家杂志社）',
    # '天府新论'
    ###疑难杂症部分
    # '开放时代',
    # '探索与争鸣3',
    # '文化纵横3'
    ### C_Plus
    #'广西社会科学',
    #'河南社会科学',
    #'湖北社会科学',
    #'湖南社会科学',
    #'兰州学刊',
    #'理论月刊',
    #'社会科学家',
    #'天府新论',
    #####
    #'探索与争鸣b',
    #'学术月刊b',
    #'云南社会科学b',
    '中国社会科学b3'
]

lis1 = [
    # 'MzI4MTY1NzQ3MQ==',
    # 'MzA3ODk5NTAzNA==',
    # 'MzI5Mzk3NTEyMw==',
    # 'MzAxNjkyMTQ3MQ==',
    # 'MzkyNTM5NDE5MA==',
    # 'MzIzNDY5MTM4Nw==',
    # 'MzAwNDYzNzAwNw==',
    # 'MzIzOTQ4Nzg4Ng==',
    # 'MzI0NTA2NjIxOQ==',
    # 'MzkzMTE5NzMxMQ==',
    # 'MzkyMDE5MTA4NQ==',
    # 'MzI3OTQxNDQ2Mg==',
    # 'MzIwMDUwNjY3Mg==',
    # 'MzA4Mjg3MTYyMA==',
    # 'MzIzNzcxNjM5Mg==',
    # 'MzAwMzQyMDk2Ng==',
    # 'MzIxNDE2OTYyOA==',
    # 'MzA4MjcxMDEwNQ==',
    # 'MzUzNjg4OTU0NQ==',
    # 'MzA5MjM2NDcwMg==',
    # 'MzAwNzM4MjQ0Mw==',
    # 'MzkxNDE5Mjk1Ng==',
    # 'MzAwNzU3OTQwMw==',
    # 'MzIwOTAyNzcwMQ==',
    # 'MzU0MTY1NDUzNQ==',
    # 'MjM5NzU4NTU4NA=='
    #####
    # 'MzIwNTEwNzUzOQ==',
    # 'MzI4Mjc4MzIzNA==',
    # 'MzI0MDc4ODcxMg==',
    # 'Mzg2MzU2MzI0Nw==',
    # 'Mzg5NjY1NjIxMg==',
    # 'Mzg2NTA0MDE5OQ==',
    # 'MzA5NTkyNzkwMg==',
    # 'MzI0MjEwODA0Ng=='
    ##### 疑难杂症部分
    # 'MzA4Mjg3MTYyMA==',
    # 'MzA4MjcxMDEwNQ==',
    # 'MzA5MjM2NDcwMg=='
    #'MzIwNTEwNzUzOQ==',
    #'MzI4Mjc4MzIzNA==',
    #'MzI0MDc4ODcxMg==',
    #'Mzg2MzU2MzI0Nw==',
    #'Mzg5NjY1NjIxMg==',
    #'Mzg2NTA0MDE5OQ==',
    #'MzA5NTkyNzkwMg==',
    #'MzI0MjEwODA0Ng=='
    ###
    #'MzA4MjcxMDEwNQ==',
    #'MzA5NTk5ODQwOQ==',
    #'MzU3NDQzNTY4Ng==',
    'MzA4NDUwMjMxNA=='

]

lis_startPpage = [
    #278,
    #157,
    #200,
    687
]

lis_post_count = [
    #138,
    #784,
    #994,
    3914
]

columns = ['account_name', 'fakeid', 'start_page', 'post_count']

todf = [lis0, lis1, lis_startPpage, lis_post_count]
df0 = pd.DataFrame(todf)
df0 = df0.T
df0.columns = columns
print(df0)

for index, row in df0.iterrows():
    print(row)
    fakeid = row['fakeid']
    account_name = row['account_name']
    sleep_time = 204
    start_page = row['start_page']
    post_count = row['post_count']

    GetTargetUrls.GetTargetUrls(Cookie, token, fakeid, account_name=account_name, sleep_time=sleep_time, start_page=start_page, post_count=post_count)
