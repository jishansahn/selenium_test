# -*-coding: utf-8-*-
# @Author = jishanshan
# @Date = 2020/4/22

a=5
print(__name__)
dd={'a':1}
def foo():
    a=1
    dd['a']=2
    print(a,dd)
print(a,dd)

if __name__=='__main__':
    foo()