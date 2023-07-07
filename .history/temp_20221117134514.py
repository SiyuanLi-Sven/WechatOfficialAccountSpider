import pandas as pd
import random
import numpy as np
import requests
import time
from bs4 import BeautifulSoup
import os
from wechatarticles import ArticlesInfo

appmsg_token = r'1192_NQVVP1oE2QkkBSGcmDH-DO0tLGI4y0GmvBRiz6dximm7O_vVUDhRFxsHGPeavu3Z5jXqxEwAnmFVVpfx'
appmsg_token = r'1192_cAN4DZgBvvxDqkuX6y6f61iTbgHtACh-Esg94t3HGs5IYRPqOXNNTJs7HA0Jb6pOYv0qDcIZpNTqRmig'
#                1192_nnnTc3EonZVQjssFmDH-DO0tLGI4y0GmvBRiz4oKMCh_lUDLG-71jVvz7h8yaU0XwxUfoSPUT9GV2dmk
cookie = r"rewardsn=; wxtokenkey=777; wxuin=2817795206; devicetype=Windows10x64; version=6307001d; lang=zh_CN; appmsg_token=1192_NQVVP1oE2QkkBSGcmDH-DO0tLGI4y0GmvBRiz6dximm7O_vVUDhRFxsHGPeavu3Z5jXqxEwAnmFVVpfx; pass_ticket=b8WWdGYkUNuOMRpz3U4Q6+59lp5ToL03jcUZJfVah4XXm3FEwpvj1oGlfrSIJ94+; wap_sid2=CIbJ0L8KErYBeV9IRml0MDc1bGFHSEw5anFzYVd0MWswY3J1elkxeG1QX1NETC1GOEtVeXF2TzNndXl4X0w2X1pVLXNJQ2pSRkREWHFVdF80WmJPdWVrOGk0bXhjWDhPaWJaVGdwNWFNVXQ4SUZWemxzWTdpRGo3OXBLb01sekdlS2QwV2V1QU9pSmgxZlFSQmlLOF80WEQwV0ZwU0FaMDc4eVRaVXRESUlMRi04N0RQb2F6TTBEaFJJQUFBfn4wuPHTmwY4DUAB"
cookie = r'rewardsn=;wxtokenkey=777;wxuin=2817795206;devicetype=Windows10x64;version=6307001d;lang=zh_CN;appmsg_token=1192_cAN4DZgBvvxDqkuX6y6f61iTbgHtACh-Esg94t3HGs5IYRPqOXNNTJs7HA0Jb6pOYv0qDcIZpNTqRmig;pass_ticket=b8WWdGYkUNuOMRpz3U4Q6+59lp5ToL03jcUZJfVah4VvKNvNzgSWocIo9FqT/ZYb;wap_sid2=CIbJ0L8KEp4BeV9ISzAzRWlTYVlCbGdpX0dCazl0R3FFdmFkNjBDT0h6MjhtVmhhTXp1cVk2ZmcySmtkMFJuUzJVRWJCX0lEVU9KS1FlNFBKaHFpaUtDaU9PU2hBaTR5WlhKMFdaMGVVc2FadHZ3YkhOM0dyZWgtbGtKTEZuODlfbjlsdldsbWR2Zmlic05uUFFRcXNEdzh0WU5WdnhSbU1PRkVnQUEwsO/TmwY4DUAB'
#          rewardsn=; wxtokenkey=777; wxuin=2817795206; devicetype=Windows10x64; version=6307001d; lang=zh_CN; appmsg_token=1192_nnnTc3EonZVQjssFmDH-DO0tLGI4y0GmvBRiz4oKMCh_lUDLG-71jVvz7h8yaU0XwxUfoSPUT9GV2dmk; pass_ticket=b8WWdGYkUNuOMRpz3U4Q6+59lp5ToL03jcUZJfVah4UVmvJTbdTRCjucE6dEErV1; wap_sid2=CIbJ0L8KErYBeV9ITHZUR0x0RFJTU25SMFhxaXp1eVd3a3NOc1RKbEwtUFNocnA4UDNTd2lSZVhKakxTaVFwak85aU9ZMUt0dWM5RV8tb3NTRWFTWDNsczRWYjF5MDc4RDVjQTczSm0zd0RIV0ZidG11dnZBNDRya2NjZy0wUEQ5bFpIUVo2NHFyRDNqQ2g5SEV2WGNLSWlzaWJyeFJ4Z3c4T1VtUVE5dVB5Wk9oUWVvRm80aVNVaFJJQUFBfn4wkpPXmwY4DUAB
url_lis = ['http://mp.weixin.qq.com/s?__biz=MzUzNjg4OTU0NQ==&mid=2247485264&idx=1&sn=10004f06df62137d8439846aa55f3b90&chksm=faee16f6cd999fe07ac2f81127ee12d17138db18c29bc4413131222ac4d4c79d43bb06a5d46d#rd']
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
        #article_url = 'http://mp.weixin.qq.com/s?__biz=MzIxODM4NTgxOQ==&mid=2247489003&idx=3&sn=c4661c3e84f3a56391736d52e1f65ec2&chksm=97ea091fa09d8009bd7b0fbf573b7cfe1691cc9149e0ac78a48d893a9b6f273e725fb8909737&token=2048984886&lang=zh_CN#rd'
        article_url = 'http://mp.weixin.qq.com/s?__biz=MzI4MTY1NzQ3MQ==&mid=2247484727&idx=1&sn=104f7efd62d9c9180cefb022e03d1134&chksm=eba4ac27dcd325311abfd22740197e87f1ee13a8b2fb1cc2aca13d60086e043b27745085ef15#rd'
        test = ArticlesInfo(appmsg_token, cookie)
        comments = test.comments(article_url)
        print(comments)
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

        if len(comments['elected_comment']) > 0:
            for i in comments['elected_comment']:
                print(i)
                lis_content.append(i['content'])
                lis_like_num.append(str(i['like_num']))
                if i.__contains__('reply_new') and i['reply_new'].__contains__('reply_list'):
                    if i['reply_new']['reply_list'] != []:
                        lis_auther_reply.append(i['reply_new']['reply_list'][0]['content'])
                        lis_auther_like_num.append(str(i['reply_new']['reply_list'][0]['reply_like_num']))
                    else:
                        lis_auther_reply.append('nan')
                        lis_auther_like_num.append('nan')
        
        print(lis_content)
        print(lis_like_num)
        print(lis_auther_reply)
        print(lis_auther_like_num)

        df0.loc[index,'lis_content'] = '☀'.join(lis_content)
        df0.loc[index,'lis_content_like_num'] = '☀'.join(lis_like_num)
        df0.loc[index,'lis_auther_reply'] = '☀'.join(lis_auther_reply)
        df0.loc[index,'lis_auther_like_num'] = '☀'.join(lis_auther_like_num)
        print('已完成：{}\n比例：{}'.format(count,count/len(target_urls)))

    except:
        df0.loc[index,'read_num'] = np.nan
        df0.loc[index,'like_num'] = np.nan
        df0.loc[index,'old_like_num'] = np.nan
        df0.loc[index,'content'] = np.nan
        df0.loc[index,'like_num'] = np.nan
        mistake_url.append(article_url)
        raise



df0.to_csv('WithToken\{}.csv'.format('test0'),encoding='utf-8',index=None)
print('>>> MISSION ACCOMPLISHED')
print(mistake_url)



