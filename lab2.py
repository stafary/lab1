# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\Magics\.spyder2\.temp.py
"""
import sys
import time
start_time = time.clock()
Q = 0
sel_final = ''
In = [False]*14
R = [[] for i in range(14)]
P =  [[] for i in range(14)]
mark = [[] for i in range(14)]
S  = [[] for i in range(14)]
SS = []
p =  []
last = 0
dic = {}
R_final = 0
Cost_final = 0
def dfs(i,r,price,sel):
    global Q,sel_final,last,p,max_price,r_need,R_final,Cost_final
    if(i == last):
        if(r - price/100 > Q):
            Q = r - price/100
            R_final = r
            Cost_final = price
            sel_final = sel
        return
    len2 = len(p[i])
    for k in range(0,len2):
        price2 = price + p[i][k][1]
        r2 = r*p[i][k][0]
        sel2 = sel + p[i][k][2] + ' '
        if(price2 > max_price):
            return
        if(r < r_need):
            continue
        dfs(i+1,r2,price2,sel2)


f = open("SERVICE.txt",'r')
service = f.read().split()
f.close()
len1 = len(service)

for k in range(0,len1):
    if (not(k % 5 == 2 or k % 5 == 4 or k % 5 == 0)): continue
    i = int(k / 2500)
    if (k%5 == 2):
        R[i].append(float(service[k]))
    else:
        if (k % 5 == 4):
            P[i].append(float(service[k]))
        else:
            mark[i].append(service[k])

for i in range(0,14):
    SS.append(zip(R[i],P[i],mark[i]))
for i in range(14):
    useful = [True]*500
    for j in range(500):
        for k in range(j+1,500):
            if(useful[k] == False):
                continue
            if(SS[i][j][0] > SS[i][k][0] and SS[i][j][1] <SS[i][k][1]):
                useful[k] = False
            else:
                if(SS[i][j][0] == SS[i][k][0] and SS[i][j][1] <SS[i][k][1]):
                    useful[k] = False
                else:
                    if(SS[i][j][0] > SS[i][k][0] and SS[i][j][1] ==SS[i][k][1]):
                        useful[k] = False
                    else:
                        if(SS[i][j][0] < SS[i][k][0] and SS[i][j][1] >SS[i][k][1]):
                            useful[j] = False
                        else:
                            if(SS[i][j][0] == SS[i][k][0] and SS[i][j][1] >SS[i][k][1]):
                                useful[j] = False
                            else:
                                if(SS[i][j][0] < SS[i][k][0] and SS[i][j][1] ==SS[i][k][1]):
                                    useful[j] = False
    for j in range(500):
        if(useful[j]):
            S[i].append(SS[i][j])            
for l in S:
    l.sort(key = lambda x:x[1])
    
f = open("PROCESS.txt",'r')
process = f.readlines()
f.close()


f = open("REQ.txt",'r')
request = f.readlines()
f.close()
for c in range(0,4):
    sel_final = ''
    In = [False]*14
    Q = 0
    tmp = ''  
    t = 1
    dic = {}
    while(request[c][t] != ','):
        tmp += request[c][t]
        t+=1
    r_need = float(tmp)
    t+=1
    tmp = ''
    while(request[c][t] != ')'):
        tmp+= request[c][t]
        t+=1
    max_price = float(tmp)

    pp =[]
    for char in process[c]:
        if(char.isalpha()):
            In[ord(char) - ord('A')] = True
    for s in range(0,14):
        if(In[s]):
            pp.append(S[s])
    last = len(pp)
    p = [[] for k in range(last)]
    for j in range(last):
        len3 = len(pp[j])
        useful = [True]*len3
        for k in range(len3):
            if(pp[j][k][0] <= r_need or pp[j][k][1]>=max_price):
                useful[k] = False
        for k in range(len3):
            if(useful[k]):
                p[j].append(pp[j][k])
    p.sort(key = lambda x: x[0][1], reverse = True)
    dfs(0,1,0,'')
    dic_tmp = sel_final.split()
    for x in dic_tmp:
        dic[x[0]] = x[2:]
    if Q != 0:
        len2 = len(process[c])
        for i in range(0, len2):
            for char in process[c][i]:
                if not(char.isalpha()):
                    sys.stdout.write(char)
                else:
                    sys.stdout.write(char)
                    sys.stdout.write('-')
                    sys.stdout.write(dic[char])
        print "Reliability="+str(R_final)+","+ "Cost=",str(Cost_final)\
                + "," +"Q=" + str(Q)
    else:
        print "Negative!"
end_time = time.clock()
print "run: %f s"%(end_time-start_time)