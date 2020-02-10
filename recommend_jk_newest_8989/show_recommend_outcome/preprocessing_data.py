import pandas as pd
import time
import os

# def read_item_detail_info():
#     item_detail_info = {}
#     df = pd.read_csv('F:/recommend_jk/outcomes/output_data_detail_info.csv', index_col=False)
#     df['product_code'] = df['product_code'].astype(str)
#     print('df.shape is ', df.shape)
#     print("df[df.product_code=='58474'] is : ", df[df.product_code=='58474'])
#     print('df.dtypes', df.dtypes)
#     return df

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 得到当前文件的的父目录

def read_item_detail_info():
    item_detail_info = {}
    with open(BASE_DIR + '/outcomes/output_data_detail_info.csv', encoding='utf-8') as file:
        line_cnt = 0
        for line in file:
            line_cnt += 1
            if line_cnt==1:
                continue
            try:
                product_code, product_name, class_code, class_name, our_price, amount = line.strip().split(',')
                item_detail_info[product_code] = {'product_name': product_name,
                                                  'class_code': class_code,
                                                  'class_name': class_name,
                                                  'our_price': float(our_price)/100.0,
                                                  'amount': int(amount)}
            except Exception as e:
                print('catch an error, line is ', line, 'str e is ', str(e))
    return item_detail_info

def read_old_recommend_items():
    recommend_items = {}
    with open(BASE_DIR + '/outcomes/old_online_recommend_outcome.csv') as file:
        line_cnt = 0
        for line in file:
            line_cnt += 1
            if line_cnt==1:
                continue
            product_code, items = line.strip().split(',')
            recommend_items[product_code] = list(items.split('#'))
    return recommend_items

def read_new_recommend_items():
    recommend_items = {}
    with open(BASE_DIR + '/outcomes/item_based_recommend_outcome.csv') as file:
        line_cnt = 0
        for line in file:
            line_cnt += 1
            if line_cnt==1:
                continue
            product_code, items = line.strip().split(',')
            if product_code=='999999999':
                continue
            recommend_items[product_code] = list(items.split('#'))
    return recommend_items

items_detail_info = read_item_detail_info()
items_old = read_old_recommend_items()
items_new = read_new_recommend_items()


# if __name__=='__main__':
#     print('hello world!')
#     read_item_detail_info()

    # dd = read_old_recommend_items()
    # print('len of dd is ', len(dd))
    # print('dd content is ', dd)

    # dd = read_new_recommend_items()
    # print('len of dd is ', len(dd))
    # print('dd content is ', dd)




