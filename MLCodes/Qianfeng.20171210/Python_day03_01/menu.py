# -*- coding: utf-8 -*-
import os
import pandas as pd

# 指定数据集路径
dataset_path = 'menu'
datafile = os.path.join(dataset_path, 'menu.csv')

# 分析的数据列
used_cols = ['Calories', 'Calories from Fat', 'Total Fat', 'Cholesterol', 'Sugars']


def inspect_data(df_data):
    """
        查看数据集基本信息
    """
    # print('\n===================== 数据预览: =====================')
    # print(df_data.head())
    #
    # print('\n===================== 数据信息: =====================')
    # print(df_data.info())
    #
    # print('\n===================== 数据基本统计信息: =====================')
    # print(df_data.describe())


def main():
#     """
#         主函数
#     """
#     # 读入数据
    menu_data = pd.read_csv(datafile)
#
#     # 查看数据集基本信息
    inspect_data(menu_data)
#
#     # 任务1. 按单品类型分析查看数据
#     print('\n===================== 任务1. 按单品类型分析查看数据 =====================')
#     print('\n===================== 营养成分最高的单品: =====================')
#     max_idxs = [menu_data[col].argmax() for col in used_cols]
#     print(max_idxs)
#     for col, max_idx in zip(used_cols, max_idxs):
#         print('{} 最高的单品：{}'.format(col, menu_data.iloc[max_idx]['Item']))

    print('\n===================== 营养成分最低的单品: =====================')
    min_idxs = [menu_data[col].argmin() for col in used_cols]
    for col, min_idx in zip(used_cols, min_idxs):
        print('{} 最低的单品：{}'.format(col, menu_data.iloc[min_idx]['Item']))
#
#     # 任务2. 按菜单类型分析查看数据
#     print('\n===================== 任务2. 按菜单类型分析查看数据 =====================')
#     print('\n===================== 菜单类型的单品数目分布: =====================')
#     cat_grouped = menu_data.groupby('Category')
#     print('菜单类型的单品数目：')
#     print(cat_grouped.size().sort_values(ascending=False))
#     # sort_values(ascending=False)) 按降序 ， 从大到小
#     # 菜单类型的营养成分分布
#     print('\n===================== 菜单类型的营养成分分布: =====================')
#     print(cat_grouped[used_cols].mean())
#
#     print('\n===================== 营养成分最高的菜单类型: =====================')
#     max_cats = [cat_grouped[col].mean().argmax() for col in used_cols]
#     for col, cat in zip(used_cols, max_cats):
#         print('{} 最高的菜单类型：{}'.format(col, cat))
#
#     print('\n===================== 营养成分最低的菜单类型: =====================')
#     min_cats = [cat_grouped[col].mean().argmin() for col in used_cols]
#     for col, cat in zip(used_cols, min_cats):
#         print('{} 最低的菜单类型：{}'.format(col, cat))
#
#     # 任务3. 查看分析单品及菜单的份量
#     print('\n===================== 任务3. 查看分析单品及菜单的份量 =====================')
#     # 过滤数据，只保留包含 'g'的单品
#     sel_menu_data = menu_data[menu_data['Serving Size'].str.contains('g')].copy()
#
#     def proc_size_str(size_str):
#         """
#             处理serving size字符串，返回g
#         """
#         start_idx = size_str.index('(') + 1
#         end_idx = size_str.index('g')
#         size_val = size_str[start_idx: end_idx]
#         return float(size_val)
#
#     sel_menu_data['Size'] = sel_menu_data['Serving Size'].apply(proc_size_str)
#     inspect_data(sel_menu_data)
#
#     max_idx = sel_menu_data['Size'].argmax()
#     print('份量最多的单品：{}，{}g'.format(sel_menu_data.iloc[max_idx]['Item'], sel_menu_data['Size'].max()))
#
#     min_idx = sel_menu_data['Size'].argmin()
#     print('份量最少的单品：{}，{}g'.format(sel_menu_data.iloc[min_idx]['Item'], sel_menu_data['Size'].min()))
#
#     sel_cat_grouped = sel_menu_data.groupby('Category')
#
#     print('份量最多的类别：{}，{}g'.format(sel_cat_grouped['Size'].mean().argmax(),
#                                   sel_cat_grouped['Size'].mean().max()))
#
#     print('份量最少的类别：{}，{}g'.format(sel_cat_grouped['Size'].mean().argmin(),
#                                   sel_cat_grouped['Size'].mean().min()))

if __name__ == '__main__':
    main()
