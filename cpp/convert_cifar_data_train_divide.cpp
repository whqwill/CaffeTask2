//
// This script converts the CIFAR dataset to the leveldb format used
// by caffe to perform classification.
// Usage:
//    convert_cifar_data input_folder output_db_file
// The CIFAR dataset could be downloaded at
//    http://www.cs.toronto.edu/~kriz/cifar.html

//#include <stdio.h>
//#include <stdlib.h>
#include <fstream>  // NOLINT(readability/streams)
#include <string>

#include "boost/scoped_ptr.hpp"
#include "glog/logging.h"
#include "google/protobuf/text_format.h"
#include "stdint.h"

#include "caffe/proto/caffe.pb.h"
#include "caffe/util/db.hpp"

#include <time.h>

using caffe::Datum;
using boost::scoped_ptr;
using std::string;
namespace db = caffe::db;

const int kCIFARSize = 32*8;
const int kCIFARImageNBytes = 3072*64;
const int kCIFARTrainSize = 50000;
const int kCIFARTestSize = 10000;

void convert_buffer_strbuffer(char* buffer, char* str_buffer) {
  for (int l = 0; l < 3; l++) {
    for (int i = 0; i < 32; i++) {
      for (int j = 0; j < 32; j++) {
        int k = i*32+j;
        for (int x = 0; x < 8; x++) {
          for (int y = 0; y < 8; y++) {
            int a = i*8+x;
	    int b = j*8+y;
	    int p = a*256+b;
            str_buffer[l*1024*64+p] = buffer[l*1024+k];
          }
        }
      } 
    }
  }
  return;
}

void read_image(std::ifstream* file, int* label, char* buffer) {
  char superlabel_char;
  char label_char;
  file->read(&superlabel_char, 1);
  file->read(&label_char, 1);
  *label = label_char;
  file->read(buffer, kCIFARImageNBytes/64);
  return;
}

void convert_dataset(const string& input_folder, const string& output_folder,
    const string& db_type) {
  int label;
  char str_buffer[kCIFARImageNBytes];
  char buffer[kCIFARImageNBytes/64];
  Datum datum;
  datum.set_channels(3);
  datum.set_height(kCIFARSize);
  datum.set_width(kCIFARSize);
  
  std::cout << "Testing" << std::endl;

  LOG(INFO) << "Writing Training data";

  // read clustering label 
  std::cout << (input_folder + "/cluster3.22.label").c_str() << std::endl;
  std::ifstream file_cluster((input_folder + "/cluster3.22.label").c_str(),std::ios::in);
  int cluster_label[100][3];
  memset(cluster_label,0,sizeof(cluster_label));
  int cluster_num = 0;
  for (int i = 0; i < 100; i++) {
        int j;
	file_cluster >> j;
	file_cluster >> cluster_label[j][0] >> cluster_label[j][1] >> cluster_label[j][2];
	std::cout << j << " " << cluster_label[j][0] << " " << cluster_label[j][1] << " " << cluster_label[j][2] << std::endl;
        if (cluster_label[j][0] > cluster_num) 
		cluster_num = cluster_label[j][0];
		std::cout << "cluster_num" << cluster_num << std::endl;
  }
  int num_each_cluster[100] = {0};
  for (int i = 0; i < 100; i++) {
  	num_each_cluster[cluster_label[i][0]] = cluster_label[i][2];
  }
  
  std::cout << "Testing2" << std::endl;

  int num_train[100] = {0};
  int num_validate[100] = {0};
  int sum_train = 0;
  int sum_validate = 0;
  srand(23);
 
  scoped_ptr<db::DB> *train_db[cluster_num];
  for (int i = 0; i < cluster_num; i++) {
	train_db[i] = new scoped_ptr<db::DB>(db::GetDB(db_type));
	std::stringstream ss;
	ss << i+1 << "(" << num_each_cluster[i+1] << ")";
  	(*train_db[i])->Open(output_folder + "/cifar100_train_cluster22_" + db_type + ss.str(), db::NEW); 
  } 

  std::cout << "Testing3" << std::endl;

  //scoped_ptr<db::DB> validate_db(db::GetDB(db_type));
  //validate_db->Open(output_folder + "/cifar100_validate_" + db_type, db::NEW); 
  
  //int num_train[100] = {0};
  //int num_validate[100] = {0};
  //int sum_train = 0;
  //int sum_validate = 0;
  //srand(time(NULL));   

  scoped_ptr<db::Transaction> *txn_train[cluster_num];
  for (int i = 0; i < cluster_num; i++) 
	txn_train[i] = new scoped_ptr<db::Transaction>((*train_db[i])->NewTransaction());
  //scoped_ptr<db::Transaction> txn_validate(validate_db->NewTransaction());
 // Open files
  
  std::cout << "Testing4" << std::endl;

  std::ifstream data_file_train((input_folder + "/train.bin").c_str(),
      std::ios::in | std::ios::binary);
  CHECK(data_file_train) << "Unable to open train file.";
 
  //for (int i = 0; i < 100; i++) 
	//std::cout << i << " " << cluster_label[i] << std::endl;
 
  for (int itemid = 0; itemid < kCIFARTrainSize; ++itemid) {
    read_image(&data_file_train, &label, buffer);
    convert_buffer_strbuffer(buffer,str_buffer);
    datum.set_label(cluster_label[label][1]);
    datum.set_data(str_buffer, kCIFARImageNBytes);
    int length = snprintf(str_buffer, kCIFARImageNBytes, "%05d", itemid);
    string out;
    CHECK(datum.SerializeToString(&out));

    if (num_validate[label] >= 100 || (num_train[label] < 400 && rand()%5 > 0)) {
	std::cout << itemid << "belongs to training set " << label << " " << cluster_label[label][0] << std::endl;
    	if (cluster_label[label][0] > 0) 
		    (*txn_train[cluster_label[label][0]-1])->Put(string(str_buffer, length), out); 
	if (cluster_label[label][0] == 4) 
			std::cout << "!!!!" << cluster_label[label][0] << " " << cluster_label[label][1] << " " << cluster_label[label][2] << std::endl;
	num_train[label]++;
	sum_train++;
    }
    else {
	std::cout << itemid << "belongs to validation set " << label << " " << cluster_label[label][0] << std::endl;
	num_validate[label]++;
	sum_validate++;
    }
    std::cout << itemid << "done" <<std::endl;
  }
    
  
  std::cout << "sum of training set: " << sum_train << std::endl;
  std::cout << "sum of validation set: " << sum_validate << std::endl;

  for (int i = 0; i < cluster_num; i++) {
	(*txn_train[i])->Commit();
 	//txn_validate->Commit();
  	(*train_db[i])->Close();
  	//validate_db->Close();
  	std::cout << "train_db " << i << " has been closed." << std::endl;
  }
  std::cout << "Done." << std::endl;
/*
  LOG(INFO) << "Writing Testing data";
  scoped_ptr<db::DB> test_db(db::GetDB(db_type));
  test_db->Open(output_folder + "/cifar100_test_" + db_type, db::NEW);
  txn.reset(test_db->NewTransaction());
  // Open files
  std::ifstream data_file_test((input_folder + "/test.bin").c_str(),
      std::ios::in | std::ios::binary);
  CHECK(data_file_test) << "Unable to open test file.";
  for (int itemid = 0; itemid < kCIFARTestSize; ++itemid) {
    read_image(&data_file_test, &label, str_buffer);
    convert_buffer_strbuffer(buffer,str_buffer);
    datum.set_label(label);
    datum.set_data(str_buffer, kCIFARImageNBytes);
    int length = snprintf(str_buffer, kCIFARImageNBytes, "%05d", itemid);
    string out;
    CHECK(datum.SerializeToString(&out));
    txn->Put(string(str_buffer, length), out);
    std::cout << itemid << std::endl;
  }
  txn->Commit();
  test_db->Close();*/
}

int main(int argc, char** argv) {
  if (argc != 4) {
    printf("This script converts the CIFAR dataset to the leveldb format used\n"
           "by caffe to perform classification.\n"
           "Usage:\n"
           "    convert_cifar_data input_folder output_folder db_type\n"
           "Where the input folder should contain the binary batch files.\n"
           "The CIFAR dataset could be downloaded at\n"
           "    http://www.cs.toronto.edu/~kriz/cifar.html\n"
           "You should gunzip them after downloading.\n");
  } else {
    google::InitGoogleLogging(argv[0]);
    convert_dataset(string(argv[1]), string(argv[2]), string(argv[3]));
  }
  return 0;
}
