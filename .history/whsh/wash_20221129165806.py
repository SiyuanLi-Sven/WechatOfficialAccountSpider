# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import os
 

def main(account_name='读书杂志'):
    # df0为单公众号原始数据，df1为整理后数据
    # 先读取df0，再生成df1，将数据逐步写入df1
    df0 = pd.read_csv(r'WithToken/fine/{}.csv'.format(account_name))
    df0 = df0.fillna(0)
    print(df0)
    '''[
        'Unnamed: 0', 'title', 'link', 'post_index', 'date', 'have_chaolianjie',
        'have_newmedia', 'have_tupian1yinpin1shipin', 'is_origin', 'read_num',
        'like_num', 'old_like_num', 'lis_content', 'lis_content_like_num',
        'lis_auther_reply', 'lis_auther_like_num','year_month'
    ]'''
    # 在df0上构建year_month方便查找
    for index, row in df0.iterrows():
        if type(row['date']) == float:
            # print(row)
            pass
        else:
            lis_date = row['date'].split('-')[:2]
            date_month = '-'.join(lis_date)
            df0.loc[index, 'year_month'] = date_month
            # print(df0.loc[index])

    df1_lis = []
    for i in range(2017, 2023):
        if i == 2022:
            for j in range(1, 10):
                df1_lis.append([i, j, str(i) + '-' + str(j)])
        else:
            for j in range(1, 13):
                df1_lis.append([i, j, str(i) + '-' + str(j)])
    df1 = pd.DataFrame(df1_lis)
    df1.columns = ['year', 'month', 'year_month']
    df1['account_name'] = account_name
    # print(df1)
    # print(df0.columns)

    for index, row in df1.iterrows():
        if row['year_month'] in df0['year_month'].values:  # 如果这个月有发文
            # 当月发文数量
            df1.loc[index, 'monthly_articles'] = df0['year_month'].value_counts()[row['year_month']]

            # 月发文次数
            df_temp = df0[df0['post_index'] == 1]
            if len(df_temp) != 0 and row['year_month'] in df_temp['year_month'].values:
                df1.loc[index, 'monthly_posts'] = df_temp['year_month'].value_counts()[row['year_month']]
            else:
                df1.loc[index, 'monthly_posts'] = 0

            # 当月阅读量超过1万人次文章数量
            df_temp = df0[df0['read_num'] > 10000]
            if len(df_temp) != 0 and row['year_month'] in df_temp['year_month'].values:
                df1.loc[index, 'monthly_read_10000_more'] = df_temp['year_month'].value_counts()[row['year_month']]
            else:
                df1.loc[index, 'monthly_read_10000_more'] = 0

            # 当月原创文章数量
            df_temp = df0[df0['is_origin'] == 1]
            if len(df_temp) != 0 and row['year_month'] in df_temp['year_month'].values:
                df1.loc[index, 'monthly_articles_origin'] = df_temp['year_month'].value_counts()[row['year_month']]
            else:
                df1.loc[index, 'monthly_articles_origin'] = 0

            # 当月文章是否含超链接（选取当月第一篇文章检验）
            # print(df0[df0['year_month'] == row['year_month']].iloc[0]['have_chaolianjie'])
            df1.loc[index, 'monthly_first_have_chaolianjie'] = df0[df0['year_month'] == row['year_month']].iloc[0][
                'have_chaolianjie']

            # 当月文章是否使用新媒体排版（选取当月第一篇文章检验）
            df1.loc[index, 'monthly_first_have_newmedia'] = df0[df0['year_month'] == row['year_month']].iloc[0][
                'have_newmedia']

            # 当月文章是否含图片、音频或视频（选取当月第一篇文章检验）
            df1.loc[index, 'monthly_first_have_tupian1yinpin1shipin'] = \
                df0[df0['year_month'] == row['year_month']].iloc[0][
                    'have_tupian1yinpin1shipin']

            # 当月文章总在看数
            df_temp = df0[df0['year_month'] == row['year_month']]
            df1.loc[index, 'monthly_likes_sum'] = df_temp['like_num'].sum()

            # 当月文章总点赞数(建议增加)
            df_temp = df0[df0['year_month'] == row['year_month']]
            df1.loc[index, 'monthly_old_likes_sum'] = df_temp['old_like_num'].sum()

            # 当月文章平均在看数
            df_temp = df0[df0['year_month'] == row['year_month']]
            df1.loc[index, 'monthly_likes_mean'] = df_temp['like_num'].mean()

            # 当月文章平均点赞数（建议增加）
            df_temp = df0[df0['year_month'] == row['year_month']]
            df1.loc[index, 'monthly_old_likes_mean'] = df_temp['old_like_num'].mean()

            # 当月头条文章平均在看数
            df_temp = df0[df0['year_month'] == row['year_month']]
            df_temp = df_temp[df_temp['post_index'] == 1]
            df1.loc[index, 'monthly_likes_mean_first_post'] = df_temp['like_num'].mean()

            # 当月头条文章平均点赞数
            df_temp = df0[df0['year_month'] == row['year_month']]
            df_temp = df_temp[df_temp['post_index'] == 1]
            df1.loc[index, 'monthly_old_likes_mean_first_post'] = df_temp['old_like_num'].mean()

            # 当月最大文章在看数
            df1.loc[index, 'monthly_likes_max'] = df0[df0['year_month'] == row['year_month']]['like_num'].max()

            # 当月文章阅读总数
            df1.loc[index, 'monthly_read_sum'] = df0[df0['year_month'] == row['year_month']]['read_num'].sum()

            # 当月文章平均阅读量
            df1.loc[index, 'monthly_read_mean'] = df0[df0['year_month'] == row['year_month']]['read_num'].mean()

            # 当月头条文章平均阅读量
            df_temp = df0[df0['year_month'] == row['year_month']]
            df_temp = df_temp[df_temp['post_index'] == 1]
            df1.loc[index, 'monthly_read_first_post'] = df_temp['like_num'].mean()

            # 当月最大文章阅读量
            df1.loc[index, 'monthly_read_max'] = df0[df0['year_month'] == row['year_month']]['read_num'].max()

            # 当月留言区开通情况
            # 与认证情况相同。认证后的账号都拥有留言区功能。

            # 当月精选留言条数
            df_temp = df0[df0['year_month'] == row['year_month']]
            df1.loc[index, 'monthly_content_num'] = 0
            if 'lis_content' in df_temp.columns:
                for i in df_temp['lis_content']:
                    if type(i) == float:
                        df1.loc[index, 'monthly_content_num'] += 0
                    elif '☀' in i:
                        df1.loc[index, 'monthly_content_num'] += len(i.split('☀')) - i.count('nan') - i.count('0')
                    else:
                        df1.loc[index, 'monthly_content_num'] += 1

                # 当月精选留言作者回复数
                df_temp = df0[df0['year_month'] == row['year_month']]
                df1.loc[index, 'monthly_auther_reply_num'] = 0
                for i in df_temp['lis_auther_reply']:
                    if type(i) == float:
                        df1.loc[index, 'monthly_auther_reply_num'] += 0
                    elif '☀' in i:
                        df1.loc[index, 'monthly_auther_reply_num'] += len(i.split('☀')) - i.count('nan') - i.count('0')
                    else:
                        df1.loc[index, 'monthly_auther_reply_num'] += 1

                # 当月精选留言获赞数
                df_temp = df0[df0['year_month'] == row['year_month']]
                df1.loc[index, 'monthly_content_like_num'] = 0
                for i in df_temp['lis_content_like_num']:
                    if type(i) == float:
                        df1.loc[index, 'monthly_content_like_num'] += 0
                    elif '☀' in i:
                        lis_temp = list(map(int, i.split('☀')))
                        df1.loc[index, 'monthly_content_like_num'] += np.array(lis_temp).sum()

                # 当月作者回复获点赞数
                df_temp = df0[df0['year_month'] == row['year_month']]
                df1.loc[index, 'monthly_auther_like_num'] = 0
                for i in df_temp['lis_auther_like_num']:
                    if type(i) == float:
                        pass
                    elif '☀' in i:
                        lis_temp = list(map(np.float, i.split('☀')))
                        array_temp = np.array(lis_temp)
                        array_temp = np.nan_to_num(array_temp)
                        df1.loc[index, 'monthly_auther_like_num'] += array_temp.sum()
            else:
                df1.loc[index, 'monthly_content_num'] = 0
                df1.loc[index, 'monthly_auther_reply_num'] = 0
                df1.loc[index, 'monthly_content_like_num'] = 0
                df1.loc[index, 'monthly_auther_like_num'] = 0

            # 当月文章标题
            df_temp = df0[df0['year_month'] == row['year_month']]
            lis_temp = df_temp['title'].tolist()
            lis_temp1 = []
            for i in lis_temp:
                i = i.strip('\n').strip('\"')
                lis_temp1.append(i.replace('\n',''))

            df1.loc[index, 'monthly_titles'] = '☀'.join(lis_temp1)
    print(df1)
    df1.to_csv('WithToken/final/{}.csv'.format(account_name))


if __name__ == '__main__':
    print('haha')
    lis_address = os.listdir('WithToken/fine')
    print(lis_address)
    for i in lis_address:
        print('正在开始：{}'.format(i))
        if i in ['temp']:
            continue
        i = i.replace('.csv', '')
        try:
            main(i)
            print('已经完成：{}'.format(i))
            print('################')
        except:
            print('mistakes were made with {}'.format(i))
            raise

    Folder_Path = r'D:\AAA_ImportantFiles\files\AJuniorFirstSemester\PythonProjects\AAAWechatOfficialAccountSpiderBySiyuanLi\WithToken\final'  # 获取源目标文件夹
    SaveFile_Path = r'D:\AAA_ImportantFiles\files\AJuniorFirstSemester\PythonProjects\AAAWechatOfficialAccountSpiderBySiyuanLi\WithToken\final'  # 拼接后要保存的文件路径
    SaveFile_Name = 'final.csv'  # 合并后要保存的文件名字

    os.chdir(Folder_Path)
    file_list = os.listdir()
    print(file_list)

    #  遍历读取文件夹中的每一个文件
    fileStart = 1
    fileEnd = len(file_list)
    for i in range(fileStart, fileEnd):
        df = pd.read_csv(Folder_Path + '/' + file_list[i])
        df.to_csv(SaveFile_Path + '/' + SaveFile_Name,
                    index=False,
                    header=True,  # 如果对每个文件的标题另外有需求，需要对header变量进行指定
                    mode='a')
        print('共合并%i个CSV文件' % len(file_list))
