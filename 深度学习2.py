import random
import time
def x(a,b):#相乘
    return float(a)*float(b)
def x_list(a,b):#点积
    num=0
    for i in range(len(a)):
        num += x(a[i],b[i])
    return num
def the_not(f_list,w1,w2,b,f1_l,f2_l):#计算平均方差
    num=0
    pr=0
    for i in f_list:
        pr+=((float(f1_l[num])*w1+float(f2_l[num])*w2+b)-i)**2
        num+= 1
    pr=pr/(len(f_list))
    return pr
b=0
lh=float(input())
f=[]
g=[1,1]
f_list=[]
f1_list=[]
f2_list=[]#初始化
llll=0
go=int(input())
y1x=float(input())
y2x=float(input())
for i in range(go):
    y1 = random.randint(10,10**5)
    y2 = random.randint(0,9)
    y = y1*y1x+y2*y2x
    f = [y1, y2]
    f2_list.append(y2)
    f1_list.append(y1)
    f_list.append(y)#更新数据
    if the_not(f_list,g[0],g[1],b,f1_list,f2_list)>the_not(f_list,g[0]+lh,g[1],b,f1_list,f2_list):#w1是否增大？
        g[0]+=lh#增大w1
    elif the_not(f_list,g[0],g[1],b,f1_list,f2_list)>the_not(f_list,g[0]-lh,g[1],b,f1_list,f2_list):#w1是否减小？
        g[0]-=lh#减小w1
    if the_not(f_list,g[0],g[1],b,f1_list,f2_list)>the_not(f_list,g[0],g[1]+lh,b,f1_list,f2_list):#w2是否增大？
        g[1]+=lh#增大w2
    elif the_not(f_list,g[0],g[1],b,f1_list,f2_list)>the_not(f_list,g[0],g[1]-lh,b,f1_list,f2_list):#w2是否减小？
        g[1]-=lh#减小w2
    if the_not(f_list,g[0],g[1],b,f1_list,f2_list)>the_not(f_list,g[0],g[1],b+lh,f1_list,f2_list):#b是否增大？
        b+=lh#增大b
    elif the_not(f_list,g[0],g[1],b,f1_list,f2_list)>the_not(f_list,g[0],g[1],b-lh,f1_list,f2_list):#b是否减小？
        b-=lh#减小b
    print(g,b,lh,the_not(f_list,g[0],g[1],b,f1_list,f2_list))
y1=int(input())
y2=int(input())
f=[y1,y2]
print(x_list(f,g))

        
          
    
