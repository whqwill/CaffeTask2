#!/usr/bin/env sh

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib:$LOCALLIB:/usr/lib:/usr/lib/x86_64-linux-gnu:/work/cv2/imagelibs/lib:/u/hanselmann/lib:/u/dreuw/lib_x86_64:/u/hanselmann/lib64/lib:/usr/local/cuda-6.0/lib64

freeCudaDevice=`/u/peter/src/test-gpus/test-gpus.sh | grep "Is free"|head -n1| cut -d" " -f2 | sed -e 's,:,,'`
CUDA_VISIBLE_DEVICES=$freeCudaDevice /work/cv2/haiwang/software/caffe/build/tools/caffe test -model=/u/haiwang/projects/googlenet_cifar100/test_new_divide_random23_soft_6.prototxt -weights=/work/cv2/haiwang/model/googlenet_cifar100_random23_6_iter_16000.caffemodel -gpu=0
