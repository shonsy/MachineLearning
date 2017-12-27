# -*- coding: utf-8 -*-
import os
"""
Created on Sat Oct 15 16:10:12 2016

@author: hasee
"""

txt =open('./gen_word/F1/out/words.txt','r')
myDic = {}
for row in txt:
    data_time=row.split('\n')
    # (key, value) = data_time[0].split(" ")
    # #modify 2017.12.20 by pzh
    key = data_time.split(' ')[0]
    #end
    (key, value) = data_time[0].split( " " )
    myDic[key] = value
#print myDic 
score=dict()
f=open('./test.txt', "r")
dataset=f.readlines()
for line in dataset:
    data_time=line.split('&')
    data=data_time[0].split(' ')
    temp=0
    for i in range(len(data)):
        if data[i] in myDic:
            temp=temp+float(myDic[data[i]])
        if i<len(data)-1:
            if data[i]+'/'+data[i+1] in myDic:
                temp=temp+float(myDic[data[i]+'/'+data[i+1]])
    score[data_time[1]]=temp
print score

dicfile=open('dic.txt','w')
for key in score:
    dicfile.write('%.3f' %score[key])
    dicfile.write(' ')
    dicfile.write(key) 
   # dicfile.write('\n')
dicfile.close()
print 'finish'
    
