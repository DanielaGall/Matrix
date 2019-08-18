
# coding: utf-8

# In[1]:


#Import NumPy and Matplotlib
get_ipython().magic(u'matplotlib inline')
import numpy as np 
import matplotlib.pyplot as plt 

#Define vector v 
v= np.array([1,1])

#Plots vector v as blue arrow with red dot at origin (0,0) using Matplotlib
#Creates axes of plot referenced 'ax'
ax = plt.axes()
#Plots red dot at origin (0,0)
ax.plot (0,0, 'or')
#PLots vector v as blue arrow starting at origin 0,0
ax.arrow (0,0, *v,color = 'b',linewidth=2.0,head_width=0.20,head_length=0.25)
#Sets limit for plot axis 
plt.xlim(-2,2)
#Sets major ticks for x-axis
major_xticks=np.arange(-2,3)
ax.set_xticks(major_xticks)

#Sets limit for plot for y-axis
plt.ylim(-1,2)
#Set major ticks for y-axis
major_yticks=np.arange(-1,3)
ax.set_yticks(major_yticks)

#Creates gridlines for only major ticks marks
plt.grid(b=True,which='major')

#Display final plot
plt.show()


















