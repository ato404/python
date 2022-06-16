import time
i=int(input())
ii=i
for j in range(i):
    if ii>3600:
        print('还有',int(ii/3600),'时',end='')
        if ii%3600!=0:
            if (ii%3600)>=60:
                print(int((ii%3600)/60),'分',end='')
                if ii%60!=0:
                    print(ii%60,'秒',end='')
            else:
                print(ii%60,'秒',end='')
    else:
        if ii>=60:
            print('还有',int(ii/60),'分',end='')
            if ii %60!=0:
                print(ii%60,'秒',end='')
        else:
            print('还有',ii,'秒',end='')
    print('')
    ii=(i-j*1)-1
    time.sleep(1)
for i in range(100):
    print('时间到')
