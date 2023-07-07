import GetTargetUrls
import pandas as pd
import time

Cookie = 'appmsglist_action_3909106468=card; ua_id=qgQSOwwPYk6QNmhLAAAAADFui5MyU1nHfqiejgcJL_M=; mm_lang=zh_CN; ptui_loginuin=1306994173; RK=70epH0ERNU; ptcz=f2443493d205a388bd0061df132f40252aad3fc2d9b223a9f36a961fecfe1b45; pgv_pvid=4490214787; o_cookie=1306994173; pac_uid=1_1306994173; iip=0; fqm_pvqid=938a7635-027c-4ab1-adf2-8e70fbf73adb; _clck=3909106468|1|f75|0; _tc_unionid=47d1db9a-65c4-4043-8713-73b25a31b3f5; pgv_info=ssid=s7041499480; rewardsn=; wxtokenkey=777; uin=o1306994173; uuid=6d6c8e48be9539845c4436d06996ad4e; wxuin=77219168643508; rand_info=CAESIMZOD+bbSGdyH/mBZsaIP2K256OqTpTz2RvJi9lh8wLF; slave_bizuin=3909106468; data_bizuin=3909106468; bizuin=3909106468; data_ticket=HhSfxAHDY/4/P7mbRPN+YaEyA5AmsG85yhf+fggMJx5+MWReLR95vpZanrJ8TfHG; slave_sid=WWNDemJfRktoUWpLZE1UMnhwMGoyNGNsOWdoVXZkYkU1YXAxWWVIb19YSjJIWkczTlB6djlTd1BlQTkzczhWVWtwOFJlRmRYcFJ0aDVIWjZhdHA1X2Jqb2dhS0E0eGJ0ZlZPOFJ6bmF2S2RCNUpxbXF1bUF1UE45bzBVTVBSeW9MVG93SUtsazNBeUJ6Mmgy; slave_user=gh_b565a45a41c8; xid=ee429dab841af4a0bffa97ac8bdf24c7'
token = '1142406550'

lis0 = [
    '武志宏'
]

lis1 = [
    'MzU2ODI5ODMzNg=='

]

lis_startPpage = [
    0
]

lis_post_count = [
    0
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
    sleep_time = 30
    start_page = row['start_page']
    post_count = row['post_count']

    GetTargetUrls.GetTargetUrls(Cookie, token, fakeid, account_name=account_name, sleep_time=sleep_time, start_page=start_page, post_count=post_count)
