import random
g=random.randint(1,1000)
f=int(input('请选择1 到 1000 之间的一个数 : '))
while f != g:
    if f<1:
        print('数字小于1，请重试')
    elif f<g:
        print(f,' 过低')
    if f>1000:
        print('超过1000啦，请重试')
    elif f>g:
        print(f,' 过高')
        
    f=int(input('请再试一次: '))
print('对啦,就是',f)
