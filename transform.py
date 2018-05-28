# coding=utf-8
import os

def art():
    path="./"
    articles = []
    for root,dirs,files in os.walk(path):
        fileid = 0
        for name in files:
            if name.endswith(".txt") and (root == "./test0\\test0"):
                filename=root+"/"+name
                f=open(filename,"r")
                filecontent='%d' %fileid
                line=f.readline()
                while line:
                    line=line.strip('\n')
                    line=line.strip('*')
                    line=line.rstrip(" - 中国知网")
                    line=line.lstrip("关键词：")
                    filecontent = filecontent + line
                    line=f.readline()
                f.close()
                fileid += 1
                articles.append(filecontent)
    return articles

def cla():
    classes = []
    f = open("./test0/classes.txt","r")
    line = f.readline()
    while line:
        #print(line)
        line = line.strip('\n')
        line = line.strip('；')
        line = line.strip('。')
        classes.append(line)
        line = f.readline()
    return classes
