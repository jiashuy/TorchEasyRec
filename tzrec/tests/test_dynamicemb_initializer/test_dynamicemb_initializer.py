import dynamicemb as de
import torch

from dynamicemb import DynamicEmbInitializerArgs as Args

arg=Args()

x = de.initializer.NormalInitializer(arg)
# y = de.initializer.NormalInitializer(arg)

# invalid configuration argument(int32_t overflow)
# num = 256 * 1024 * 1024 + 13
# dim=8

num =27648
dim=8

a=torch.empty((num,dim), dtype=torch.float, device="cuda:0")
# a1=torch.empty((num,dim), dtype=torch.float, device="cuda:0")
b=torch.arange(num,dtype=torch.int64,device="cuda:0")
c=torch.arange(num,dtype=torch.int64,device="cuda:0")

s0 = torch.cuda.Stream(device='cuda:0')
s1 = torch.cuda.Stream(device='cuda:0')

for i in range(20):
  print(i)
  
  torch.cuda.synchronize()

  # with torch.cuda.stream(s0):
  x(a,b,c)

  # with torch.cuda.stream(s1):
  #   y(a1,b,c)
  
