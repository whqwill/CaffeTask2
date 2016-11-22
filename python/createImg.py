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
imroot = '/work/cv2/haiwang/data/cifar100/images/train/'
traindata = '/work/cv2/haiwang/data/cifar100/cifar-100-python/train'

dic = unpickle(traindata)
num = [0 for i in range(ClassSize)]

for i in range(TrainSize):
	print 'deal with image',i,'...'
	pic = Image.fromarray(dic['data'][i].reshape(3,1024).T.reshape(32,32,3))
	label = dic['fine_labels'][i]
	folder = str(label)+'/'
	imname = str(num[label])+'.png'
	num[label] += 1
	if not os.path.isdir(imroot+folder):
		os.mkdir(imroot+folder)
	pic.save(imroot+folder+imname,'PNG')



