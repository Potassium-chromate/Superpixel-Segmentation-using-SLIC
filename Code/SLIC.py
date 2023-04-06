'''
請先安裝 opencv-python
        opencv-contrib-python
不然沒辦法 import cv2
'''
import cv2
import numpy as np 
import matplotlib.pyplot as plt

#SLIC運算法
def SLIC(img,region_size,ruler,colar_space,iteration_times): #這個是superpixel內沒取平均的
    
    if colar_space == "rgb":
        img=img
    elif colar_space == "gray":
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    elif colar_space == "hsv":
        img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    elif colar_space == "lab":
        img = cv2.cvtColor(img, cv2.COLOR_RGB2LAB)
        
    #設定SLIC初始化設定，超像素平均尺寸20(默認為10)，平滑參數為20
    slic = cv2.ximgproc.createSuperpixelSLIC(img,region_size=region_size,ruler=ruler) 
    slic.iterate(iteration_times)     #迭代次數，跌代越多次，則超像素分離的效果越好
    mask_slic = slic.getLabelContourMask() #建立超像素的遮罩，mask_slic數值為1
    mask_inv_slic = cv2.bitwise_not(mask_slic)  
    img_slic = cv2.bitwise_and(img,img,mask =  mask_inv_slic) #在原圖中繪製超像素邊界
    
    if colar_space == "rgb":
        img_slic=img_slic
    elif colar_space == "gray":
        img_slic = cv2.cvtColor(img_slic, cv2.COLOR_GRAY2RGB)
    elif colar_space == "hsv":
        img_slic = cv2.cvtColor(img_slic, cv2.COLOR_HSV2RGB)
    elif colar_space == "lab":
        img_slic = cv2.cvtColor(img_slic, cv2.COLOR_LAB2RGB)
    
    return img_slic

def SLIC_uniform(img,region_size,ruler,colar_space,iteration_times): #這個是superpixel有取平均的
    
    if colar_space == "rgb":
        img=img
    elif colar_space == "gray":
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    elif colar_space == "hsv":
        img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    elif colar_space == "lab":
        img = cv2.cvtColor(img, cv2.COLOR_RGB2LAB)

    slic = cv2.ximgproc.createSuperpixelSLIC(img,region_size=region_size,ruler=ruler)  
    slic.iterate(iteration_times)
    label_slic = slic.getLabels()
    
    # Average the color values of each superpixel
    for label in np.unique(label_slic):
      mask = label_slic == label
      color = cv2.mean(img, mask=mask.astype(np.uint8))[:3] # calculate mean color of superpixel
      img[mask] = color # set all pixels in superpixel to the mean color
    
    if colar_space == "rgb":
        img=img
    elif colar_space == "gray":
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    elif colar_space == "hsv":
        img = cv2.cvtColor(img, cv2.COLOR_HSV2RGB)
    elif colar_space == "lab":
        img = cv2.cvtColor(img, cv2.COLOR_LAB2RGB)
    
    return img

image=plt.imread('C:/Users/88696/Desktop/temp/Jujutsu_Kaisen.png') #自己輸入圖片的路徑
plt.axis('off')
plt.figure(figsize=(10, 20))
plt.subplot(2,1,1)
image_SLIC=SLIC(image,50,20,'lab',10)
plt.imshow(image_SLIC)

plt.subplot(2,1,2)
image_SLI_uniform=SLIC_uniform(image,75,20,'lab',10)
plt.imshow(image_SLI_uniform)
plt.show()
plt.savefig('C:/Users/88696/Desktop/temp/Jujutsu_Kaisen_revise.png',bbox_inches='tight', dpi=450) #看妳要存哪裡
print("finish")