# coding:utf-8

import os
import time
import random
import uiautomator2 as u2

"""
订阅频道的屏幕坐标（x,y）：
1: (120, 600)
2: (360, 612)
3: (598, 615)
4: (120, 854)
banner: (513, 555)

文章中跳转到评论的按钮坐标： (691, 113)
点击评论编辑框： (160, 1830)
点击评论发送按钮： (982, 1011)

点击分享按钮： (851, 112)
点击分享到微信： (526, 843)
点击分享到微信的第一个好友： (258, 686)
点击分享： (815, 1310)
点击返回ZAKER： (500, 1189)

点击文章的返回：(73, 120)

根据ZAKER的每日任务来看，需要完成看新闻100条，发送评论100条，分享文章10条，
为了提高容错率，在原有的数量上加0.5倍的访问量，即：新闻150，评论150，分享15

具体操作流程(每一步执行完都要等待一定的时间，防止网络差等情况)：
1.点击具体的频道
2.点击具体的新闻
    循环执行以下操作：
        3.点击跳转到评论的按钮
        4.点击评论编辑框
        5.输入评论内容
        6.点击发送按钮
        7.如果分享的次数小于指标，则执行以下脚本：
            点击分享按钮
            点击分享到微信
            点击分享到微信的第一个好友
            点击分享
            点击返回ZAKER
            次数+1
        8.执行滑动操作（左滑操作：右边坐标 → 左边坐标）
"""

# 各个新闻坐标的数值
news1 = (0.241, 0.199)
news2 = (0.739, 0.201)
news3 = (0.487, 0.445)
news4 = (0.246, 0.672)
news5 = (0.736, 0.676)
news6 = (0.507, 0.838)
news_point_list = [news1, news2, news3, news4, news5, news6]
# 具体的访问次数指标
news_time = 150
comment_time = 150
share_time = 0
# 当前的访问次数
curr_news_time = 0
curr_comment_time = 0
curr_share_time = 0

channel_list_title = ['科技频道', '娱乐八卦', '体育频道', '头条新闻', '今日看点', '深圳热点']


def click_by_text_condition(condition, type_text=True):
    if type_text:
        phone(text=condition).click()


def click_by_resid_condition(condition, click=True, settext=False, text=''):
    if phone(resourceId=condition).wait(timeout=5):
        if click:
            phone(resourceId=condition).click()
        else:
            phone(resourceId=condition).set_text(text)
        time.sleep(1)


def resid_and_inst(resid, inst=0, click=True, gettext=False):
    if click:
        if phone(resourceId=resid, instance=inst).wait(timeout=5):
            phone(resourceId=resid, instance=inst).click()
    elif gettext:
        if phone(resourceId=resid, instance=inst).wait(timeout=5):
            if inst == 0:
                return phone(resourceId=resid).get_text()
            else:
                return phone(resourceId=resid, instance=inst).get_text()
        else:
            return None


def operation_screen(point1, point2, swipetime=0.1):
    """
    根据2个坐标操作屏幕：点击 、滑动
    :param swipetime:
    :param point1:
    :param point2:
    :return:
    """
    x1, y1 = point1
    x2, y2 = point2
    phone.swipe(x1, y1, x2, y2, swipetime)
    time.sleep(1)


def get_screen_comment_count():
    """
    向下滚动屏幕，并返回当前屏幕的评论数
    :return:
    """
    curr_screen_comment_count = phone(className="android.widget.ListView",
                                      resourceId='com.myzaker.ZAKER_Phone:id/article_content_lv') \
        .child(resourceId="com.myzaker.ZAKER_Phone:id/comment_itemv").count
    return curr_screen_comment_count


def get_random_comment():
    """
    从评论列表中获取随机的评论，获取规则如下：
    1.点击评论按钮跳转到评论后，先获取当前屏幕有几条评论，然后使用instance定位方法随机获取当前屏幕评论中的其中一条，加入列表中
    2.向下滑动列表，执行第一步
    :return:
    """
    # 总评论数
    comment_count = resid_and_inst(resid='com.myzaker.ZAKER_Phone:id/comment_menu_item_tv', click=False, gettext=True)
    # 如果总的评论数是None或者不超过8条，则返回None，不做评论，因为评论太少了不好做样本抽取
    if comment_count is None or comment_count == '':
        print('获取新闻评论出错')
        return None
    if int(comment_count) < 8:
        print('当前新闻评论人数过少，不参加评论')
        return None

    print('当前新闻有: ' + comment_count + '条评论')
    # 获取随机列表中评论最长的一条
    longest_comment = ''
    random_comment_list = []

    # 随机滑动几页，然后随机抽取当前屏幕的评论列表中的其中一条评论
    swipe_times = int(int(comment_count) / 5)
    if swipe_times > 7:
        swipe_times = 7
    for swipe in range(1, random.randint(1, swipe_times)):
        swipe_down()
        curr_screen_comment_count = get_screen_comment_count()
        # 因为如果碰见撕逼的评论，通常都会一个屏幕只会显示那一条评论，所以要忽略
        if curr_screen_comment_count >= 3:
            random_news_index = random.randint(1, curr_screen_comment_count)
            print('当前屏幕有评论：的第' + str(random_news_index + 1) + '条评论')
            time.sleep(1)
            comment_add = resid_and_inst(resid='com.myzaker.ZAKER_Phone:id/comment_content_tv',
                                         inst=random_news_index, click=False, gettext=True)

            if comment_add is None:
                comment_add = resid_and_inst(resid='com.myzaker.ZAKER_Phone:id/comment_content_tv',
                                             inst=random_news_index - 2, click=False, gettext=True)

            if comment_add is not None and comment_add != '':
                random_comment_list.append(comment_add)
                print("append: " + comment_add)

    for t_comment in random_comment_list:
        if len(longest_comment) < len(t_comment):
            longest_comment = t_comment

    if len(random_comment_list) >= 3:
        random_comment_list.pop(random_comment_list.index(longest_comment))
        pre_comment = random_comment_list[random.randint(0, len(random_comment_list) - 1)]
        suffix_comment = random_comment_list[random.randint(0, len(random_comment_list) - 1)]
        return pre_comment + " " + suffix_comment
    elif len(random_comment_list) > 0:
        return random_comment_list[0]
    else:
        return None


def comment():
    """
    在编辑框中输入文字
    exist = phone(resourceId="com.myzaker.ZAKER_Phone:id/webview_title_text").wait(exists=False, timeout=5)
    exists=True: 等待timeout值的时间，如果需要等待的元素还是没有出现则返回False，否则返回True
    exists=False: 在timeout的时间内，指定的元素消失的话返回True，否则返回False
    :return:
    """
    global curr_comment_time, comment_time
    if curr_comment_time >= comment_time:
        return

    # os.system('adb shell input text "%s"' % text)  # 此方法不可以输入中文
    # 此处判断的作用是：评论前需要等待这篇新闻先加载完成
    if phone(resourceId='com.myzaker.ZAKER_Phone:id/clock_loading').wait(exists=False, timeout=5):
        pass
    else:
        # 递归调用，网络总不会一直很慢的。。。
        comment()
    # 点击跳转到评论的按钮
    click_by_resid_condition('com.myzaker.ZAKER_Phone:id/comment_menu_item_tv')
    # 返回None，不做评论，因为评论太少了不好做样本抽取
    text = get_random_comment()
    if text is None:
        print('获取随机评论失败！')
        return
    # 点击评论编辑框
    click_by_resid_condition('com.myzaker.ZAKER_Phone:id/comment_reply_content_et_2')
    # 编辑框输入文字
    click_by_resid_condition('com.myzaker.ZAKER_Phone:id/comment_reply_content_et', click=False, settext=True, text=text)
    # 点击发送评论
    click_by_resid_condition('com.myzaker.ZAKER_Phone:id/comment_reply_iv')
    # 评论+1
    curr_comment_time += 1


def share():
    """
    分享操作
    :return:
    """
    global curr_share_time, share_time
    if curr_share_time <= share_time:
        # 点击分享按钮
        click_by_resid_condition('com.myzaker.ZAKER_Phone:id/action_shares')
        # 点击分享到微信
        click_by_resid_condition('com.myzaker.ZAKER_Phone:id/share_wechat')
        # 第一次调起微信分享的时间可能比较久，所以等待一下
        if curr_share_time == 0:
            time.sleep(2)
        # 点击分享到微信的第一个好友
        click_by_resid_condition('com.tencent.mm:id/lp')
        # 点击分享
        click_by_resid_condition('com.tencent.mm:id/an3')
        # 点击返回ZAKER
        click_by_resid_condition('com.tencent.mm:id/an2')
        # 分享+1
        curr_share_time += 1


def go_back():
    """
    返回上一级页面
    :return:
    """
    os.system('adb shell input keyevent 4')
    time.sleep(1)


def swipe_down():
    """
    上划操作
    :return:
    """
    operation_screen((0.506, 0.892), (0.506, 0.121), swipetime=0.3)
    time.sleep(1)


def swipe_up():
    """
    上划操作
    :return:
    """
    operation_screen((0.833, 0.111), (0.814, 0.913), swipetime=0.1)
    time.sleep(1)


def main():
    global curr_news_time, phone
    # 启动app
    phone = u2.connect('192.168.1.103')
    print(phone.info)
    phone.app_start('com.myzaker.ZAKER_Phone')
    channel_size = len(channel_list_title)
    channel_list_title_cache = channel_list_title

    # 每次切换频道阅读新闻的时候都做判断 是否已经达到任务数
    while curr_news_time <= news_time and curr_comment_time <= comment_time and curr_share_time <= share_time:
        channel = ''
        if channel_list_title is None or len(channel_list_title) == 0:
            channel = channel_list_title_cache.pop(random.randint(0, len(channel_list_title) - 1))
        else:
            channel = channel_list_title.pop(random.randint(0, len(channel_list_title) - 1))
        # 点击具体的频道
        click_by_text_condition(channel)
        time.sleep(2)
        # 点击具体的新闻
        news_point = random.choice(news_point_list)
        operation_screen(news_point, news_point)
        curr_news_time += 1
        time.sleep(1)

        # 如果此时显示的界面不是 具体的一条新闻，则点击返回键
        if phone(resourceId="com.myzaker.ZAKER_Phone:id/autoloopswitch_shade_id").wait(exists=False, timeout=5) or \
                phone(resourceId='com.myzaker.ZAKER_Phone:id/webview_title_text').wait(exists=False, timeout=5):
            pass
        else:
            # 一个频道的新闻列表页面不会有2个非正常的新闻页面，所以这里只做二次容错处理
            go_back()
            temp_list = news_point_list
            temp_list.remove(news_point)
            news_point = random.choice(temp_list)
            operation_screen(news_point, news_point)
            time.sleep(1)

        # 每个频道只访问一定的新闻数量
        for news in range(1, int(news_time / channel_size) + 1):
            # 脚本执行到这里就可以认定为已经阅读了一条新闻
            curr_news_time += 1
            # 这里做一段长时间的等待，防止被ZAKER网站后台认定为恶意评论并封号
            time.sleep(random.randint(5, 8))
            # 向下滑动屏幕
            swipe_down()
            # 评论、分享
            comment()
            share()
            # 点击跳转到评论的按钮 返回新闻顶部
            click_by_resid_condition('com.myzaker.ZAKER_Phone:id/comment_menu_item_tv')

            print("当前阅读新闻：" + str(curr_news_time) + ", 当前评论新闻：" + str(curr_comment_time) + ", 当前分享新闻：" + str(
                curr_share_time))
            # 下一条新闻 执行滑动操作（左滑操作：右边坐标 → 左边坐标）
            operation_screen(news2, news1, swipetime=0.03)

        go_back()
        go_back()


if __name__ == '__main__':
    # 启动app
    main()
    # phone = u2.connect('192.168.1.103')
    # print(phone.info)
    # phone.app_start('com.myzaker.ZAKER_Phone')
    # comment()
    # swipe_down()
    print('done!!!')
