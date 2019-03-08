# coding=utf-8
import yaml

data = {'data':{'login_data01':
            {'name':'lili',
             'pwd':456,'se':'男'},
        'sex':{'se':'男'}}}


with open("./data.yml",'w',encoding='utf-8')as f:
    w_data = yaml.dump(data,f,encoding='utf-8',allow_unicode=True)