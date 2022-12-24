# coding:utf-8

import yaml
import os


def read_yaml(path):
    with open(path, 'r') as file:
        data = file.read()
        result = yaml.load(data, Loader=yaml.FullLoader)
        return result


def get_all_yaml(root_dir):
    yaml_list = []
    path_list = os.listdir(root_dir)
    for i in range(len(path_list)):
        path = os.path.join(root_dir, path_list[i])
        if os.path.isdir(path):
            yaml_list.extend(get_all_yaml(path))
        if os.path.isfile(path):
            yaml_list.append(path)
    return yaml_list


def read_all_yaml(root_dir):
    yaml_list = get_all_yaml(root_dir)
    data = []
    for i in yaml_list:
        data.append(read_yaml(i))
    return data


if __name__ == '__main__':
    pass
# root_dir = "/Users/yijia/PycharmProjects/pythonProject2/testcase"
# yaml_list = get_all_yaml(root_dir)
# yaml_merge = get_yaml_merge(yaml_list)
# print(yaml_merge)
# print(os.listdir(os.path.abspath('..') + "/testcase"))
# print(os.path.abspath('..'))  # 获得当前工作目录的父目录
