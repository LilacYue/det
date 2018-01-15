
import xml.etree.ElementTree as ET
import string
import matplotlib.pyplot as plt
import cv2
import os
from collections import defaultdict
import numpy as np
def ShowResults(img_path,label,bboxes,score,threshold):
    classes=['__background__','car', 'truck', 'bus', 'motorcycle','bicycle', 'person']
    kk=0
    label_num=7
    colors = plt.cm.hsv(np.linspace(0, 1, label_num)).tolist()
    img_index = defaultdict(list)
    for k, va in [(v, i) for i, v in enumerate(img_path)]:
        img_index[k].append(va)
    img_files=set(img_path)
    save_dir = dir + "save_img/"
    if (os.path.exists(save_dir) is not True):
        os.makedirs(save_dir)
    for img_file in img_files:
        kk=kk+1
        img=cv2.imread(img_file)
        #print img.shape
        temp_index=img_index[img_file]
        plt.clf()
        plt.figure(figsize=(19.2,10.8))
        plt.imshow(img)
        plt.axis('off')
        ax = plt.gca()
        for i in temp_index:
            if score[i]>threshold:
                color = colors[classes.index(label[i]) % label_num]
                xmin = int(round(bboxes[i][0]))
                ymin = int(round(bboxes[i][1]))
                xmax = int(round(bboxes[i][2]))
                ymax = int(round(bboxes[i][3]))
                coords = (xmin, ymin), xmax - xmin, ymax - ymin
                ax.add_patch(plt.Rectangle(*coords, fill=False, edgecolor=color, linewidth=3))
                display_text = '%s: %.2f' % (label[i], score[i])
                ax.text(xmin, ymin, display_text, bbox={'facecolor': color, 'alpha': 0.5})

        save_name=save_dir+img_file.split("/")[-1].split(".")[0]
        #print save_name
        plt.savefig(save_name + '_dets.jpg', bbox_inches="tight")
        print kk,len(img_files)
        #exit()
    #plt.show()
    #exit()

def read_img_bbox_score(dir,txt):
    with open (txt,"r") as f1:
        img_path=[]
        bboxes=[]
        score=[]
        label=[]
        for line in f1.readlines():
            temp=line.split(" ")
            temp_img_dir=dir+temp[0].split("/")[-1].split(".")[0]+'.jpg'
            img_path.append(temp_img_dir)
            #print img_path
            #print temp[1:5]
            label.append(temp[1])
            temp_bbox=[string.atof(temp[2]),string.atof(temp[3]),string.atof(temp[4]),string.atof(temp[5])]
            bboxes.append(temp_bbox)
            score.append(string.atof(temp[6]))
    return img_path,label,bboxes,score


def gt(filename):
    """ Parse a PASCAL VOC xml file """
    tree = ET.parse(filename)
    objects = []
    for obj in tree.findall('object'):
        obj_struct = {}
        obj_struct['name'] = obj.find('name').text
        obj_struct['pose'] = obj.find('pose').text
        obj_struct['truncated'] = int(obj.find('truncated').text)
        obj_struct['difficult'] = int(obj.find('difficult').text)
        bbox = obj.find('bndbox')
        obj_struct['bbox'] = [int(bbox.find('xmin').text),
                              int(bbox.find('ymin').text),
                              int(bbox.find('xmax').text),
                              int(bbox.find('ymax').text)]
        objects.append(obj_struct)

    return objects
if __name__ == '__main__':
    dir="/Users/lilac/Code/python/traffic/"
    data_dir='/Users/lilac/Data/Priv_shanxitraffic/Images/'
   # dir = "/home/qiuyue/1/Program/Traffic-SSD/Refine2/"
    txt=dir+'det_result.txt'
    threshold=0.7
    img_path,label, bboxes, score=read_img_bbox_score(data_dir,txt)
    #print img_path[0]
    ShowResults(img_path, label, bboxes, score,threshold)
    print len(img_path)
    print len(set(img_path))
    print len(label)
    print len(set(label))
    #print img_path
    print set(label)
    print "finished"
   # print label.index('car')

    #print d['car']
    #print d
    #print bboxes
    #print score
