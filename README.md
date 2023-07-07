# 微信公众号爬虫项目

维护：李思远 20327077 SYSU Lingnan College
Email：lisiyuansven@foxmail.com
QQ：13660736050

所有csv文件采用utf-8-sig编码

##0.参考
本项目在很大程度上是对GitHub项目[wechat_articles_spider](https://github.com/wnma3mz/wechat_articles_spider)的改写与运用，大部分技术性问题均参考自该项目。

##1.思路
这个爬虫项目希望获得数十个公众号在过去数年中的所有文章内容并提取相关数据（题目、链接、发布日期、是否使用超链接、是否使用参考链接、是否有图片1音频1视频、是否原创、阅读量、在看量、点赞量、精选留言条数、留言内容、作者回复数量、作者回复获赞数），具体的数据名称及解释可以在**A 数据说明.xlsx**文件中找到。

想要获得文章数据，首先就要得到文章的链接。微信公众号推文的链接不容易获得，常见的做法是通过搜狗浏览器的检索或者微信公众平台编辑界面选择链接到其他文章。本项目采用后者，并用**GetTargetUrls.py**实现这一功能。这一脚本以单个公众号为单位，将爬取得到的特定公众号的全部文章标题、链接以csv文件的形式保存在**根目录/TargetUrls**文件夹中。touken和cookie的获取可以参考[这篇文章](https://github.com/wnma3mz/wechat_articles_spider/blob/master/docs/get_cookie_token.md)

得到文章链接后，我们通过链接获得相应html文件，并解析文件获得我们需要的数据。本项目将数据分为两类，一类为普通浏览器可见的，我们将其称为**InfoWithoutToken**（发布日期、是否使用超链接、是否使用参考链接、是否有图片1音频1视频、是否原创），另一类数据为普通浏览器不可见，需要通过微信PC端自带浏览器才可见的，我们将其称为**InfoWithToken**（阅读量、在看量、点赞量、精选留言条数、留言内容、作者回复数量、作者回复获赞数）。我们分阶段地爬取这两类数据。

我们通过**GetInfoWithoutToken.py**爬取InfoWithoutToken类数据并进行分析，这个脚本从**根目录/TargetUrls**读取文件，将结果保存在**根目录/WithoutToken**文件夹中。

我们通过**GetInfoWithToken.py**爬取InfoWithToken类数据并进行分析，这个脚本从**根目录/WithoutToken**读取文件，将结果保存在**根目录/WithToken**文件夹中。这个脚本采用的token和cookie等数据需要打开微信PC客户端，设置中选择不以默认浏览器打开链接，以微信客户端自带浏览器打开链接并抓包。相关操作可以参考[这篇文章](https://github.com/wnma3mz/wechat_articles_spider/blob/master/docs/get_appmsg_token.md)

