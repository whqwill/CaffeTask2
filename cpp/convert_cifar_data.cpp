//
// This script converts the CIFAR dataset to the leveldb format used
// by caffe to perform classification.
// Usage:
//    convert_cifar_data input_folder output_db_file
// The CIFAR dataset could be downloaded at
//    http://www.cs.toronto.edu/~kriz/cifar.html

#include <fstream>  // NOLINT(readability/streams)
#include <string>

#include "boost/scoped_ptr.hpp"
#include "glog/logging.h"
#include "google/protobuf/text_format.h"
#include "stdint.h"

#include "caffe/proto/caffe.pb.h"
#include "caffe/util/db.hpp"

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

  LOG(INFO) << "Writing Training data";
  scoped_ptr<db::DB> train_db(db::GetDB(db_type));
  train_db->Open(output_folder + "/cifar100_train_" + db_type, db::NEW);
  scoped_ptr<db::Transaction> txn(train_db->NewTransaction());
  // Open files
  std::ifstream data_file_train((input_folder + "/train.bin").c_str(),
      std::ios::in | std::ios::binary);
  CHECK(data_file_train) << "Unable to open train file.";
  for (int itemid = 0; itemid < kCIFARTrainSize; ++itemid) {
    read_image(&data_file_train, &label, buffer);
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
  train_db->Close();

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
  test_db->Close();
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
