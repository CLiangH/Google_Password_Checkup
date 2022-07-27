项目目标
=

PoC impl of the scheme

项目原理
=

![image](https://github.com/CLiangH/Picture/blob/main/Goo2.png)

代码解析
=

为方便讨论，在此我使用的是一个文件模拟两个进程交互，并且将原流程中的Hash函数更改为SM3
（其中幂运算更改为了有限域上的运算）

1.首先用户首先计算自己用户名和口令的Hash值h，并将Hash值的前1字节和$h^a$求出发送给服务器
（此处直接返回函数值，将参数传入客户端）

`h=SM3.SM3_test(str(user)+str(password))`

`k=h[:2]`

`v=(pow(int(h,16),a))%n`

2.服务器首先进行预计算，将数据库中所有参数求解Hash
（此处数据库使用数组模拟，其中存储的是用户名为10,000-10256的数据，口令与用户名一致）
之后将前缀匹配的Hash值全部进行幂运算处理，连同$h^{ab}$一同发送至客户端。

3.客户端拿到数据之后，用自己的私钥进行幂逆运算，将求解的值与数组中的泄露值对比以确定是否泄露。

运行指导
=

代码可直接运行

运行截图
=

![image](https://github.com/CLiangH/Picture/blob/main/Goo1.png)


