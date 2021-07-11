# -*- coding: utf-8 -*-
# Author: coolrc <root@coolrc.me>
# date:   2021/7/11
"""读取配置文件"""
from validit import Template, TemplateDict, Optional, ValidateFromYAML

filepath = 'config.yaml'
template = TemplateDict(
    mail=TemplateDict(
        email=Template(str),
        password=Template(str),
        host=Template(str)
    ),
    http=TemplateDict(
        port=Template(int)
    ),
    token=Template(str)
)

with open(filepath, 'r') as file:
    # load and validate data from the file
    valid = ValidateFromYAML(template, file)
    config = valid.data

if valid.errors:  # if one or more errors found
    print(valid.errors)  # print errors to console
    exit(1)  # exit the script with exit code 1

# else:  # if data matches the template
#     print(valid.data)

if __name__ == '__main__':
    pass
