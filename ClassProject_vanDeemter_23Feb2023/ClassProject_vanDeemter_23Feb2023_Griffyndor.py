#!/usr/bin/env python
# coding: utf-8

# # A least-squares fitting execise in gas chromatography.

# The csv file `nm2023/data/exp_data.csv` contains data from a gas chromatography experiment. The first column corresponds to the flow rate, $u$, in milli-Litre-per-minute (mL/min), and the second column corresponds to the plate height, $H(u)$, in millimeter (mm). 
# 
# Fit this data to the [van Deemter equation](https://en.wikipedia.org/wiki/Van_Deemter_equation), $H(u)=A+B/u+Cu$, and determine the diffusion parameters, $A$, $B$, and $C$. The meaning of the parameters are defined in the wiki article linked above. 
# 
# Report the following in a Jupyter notebook (rename this file as `ClassProject_vanDeemter_23Feb2023_githubhandle.ipynb`) and send it via google classroom:   
# - The diffusion parameters, $A$, $B$, and $C$  
# - Accuracy of your fit in terms of mean absolute deviation (MAD), root mean square deviation (RMSD), maximum absolute error (MAD), and Pearson correlation coefficient. 
# - Plot the actual data along with your fitted function.
# 

# # Solution

# ## Codes

# In[40]:



    
  

#=== Read the data from a file
myfile=open('../data/exp_data.csv','r')

x=np.array([])
y=np.array([])

iline=0
for line in myfile:
    if iline > 0:            # i == 0 corresponds to the heading
        str=line.split(',')  # csv, comma separated values
        valx=eval(str[0])
        valy=eval(str[1])
        x=np.append(x,[valx])
        y=np.append(y,[valy])
        
    iline=iline+1
myfile.close() 
    
#=== Let's use numpy's polyval and polyfit 

D=16
N=x.shape[0]

print('#    i','     a_i')
a=np.polyfit(x,y,D)
for i in range(D+1):
    print('{:6d}{:15.8f}'.format(i,a[i]))

p = np.poly1d(a)
print("\nThe fitted polynomial is \n",p,"\n\n")

yfit=np.polyval(a,x)

err=y-yfit
abs_err = np.abs(y-yfit)
perc_err=np.abs( abs_err/y ) *100

print('#    i','     x_i           y_i             y_i (fit)      error          |error|      % error')
for i in range(N):
    print('{:6d}{:15.8f}{:15.8f}{:15.8f}{:15.8f}{:15.8f}{:15.8f}'.format(i,x[i],y[i],yfit[i],err[i],abs_err[i],perc_err[i]))
    
    D=2
c=polyfit(x,y,D)

for i in range(D+1):
    print("coefficient of x^",i," is ",c[i])


# ## Plot

# In[22]:


import numpy as np
import matplotlib.pyplot as plt

plt.plot(x,y,'o',color='r',linewidth=1,label='y$^{exact}$')
plt.plot(x,yfit,'x',color='b',linewidth=1)

xgrids=np.linspace(0,7, 51)
ygridsfit=np.polyval(a,xgrids)

plt.plot(xgrids,ygridsfit,'-',color='b',linewidth=1,label='y$^{fitted}$')

plt.legend()

plt.xlabel("x")
plt.ylabel("y")
plt.title('Polynomial fitting')

#plt.savefig('test.png')  

#=== display
plt.show()


# ## Accuracy of the fit

# In[38]:


print('No. of data points, N: ', N)
print('Degree of the polynomial, D: ', D)

#Mean absolute error
mae=np.mean(abs_err)
print("Mean absolute error: ", mae)

# Centralized error
cerr=err-np.mean(err)

# Variance
var=np.mean(cerr**2)

# Standard deviation
std=np.sqrt(var)
print("Standard deviation:  ", std)

# Numpy's standard deviation
std=np.std(err)
print("Standard deviation using numpy: ", std)



var=np.sum(cerr**2)/(N-D-1.0)
std=np.sqrt(var)
print("Standard deviation of polynomial fit [upper bound]: ", std)



my_rho = np.corrcoef(y, yfit)[0,1]  #check what is [0,1]
print('Pearson correlation coefficient is: ', my_rho)




import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()                          # comment if square plot is not needed
ax = fig.add_subplot(111)                   # comment if square plot is not needed
plt.plot(y,yfit,'x',color='blue')
ax.set_aspect('equal', adjustable='box')    # comment if square plot is not needed
plt.plot(y,y,'-',color='black')

plt.text(10,-5, r'$\rho=$ {0:5.3f}'.format(my_rho), fontsize=10)

plt.legend(['fit','$y=x$'])

plt.xlabel("y$^{exact}$")
plt.ylabel("y$^{fitted}$")
plt.title('Scatterplot')

#plt.savefig('test.png')  

#=== display
plt.show()


# | A       | B       | C       | MAD     | RMSD    | Pearson coefficient |
# |---------|---------|---------|---------|---------|---------------------|
# | 8.183311407357454| -0.08130804288974085 | 0.0005972406390972926  |0.1830695103392632 |   0.2826239933374744        | 0.9882468539039873| 
