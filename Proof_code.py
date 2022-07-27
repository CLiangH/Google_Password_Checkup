import random
import socket
import SM3


    
def Coprime(a, b):
    while a != 0:
        a, b = b % a, a
    if b != 1 and b != -1:
        return 1
    return 0

def gcd(a, m):
    if Coprime(a, m):
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    if u1 > 0:
        return u1 % m
    else:
        return (u1 + m) % m


n = 23
d1 = 5
d2=7
user=15678
password=15687


def Client1(u,p,a):
    h=SM3.SM3_test(str(user)+str(password))
    k=h[:2]#16进制
    v=(pow(int(h,16),a))%n#数字
    return k,v


def Server(k,v,b):
    SJK=[]
    for i in range(10000,10000+pow(2,8)):
        text=SM3.SM3_test(str(i)+str(i))
        SJK.append(text)
    vi=[]
    for V in SJK:
        if V[:2]==k:
            vi.append((pow(int(V,16),b))%n)#数字
    hab=(pow(v,b))%n#数字
    return hab,vi


def Client2(hab,S,a):
    global user
    hb=(pow(hab,gcd(a,n-1)))%n
    a=0
    for V in S:
        b=V
        if b == hb:
            a=1
    if a == 0:
        print('测试账户',user,'安全')
    else:
        print('测试账户',user,'泄露')


k,v = Client1(user,password,d1)
hab,vi = Server(k,v,d2)
Client2(hab,vi,d1)

















