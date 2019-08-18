
# coding: utf-8

# In[10]:


#Define vector v
import numpy as np
import matplotlib as plt
v=np.array([-1,2])

#TODO 1.: Define vector i_hat as transformed vector i_hat(ihat_t)
#Where x=3 and y=1 instead of x=1 and y=0 

ihat_t = np.array ([1,0])

#TODO 2.:Define vector j_hat as transformed vector j_hat(jhat_t)
#Where x=1 and y=2 instead of x=0 and y=1 

jhat_t = np.array([0,1])

#Define v_ihat_t - as v[0](x) mutiplied by transformedvector ihat

v_ihat_t = v[0]*ihat_t

#Define v_jhat_t  - as v[1](y) multiplied by transformed vector jhat

v_jhat_t = v[1]*jhat_t

#TODO 3.:Define transformed vector v(v_t) as 
#vector v_ihat_t added to vector v_jhat_t

v_t = None 

#Plot that graphically shows vector v (color = 'skyblue') can be transformed 
#into transformed vector v(v_trfm - color ='b') by adding v[0]*transformed 
#vector ihat to v[0]*transformed vector jhat 

#Creates axes of plot referenced 'ax'

ax = plt.axes()

#Plots red dot at origin (0,0)
ax.plot (0,0,'or')

#Plots vector v_ihat as dotted green arrow starting at origin 0,0
ax.arrow (0,0 *v_ihat, color = 'g', linestyle = 'dotted', linewidth = 2.5, head_width = 0.30, head_length = 0.35)

#Plots vector v_jhat_t as dotted red arrow starting at origin defined by v_ihat
ax.arrow (v_ihat-t [0], v_ihat_t[1], *v_jhat_t, color = 'r', linestyle = 'dotted', linewidth= 2.5, head_width = 0.30, head_lemgth = 0.35
)

#Plots vector v as blue arrow starting at origin 0,0
ax.arrow (0,0, *v,color = 'skyblue', linewidth = 2.5,headwidth = 2.5,head_width = 0.30, head_length = 0.35)

#TODO 4.:Plot transformed vector v(v_t) a blue colored vector (color ='b') using #vector v's as arrow() statement above as template for the plot.

#Set limits for plot for x-axis
plt.xlim (-4,2)

#Set major ticks for x-axis
major_xticks = np.arrange (-4,2)
ax.set_xticks (major_xticks)

#Sets limit for plot for y_axis
plt.ylim (-2,4)

#Set major ticks for y_axis
major_yticks = np.arrange(-2,4)
ax.set_yticks (major_yticks)

#Creates gridlines for only major tick marks
plt.grid (b=True ,width = 'major')

#Displays final plot 
plt.show()
















