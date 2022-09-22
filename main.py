# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import sys


def path_check(path):
  str=' '
  file=open(path,'r',encoding='UTF-8') #只读打开文件
  line = file.readline()
  while line:
    str = str + line
    line = file.readline()
  file.close()
  return str


#参数检测
def parameter_check(add):
    if len(add)!=4:
        print("输入参数不匹配")




#相似度计算
def cal_sim(t1,t2):
   from difflib import SequenceMatcher
   ratio =SequenceMatcher(lambda x: x=="[a-zA-Z0-9\u4e00-\u9fa5]",t1,t2).ratio()
   return ratio


if __name__ == '__main__':
    parameter_check(sys.argv)
    sen1 = (path_check(sys.argv[1]))
    sen2 = (path_check(sys.argv[2]))
    cal_sim(sen1, sen2)
    print("相似度为%0.4f"%cal_sim(sen1, sen2))
    fopen2 = open(sys.argv[3], 'w', encoding="utf-8")  # 编码方式使用UTF-8
    fopen2.write("%.5f" %cal_sim(sen1, sen2))
    fopen2.close()
