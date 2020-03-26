#!/usr/bin/env python
# coding: utf-8

# In[4]:


import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# In[7]:


import cv2


# In[10]:


image = cv2.imread('C:/Users/compaq-pc/Desktop/Image processing Using Opencv, Keras and tensorFlow/data/chewbacca.jpg')


# In[11]:


type(image)


# In[13]:


image.shape


# In[14]:


plt.imshow(image)


# In[15]:


image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image)


# In[16]:


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray, cmap = 'gray')


# In[17]:


height = 300
width = 300


# In[18]:


resized = cv2.resize(image, (height, width))

plt.imshow(resized)


# In[21]:


aspect = image.shape[1] / float(image.shape[0])
print(aspect)

if aspect > 1:
    res = int(aspect * height)
    scaled = cv2.resize(image, (res, height))
if aspect < 1:
    res = int(width / aspect)
    scaled = cv2.resize(image, (width, res))
if aspect == 1:
    scaled = cv2.resize(image, (width, height))
    
plt.imshow(scaled)


# In[24]:


def crop_center(img, cropx, cropy):
    y,x,c = img.shape
    startx = x//2-(cropx//2)
    starty = y//2-(cropy//2)
    return img[starty:starty+cropy, startx:startx+cropx]

cropped = crop_center(scaled, width, width)

plt.imshow(cropped, cmap='gray')


# In[26]:


#DRAWING ON IMAGE

image = cropped.copy()
#add text
cv2.putText(image, 'TEXT', (70, 270),
           cv2.FONT_HERSHEY_SIMPLEX, 0.8, (20, 240, 150), 2)
#add line
cv2.line(image, (75, 280), (280,280), (50,100,250), 3)

plt.imshow(image, cmap='gray')


# In[ ]:




