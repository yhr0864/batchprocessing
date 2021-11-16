import os
import glob
from tqdm import tqdm
import cv2


save_dir = os.path.normpath(r'C:\Users\Myth\Desktop\data\output\trainscaling')

if not os.path.exists(save_dir):
    os.mkdir(save_dir)
    print('create folder')
    
gt_image = r'C:\Users\Myth\Desktop\data\output\train\*png'

pictures_list = glob.glob(gt_image)

path1 = r'C:\Users\Myth\Desktop\data\output\train'

with tqdm(total=len(pictures_list)) as bar:
    for pic in pictures_list:
        img = cv2.imread(pic)
        
        height, width = img.shape[:2]
        size = (int(width*0.5), int(height*0.5))  
        img = cv2.resize(img, size, interpolation=cv2.INTER_AREA)  
        
        name = os.path.basename(os.path.normpath(pic))
        
        cv2.imwrite(os.path.join(save_dir, name), img)
      
        bar.update(1)
