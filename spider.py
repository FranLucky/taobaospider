import re

from selenium import  webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq
from config import *
from pymongo import MongoClient


mg_client = MongoClient(MONGO_PATH, connect=False)
db = mg_client[MONGO_DB]
client = webdriver.PhantomJS(service_args=SERVICE_ARGS)
wait = WebDriverWait(client, 10)

client.set_window_size(1400, 900)


def search():
    print('进入search')
    try:
        client.get(url='https://www.taobao.com')
        input_label = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="q"]')))
        submit = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="J_TSearchForm"]/div[1]/button')))
        input_label.send_keys(KEYWORD)
        submit.click()
        total_page = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mainsrp-pager"]/div/div/div/div[1]')))
        get_products()
        return total_page.text
    except TimeoutException:
        print('timeout research')
        search()


def get_next_page(page_index):
    print('当前页码', page_index)
    try:
        input_label = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mainsrp-pager"]/div/div/div/div[2]/input')))
        submit = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mainsrp-pager"]/div/div/div/div[2]/span[3]')))
        input_label.clear()
        input_label.send_keys(page_index)
        submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span'), str(page_index)))
        get_products()
    except TimeoutException:
        get_next_page(page_index)


def get_products():
    try:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-itemlist .items .item')))
        html = client.page_source
        doc = pq(html)
        items = doc('#mainsrp-itemlist .items .item').items()
        for item in items:
            product = {
                'title': item.find('.title').text(),
                'detial_url': item.find('.title .J_ClickStat').attr('href'),
                'price': item.find('.price').text(),
                'deal': item.find('.deal-cnt').text()[:-3],
                'shop': item.find('.shop').text(),
                'location': item.find('.location').text(),
            }
            # print(item.find('.shop').text())
            save_mogno(product)
            print('--------------------------')
    except TimeoutException:
        get_products()


def save_mogno(result):
    try:
        if db[MONGO_TABLE].insert(result):
            print('插入数据库成功', result)
    except Exception:
        print('插入数据库失败', result)


def main():
    try:
        total_paga = search()
        # page_count = int(total_paga[2:-2])
        page_count = int(re.compile('(\d+)').search(total_paga).group(1))
        print(page_count)
        for i in range(2, page_count + 1):
            get_next_page(i)
    except Exception:
        print('------error-----',)
    finally:
        client.close()


if __name__ == '__main__':
    main()