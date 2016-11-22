#!/usr/bin/env python

def unpickle(file):
    import cPickle
    fo = open(file, 'rb')
    dict = cPickle.load(fo)
    fo.close()
    return dict

from PIL import Image
import os
TrainSize = 50000
ClassSize = 100
ClusterSize = 8
imroot = '/work/cv2/haiwang/data/cifar100/images/train_validate/'
traindata = '/work/cv2/haiwang/data/cifar100/cifar-100-python/train'
clusterfile = '/work/cv2/haiwang/logs/google_cifar100/validate.clustering.label'
trainlabel = '/work/cv2/haiwang/logs/google_cifar100/train.label'

dic = unpickle(traindata)
num = [0 for i in range(ClassSize)]
flag_train = [False for i in range(TrainSize)]
cluster = []

#read train label
fin = open(trainlabel)
while True:
	line = fin.readline()
	if line in ('',None):
		break
	flag_train[int(line.strip())] = True

#read cluster information
fin = open(clusterfile)
while True:
	line = fin.readline()
	if line in ('',None):
		break
	[i,c,l,n] = map(int,line.split())
	cluster.append((c,l))

#convert binary to image and save
for i in range(TrainSize):
	if flag_train[i]:	
		print 'deal with image',i,'...'
		pic = Image.fromarray(dic['data'][i].reshape(3,1024).T.reshape(32,32,3))
		label = dic['fine_labels'][i]
		folder = str(label)+'/'
		imname = str(num[label])+'.png'
		num[label] += 1
		if not os.path.isdir(imroot+folder):
			os.mkdir(imroot+folder)
		pic.save(imroot+folder+imname,'PNG')



