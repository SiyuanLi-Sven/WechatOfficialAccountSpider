# coding: utf-8
import os
from pprint import pprint
from wechatarticles import ArticlesInfo

if __name__ == "__main__":
    # 登录微信PC端获取文章信息
    appmsg_token = r'1189_rq49Bs%2FC8eVr9E1VqQSJJw-SZi4xO44QVDM4QsJ6rkm6FmM88fo1MQ_xMgDXJ10AWRlu_ft80oj1J_eb'
    cookie = r"rewardsn=; wxtokenkey=777; wxuin=2817795206; devicetype=Windows10x64; version=6307001d; lang=zh_CN; pass_ticket=NK1pxhfehoNBO62nx2VDi1tp5dJbVb0SrszQOE/2pVgChhCjTqYqJU5qQUqzsDhQ; appmsg_token=1189_rq49Bs%2FC8eVr9E1VqQSJJw-SZi4xO44QVDM4QsJ6rkm6FmM88fo1MQ_xMgDXJ10AWRlu_ft80oj1J_eb; wap_sid2=CIbJ0L8KEooBeV9ISjZjQ2dIZTZkNjdaUGhDdzR6UlhxeFNNTXo2aUtOMlV5a2RINUNpV3pvS3NvU0s3bjZLcV9PMnBMdUpGS2FpUDB2ZGhWMVhmUVpCcXJBM3RlRlFWdUpkUU1VUW84UFJjRVJMbkJMNnJiLXRJa1AySDRpa1RpbXpBd3llM2RvRmFvTVNBQUF+MJTf+JoGOA1AAQ=="
    article_url = "https://mp.weixin.qq.com/s?__biz=MjM5MjA4MjA4MA==&mid=2655053235&idx=1&sn=0704b906196f08a0f345f83c605c9283&chksm=bd1ff47c8a687d6aae2232d81c48835008804f69b7cd47e123359e3c1579a122721bdfb1fe28&mpshare=1&srcid=1030YzsoalrSYSuPu5NyEWOl&sharer_sharetime=1667116824567&sharer_shareid=9146a9f02c85bcb20b760eb3fefb7e86&from=singlemessage&scene=1&subscene=10000&clicktime=1667116830&enterid=1667116830&ascene=1&devicetype=android-29&version=28000f3d&nettype=WIFI&abtest_cookie=AAACAA%3D%3D&lang=zh_CN&exportkey=n_ChQIAhIQJSGVUpHTpgmykShtx381jBLvAQIE97dBBAEAAAAAAC%2F8FmMYLB0AAAAOpnltbLcz9gKNyK89dVj0THPV07XEvv1JT%2FHpfDphLksoZJG6WvB6%2B7QWyptUs4vcpBJ5HvgF14Yvv3yOQX26i0Zy6cwD12QL7iN1NeBrM%2Fd1tk%2B5oxBncFyyYHuF1FIkuT87HlKaH0%2Fhtsqe6ymOYV1nOlri%2FR7qRcd7xssxzxPEZXgnNt6pD5vkg9sqVoUjiorH8dp9o45Iw14ztWhtctUN1OF2PZYK%2B4OFj73moieOHfr7h9mfjyZ%2FFLuGQm9ex09%2BlCmWfUsalc6HEcnDKc9xjIV53z6w&pass_ticket=ftrovc9LuK63sKUoaDGURQiqd%2FJDHNUno7Lto362UVSob8CM%2FGnGmYcu5v7dFJ6c&wx_header=3"
    test = ArticlesInfo(appmsg_token, cookie)
    print(test)
    print(1)
    comments = test.comments(article_url)
    read_num, like_num, old_like_num = test.read_like_nums(article_url)
    print("comments:")
    pprint(comments)
    print("read_like_num:", read_num, like_num, old_like_num)


'''
第三步：登录PC微信客户端，通过微信客户端自带的浏览器打开任意一篇公众号的文章。
第四步：如果上述步骤都正确，应该可以在fiddler里看到这个url： **https://mp.weixin.qq.com/mp/getappmsgext**。
然后点开这个链接。fiddler右侧webForms选项里有appmsg_token 参数的值，
点raw选项可以找到cookie参数的值。 
将这两个值带入test_WechatInfo.py文件，就能抓取到数据。
'''