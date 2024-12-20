# 微信公众号爬虫项目

note: All csv files use utf-8-sig encoding

## 0. Reference
This project is an application of the GitHub project [wechat_articles_spider](https://github.com/wnma3mz/wechat_articles_spider). 

## 1. Approach
This crawler project aims to obtain all article content from dozens of public accounts over the past few years and extract relevant data (title, link, release date, whether hyperlinks are used, whether reference links are used, whether there are images, audio, video, whether it is original, reading volume, viewing volume, likes, number of selected comments, comment content, number of author replies, number of likes for author replies). The specific data names and explanations can be founnd in the **A Data Explanation.xlsx** file.

To get article data, you first need to get the link to the article. Links to WeChat public account posts are not easy to obtain. Common practices are to search through the Sogou browser or select links to other articles from the WeChat public platform editing interface. This project uses the latter and implements this function with **GetTargetUrls.py**. This script takes a single public account as a unit, and saves all article titles and links obtained from a specific public account in the form of a csv file in the **root directory/TargetUrls** folder. The acquisition of token and cookie can refer to [this article](https://github.com/wnma3mz/wechat_articles_spider/blob/master/docs/get_cookie_token.md)

After obtaining the article link, we obtain the corresponding html file through the link and parse the file to get the data we need. This project divides the data into two categories, one is visible to ordinary browsers, we call it **InfoWithoutToken** (release date, whether hyperlinks are used, whether reference links are used, whether there are images, audio, video, whether it is original), and the other type of data is not visible to ordinary browsers, and needs to be visible through the WeChat PC client's own browser, we call it **InfoWithToken** (reading volume, viewing volume, likes, number of selected comments, comment content, number of author replies, number of likes for author replies). We crawl these two types of data in stages.

We use **GetInfoWithoutToken.py** to crawl InfoWithoutToken class data and analyze it. This script reads files from **root directory/TargetUrls** and saves the results in the **root directory/WithoutToken** folder.

We use **GetInfoWithToken.py** to crawl InfoWithToken class data and analyze it. This script reads files from **root directory/WithoutToken** and saves the results in the **root directory/WithToken** folder. The token and cookie data used by this script need to open the WeChat PC client, select not to open links with the default browser in the settings, open links with the WeChat client's own browser and capture packets. Related operations can refer to [this article](https://github.com/wnma3mz/wechat_articles_spider/blob/master/docs/get_appmsg_token.md)


note: 所有csv文件采用utf-8-sig编码

## 0.参考
本项目是对GitHub项目[wechat_articles_spider](https://github.com/wnma3mz/wechat_articles_spider)的改写与运用。

## 1.思路
这个爬虫项目希望获得数十个公众号在过去数年中的所有文章内容并提取相关数据（题目、链接、发布日期、是否使用超链接、是否使用参考链接、是否有图片1音频1视频、是否原创、阅读量、在看量、点赞量、精选留言条数、留言内容、作者回复数量、作者回复获赞数），具体的数据名称及解释可以在**A 数据说明.xlsx**文件中找到。

想要获得文章数据，首先就要得到文章的链接。微信公众号推文的链接不容易获得，常见的做法是通过搜狗浏览器的检索或者微信公众平台编辑界面选择链接到其他文章。本项目采用后者，并用**GetTargetUrls.py**实现这一功能。这一脚本以单个公众号为单位，将爬取得到的特定公众号的全部文章标题、链接以csv文件的形式保存在**根目录/TargetUrls**文件夹中。touken和cookie的获取可以参考[这篇文章](https://github.com/wnma3mz/wechat_articles_spider/blob/master/docs/get_cookie_token.md)

得到文章链接后，我们通过链接获得相应html文件，并解析文件获得我们需要的数据。本项目将数据分为两类，一类为普通浏览器可见的，我们将其称为**InfoWithoutToken**（发布日期、是否使用超链接、是否使用参考链接、是否有图片1音频1视频、是否原创），另一类数据为普通浏览器不可见，需要通过微信PC端自带浏览器才可见的，我们将其称为**InfoWithToken**（阅读量、在看量、点赞量、精选留言条数、留言内容、作者回复数量、作者回复获赞数）。我们分阶段地爬取这两类数据。

我们通过**GetInfoWithoutToken.py**爬取InfoWithoutToken类数据并进行分析，这个脚本从**根目录/TargetUrls**读取文件，将结果保存在**根目录/WithoutToken**文件夹中。

我们通过**GetInfoWithToken.py**爬取InfoWithToken类数据并进行分析，这个脚本从**根目录/WithoutToken**读取文件，将结果保存在**根目录/WithToken**文件夹中。这个脚本采用的token和cookie等数据需要打开微信PC客户端，设置中选择不以默认浏览器打开链接，以微信客户端自带浏览器打开链接并抓包。相关操作可以参考[这篇文章](https://github.com/wnma3mz/wechat_articles_spider/blob/master/docs/get_appmsg_token.md)


