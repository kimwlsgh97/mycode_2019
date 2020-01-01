#!C:\Python27\python.exe
#-*- coding:utf-8 -*-
print("content-type: text/html; charset=utf-8\n")

def print_value_list(values):
    for val in values:
        if val == 'web':
            print('This is, ')
        elif val == 'crawler':
            print('Web Crewler!')

if __name__=='__main__':
    value_list = ['how', 'to', 'make', 'web', 'crawler']
    print_value_list(value_list)
