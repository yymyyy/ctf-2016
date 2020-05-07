根据题目源码，写以下小代码：

import msgpack
c=open("msg.enc").read()
for r_s, c_s in msgpack.unpackb(c):
    print "-r- "*20
    r = int(r_s.encode('hex'), 16)
    print r
    print "-c- "*20
    c = int(c_s.encode('hex'), 16)   
    print c 

ms=open("msg.txt").read()
for i in range(0, len(ms), 256):
    m = ms[i:i+256]
    m = int(m.encode('hex'), 16)
    print "-m- "*20
    print m


在kali的python2中跑，得到：
 m1 m2
r1 r2
c1 c2


步骤02 在SageMath手敲运行 solv.sage 求得K

root@kali:~/CTF-RSA-tool/special_rsa# python ok.py dec flag.enc flag.txt
root@kali:~/CTF-RSA-tool/special_rsa# more flag.txt
得到答案
