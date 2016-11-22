#!/usr/bin/env sh

source /u/standard/settings/sge_settings.sh
export PATH=${HOME}/bin:${PATH}
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib:$LOCALLIB:/usr/lib:/usr/lib/x86_64-linux-gnu:/work/cv2/imagelibs/lib:/u/hanselmann/lib:/u/dreuw/lib_x86_64:/u/hanselmann/lib64/lib:/usr/local/cuda-6.0/lib64:/home/forster/lib_64:/home/forster/lib_64/opencv-2.4.9:/work/cv2/forster/software/protobuf-2.5.0/jens-install/lib:/work/cv2/software/caffe/build/lib
export LIBRARY_PATH=$LIBRARY_PATH:/usr/lib:/usr/lib/x86_64-linux-gnu:/u/hanselmann/lib:/u/dreuw/lib_x86_64:/u/hanselmann/lib64/lib:/u/forster/lib_64/opencv-2.4.9:/work/cv2/software/caffe/build/lib

TOOLS=/work/cv2/forster/software/caffe/build/tools

EXAMPLE=/work/cv2/haiwang/data/cifar100
DATA=/work/cv2/haiwang/data/cifar100
DBTYPE=leveldb

echo "Creating $DBTYPE..."

/work/cv2/haiwang/data/cifar100/convert_cifar_data_test_divide.bin $DATA $EXAMPLE $DBTYPE

echo "Done."
