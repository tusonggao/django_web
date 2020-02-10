import time
import datetime

from django.shortcuts import render
from .models import RecommendItemInfo
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from .preprocessing_data import  (items_detail_info,
                                  items_old,
                                  items_new)


def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  # 所以这里是真实的ip
    else:
        ip = request.META.get('REMOTE_ADDR')  # 这里获得代理ip
    return ip

def get_new_items(product_code):
    print('in items_show, product_code is ', product_code)
    # recommend_product_codes = items_new['173736']
    recommend_product_codes = items_new[str(product_code)]
    print('recommend_product_codes is ', recommend_product_codes)
    recommend_item_info_lst = []

    for i, prod_code in enumerate(recommend_product_codes):
        item = RecommendItemInfo()
        item.num = i + 1
        item.product_code = prod_code
        item.product_url = 'http://www.jianke.com/product/{}.html'.format(item.product_code)
        try:
            detail_info = items_detail_info[prod_code]
            print('item.product_code is ', item.product_code)
            item.product_name = detail_info['product_name']
            item.product_class_code = detail_info['class_code']
            item.product_class_name = detail_info['class_name']
            item.product_price = detail_info['our_price']
            item.amount = detail_info['amount']
        except:
            print('get an except is for prod_code: ', prod_code)
            item.product_name = 'UnKnown'
            item.product_class_code = 'UnKnown'
            item.product_class_name = 'UnKnown'
            item.product_price = 'UnKnown'
            item.amount = 'UnKnown'
        recommend_item_info_lst.append(item)
        if i>=9:
            break

    self_item = RecommendItemInfo()
    self_item.num = 1
    self_item.product_code = str(product_code)
    detail_info = items_detail_info[str(product_code)]
    print('self_item.product_code is ', self_item.product_code)
    self_item.product_name = detail_info['product_name']
    self_item.product_class_code = detail_info['class_code']
    self_item.product_class_name = detail_info['class_name']
    self_item.product_price = detail_info['our_price']
    self_item.amount = detail_info['amount']
    self_item.product_url = 'http://www.jianke.com/product/{}.html'.format(self_item.product_code)

    return self_item, recommend_item_info_lst

def get_old_items(product_code):
    print('in old_items_show, product_code is ', product_code)
    recommend_product_codes = items_old[str(product_code)]
    print('recommend_product_codes is ', recommend_product_codes)
    recommend_item_info_lst = []

    for i, prod_code in enumerate(recommend_product_codes):
        item = RecommendItemInfo()
        item.num = i + 1
        item.product_code = prod_code
        item.product_url = 'http://www.jianke.com/product/{}.html'.format(item.product_code)
        try:
            detail_info = items_detail_info[prod_code]
            print('item.product_code is ', item.product_code)
            item.product_name = detail_info['product_name']
            item.product_class_code = detail_info['class_code']
            item.product_class_name = detail_info['class_name']
            item.product_price = detail_info['our_price']
            item.amount = detail_info['amount']
        except:
            print('get an except is for prod_code: ', prod_code)
            item.product_name = 'UnKnown'
            item.product_class_code = 'UnKnown'
            item.product_class_name = 'UnKnown'
            item.product_price = 'UnKnown'
            item.amount = 'UnKnown'
        recommend_item_info_lst.append(item)

    self_item = RecommendItemInfo()
    self_item.num = 1
    self_item.product_code = str(product_code)
    detail_info = items_detail_info[str(product_code)]
    print('self_item.product_code is ', self_item.product_code)
    self_item.product_name = detail_info['product_name']
    self_item.product_class_code = detail_info['class_code']
    self_item.product_class_name = detail_info['class_name']
    self_item.product_price = detail_info['our_price']
    self_item.amount = detail_info['amount']
    self_item.product_url = 'http://www.jianke.com/product/{}.html'.format(self_item.product_code)

    return self_item, recommend_item_info_lst


def get_all_items():
    recommend_item_info_lst = []

    item_cnt = 0
    for prod_code in items_new:
        try:
            detail_info = items_detail_info[prod_code]
            item = RecommendItemInfo()
            # item.product_code = detail_info['product_code']
            item.num = item_cnt + 1
            item.product_code = prod_code
            print('item.product_code is ', item.product_code)
            item.product_name = detail_info['product_name']
            item.product_class_code = detail_info['class_code']
            item.product_class_name = detail_info['class_name']
            item.product_price = detail_info['our_price']
            item.amount = detail_info['amount']
            item.product_url = 'http://www.jianke.com/product/{}.html'.format(item.product_code)
            recommend_item_info_lst.append(item)
            item_cnt += 1
        except Exception as e:
            print('get an except for prod_code: ', prod_code, 'e.message is ', str(e))
            continue

    recommend_item_info_lst = sorted(recommend_item_info_lst, key=lambda x: x.amount, reverse=True)
    for i, item in enumerate(recommend_item_info_lst):
        item.num = i + 1
    return recommend_item_info_lst


all_items_info_lst = get_all_items()

def new_items_show(request, product_code):
    self_item, recommend_item_info_lst = get_new_items(product_code)
    return render(request, 'show_recommend_outcome/new_recommend_items.html',
                  {'page_obj': recommend_item_info_lst,
                   'self_item': self_item,
                   'product_code': str(product_code)})



def old_items_show(request, product_code):
    self_item, recommend_item_info_lst = get_old_items(product_code)

    return render(request, 'show_recommend_outcome/old_recommend_items.html',
                  {'page_obj': recommend_item_info_lst,
                   'self_item': self_item,
                   'product_code': str(product_code)})



def merged_items_show(request, product_code):
    self_item, recommend_item_info_lst_new = get_new_items(product_code)
    self_item, recommend_item_info_lst_old = get_old_items(product_code)
    ip = get_ip(request)
    time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print('in merged_items_show from ip: ', ip)
    with open('vistor_records.txt', 'a') as file:
        file.write('time: {} in merged_items_show from ip: {}\n'.format(time_now, ip))
        file.flush()
    return render(request, 'show_recommend_outcome/merged_recommend_items.html',
                  {'page_obj_new': recommend_item_info_lst_new,
                   'page_obj_old': recommend_item_info_lst_old,
                   'self_item': self_item,
                   'product_code': str(product_code)})


def all_items_show(request):
    global all_items_info_lst
    ip = get_ip(request)
    print('in all_items_show() from ip: ', ip)
    time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('vistor_records.txt', 'a') as file:
        file.write('time: {} in all_items_show from ip: {}\n'.format(time_now, ip))
        file.flush()
    return render(request, 'show_recommend_outcome/index.html',
                  {'page_obj': all_items_info_lst})