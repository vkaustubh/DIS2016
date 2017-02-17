import numpy as np
import matplotlib.pyplot as plt
  
def plot_clusters(orig,pred,nx,ny,legend=True):
  data = orig
  import matplotlib.pyplot as plt
  ylabels = { 0:'Male life expectancy in yrs',1:'Female life expectancy in yrs',2:'Infant mortality, per 1000'}
  # plot data into three clusters based on value of c
  p0 = plt.plot(data[pred==0,nx],data[pred==0,ny],'ro',label='')
  p2 = plt.plot(data[pred==1,nx],data[pred==1,ny],'go',label='') 
  p1 = plt.plot(data[pred==2,nx],data[pred==2,ny],'bo',label='') 

  lx = p1[0].axes.set_xlabel('Per Capita GDP in US$')
  ly = p1[0].axes.set_ylabel(ylabels[ny])
  tt= plt.title('UN countries Dataset, KMeans clustering with K=3')
  if legend:
    ll=plt.legend()  
  return (p0,p1,p2)
  
