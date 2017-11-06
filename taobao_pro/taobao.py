from selenium import webdriver
import time
# from bs4 import BeautifulSoup
import re
import json
from config import *

# 1.添加多个账号，分不同的vip
# 2.浏览时间
# 3.添加收藏和购物车需要添加多个账号，不添加账号只是浏览，清楚cookie
# 4.云任务、本地任务


def first_content(contents):
    '''
    首页商品信息页
    '''
    # s = requests.get(first_url)
    # contents = content
    regex = 'g_page_config = (.+)'
    items = re.findall(regex, contents)
    items = items.pop().strip()
    items = items[0:-1]
    items = json.loads(items)
    items = items['mods']['itemlist']['data']['auctions']
    if items:
        # print(items)
        for item in items:
            # print(item['nick'])
            if item['nick'] == '张大宝9527':
                url = 'https://item.taobao.com' + item['detail_url']
                print(url)
                return url
                #goods_id, shop_id = self.sovl_dict(items)
                #self.second_content(goods_id, shop_id)  # 爬取二级页面
                #time.sleep(1)
    else:
        return

if __name__ == '__main__':
    dirver = webdriver.PhantomJS()
    dirver.get("https://www.taobao.com/")
    time.sleep(1)

    #[{'expiry': None, 'httpOnly': False, 'name': 'thw', 'domain': '.taobao.com', 'value': 'cn', 'secure': False, 'path': '/'}, 
    #{'expiry': None, 'httpOnly': False, 'name': '_med', 'domain': 'www.taobao.com', 'value': 'dw:1440&dh:900&pw:1440&ph:900&ist:0', 'secure': False, 'path': '/'},
    #{'expiry': None, 'httpOnly': False, 'name': 'v', 'domain': '.taobao.com', 'value': '0', 'secure': False, 'path': '/'}, 
    #{'expiry': None, 'httpOnly': False, 'name': 't', 'domain': '.taobao.com', 'value': '8c054bec44041cb072e6ca84aedaf560', 'secure': False, 'path': '/'}, 
    #{'expiry': None, 'httpOnly': True, 'name': 'cookie2', 'domain': '.taobao.com', 'value': '129a0eb17385c43ea2d37f78c1366c3b', 'secure': False, 'path': '/'},
    #{'expiry': None, 'httpOnly': False, 'name': '_tb_token_', 'domain': '.taobao.com', 'value': 'e3770bd87877a', 'secure': False, 'path': '/'},
    #{'expiry': None, 'httpOnly': False, 'name': 'isg', 'domain': '.taobao.com', 'value': 'AsHBPN7XfM77uZD6p280gFEl0QsbRjSHGH-XjSMWvUgnCuHcaz5FsO8ImkSz', 'secure': False, 'path': '/'},
    #{'expiry': None, 'httpOnly': False, 'name': 'cna', 'domain': '.taobao.com', 'value': 'qiJlEnME0z4CAXaQhSc7VrL9', 'secure': False, 'path': '/'}]
    #dirver.delete_all_cookies()
    print(dirver.get_cookies())

    
    dirver.find_element_by_xpath('//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]').click()
    print("login")
    dirver.find_element_by_xpath('//*[@id="J_QRCodeLogin"]/div[5]/a[1]').click()
    print("qiehuandengluming")
    dirver.find_element_by_xpath('//*[@id="TPL_username_1"]').clear()
    print("清空用户名")
    dirver.find_element_by_xpath('//*[@id="TPL_password_1"]').clear()
    print("清空密码")
    dirver.find_element_by_xpath('//*[@id="TPL_username_1"]').send_keys(USERNAME)
    print("输入用户名")
    dirver.find_element_by_xpath('//*[@id="TPL_password_1"]').send_keys(PASSWORD)
    print("输入密码")
    dirver.find_element_by_xpath('//*[@id="J_SubmitStatic"]').click()
    print("点击确定")
    time.sleep(2)
    print(dirver.page_source)
    
    dirver.find_element_by_xpath('//*[@id="q"]').clear()
    time.sleep(1)
    dirver.find_element_by_xpath('//*[@id="q"]').send_keys('凿壁钥匙扣')
    time.sleep(1)
    dirver.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button').click()
    time.sleep(1)
    dirver.find_element_by_xpath('//*[@id="mainsrp-itemlist"]/div/div/div[1]/div[1]/div[2]/div[2]').click()
    time.sleep(2)
    
    # soup = BeautifulSoup(dirver.page_source, 'lxml')
    # print(soup.getText())
    url = first_content(dirver.page_source)
    print(url)
    dirver.get(url)
    time.sleep(5)
    dirver.quit()
    # 打开页面点击收藏
    # dirver.get('https://click.simba.taobao.com/cc_im?p=%B9%B6%C0%FB%B9%FA%BC%D2%C9%FA%CB%C0%D2%D1%C6%F1%D2%F2%B8%A3%BB%F6%B1%DC%C7%F7%D6%AE&s=584678424&k=577&e=qzPBbEd%2FmCpqXJDnZyXVXWXRE9qbZxfR1ukJ6FhRvRvyEcu%2FKKhWNwrYcIe06gvSfZDmKWqCg%2Bma5jpnnkl9NGKTOvW70ShgEsCi4%2BQyfA1rU6l9KpVerJV26usGLzXmxmdnPPlUBSRblNyXEt9oQOKI2YcUmjt5s%2FSQcYMnVMvJLPemqKrwrGIgmb1MJ856q1s1x3neHZisULK1ShclqQEiVoqkq7zOTHIVWTBk1UnhNm3yR6mX%2BhJMYfR2OLrYm2%2FQvs2wRD3CcaouDVN%2BlyQURnTDy4ngkZBfZQYv12oUD6QkqHGvN5ENI%2BLhf0BunbL%2B0avU1zOJM40%2BvOSUvCrfdMRqw0%2F3GFXVrrIk%2BcSqZsxY5hDrh878T0fyJmgT87sWwPSZXO3BNv2i5ayeMmPa6DceQHiO1OLsLkntjiMQfjalFWD1X1p7MA7DZt9cAv47GpDtff5c4jd0XKIz6bwS7280CvpxmbHb8l2uNCZ%2F44NMM0RLJAoA2uYdghhJoYC6tjfbRFKrbCgrPeQ3vlZcfkp1Nk0l%2BEox9AtgpxMG63%2B%2FplahwSZ916OOsS%2F%2B')
    # time.sleep(2)
    # dirver.find_element_by_xpath('//*[@id="J_AddFavorite"]').click()


    # time.sleep(1)
    # for i in range(10):
    #     # 模拟浏览器跳转到最底
    #     dirver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    #     time.sleep(2)
    # dirver.find_element_by_xpath('//*[@id="J_LinkBasket"]').click()
    # dirver.find_element_by_xpath('').click()

    # //*[@id="J_Itemlist_TLink_539726491342"]
    # //*[@id="J_Itemlist_TLink_523330929977"]

