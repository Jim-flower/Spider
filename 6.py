import os,time
from multiprocessing import Process
def worker():
  print("子进程执行中>>> pid={0},ppid={1}".format(os.getpid(),os.getppid()))
  time.sleep(2)
  print("子进程终止>>> pid={0}".format(os.getpid()))
def main():
  print("主进程执行中>>> pid={0}".format(os.getpid()))
  ps=[]
  # 创建子进程实例
  for i in range(2):
    p=Process(target=worker,name="worker"+str(i),args=())
    ps.append(p)
  # 开启进程
  for i in range(2):
    ps[i].start()
  # 阻塞进程
  for i in range(2):
    ps[i].join()
  print("主进程终止")
if __name__ == '__main__':
  main()