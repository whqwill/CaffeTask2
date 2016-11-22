#!/usr/bin/env sh

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib:$LOCALLIB:/usr/lib:/usr/lib/x86_64-linux-gnu:/work/cv2/imagelibs/lib:/u/hanselmann/lib:/u/dreuw/lib_x86_64:/u/hanselmann/lib64/lib:/usr/local/cuda-6.0/lib64


GLOG_logtostderr=1 /work/cv2/software/caffe/build/tools/caffe train --solver=/u/haiwang/projects/googlenet_cifar100/solver_new_sp10000_lr001_gm6_smaller_dropout.prototxt -weights /work/cv2/haiwang/model/bvlc_googlenet/bvlc_googlenet.caffemodel
