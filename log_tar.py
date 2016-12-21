#!encoding: utf-8
# author: dwong

import tarfile 
import glob
import os 
import shutil

node_list = ['node-15.eayun.com', 'node-17.eayun.com']
# node_list = ['node-15.eayun.com']

root_dir = "/var/log/docker-logs/remote/"

cache_dir = "/tmp/log_collector/"

controller_keyword = ['cinder', 'glance', 'keystone', 'neutron', 'nova']
compute_keyword = ['libvirt', 'neutron', 'nova']
ceph_keyword = []
mongo_keyword = ['mongo']

def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
def make_copy():
    for i in node_list:
        file_dir = root_dir + str(i) 
        sub_dir = cache_dir + str(i) 
        create_dir(sub_dir)
        #create destination directory  
        # create_dir(cache_dir+str())
        #  print file_dir
        for key in controller_keyword: 
            # print key
    #       print '%s/%s+*.log' % (file_dir, key)
            for file in glob.glob('%s/%s*.log' % (file_dir, key)):
                 '''two below to extract the filename '''  
    #              tar.add('%s/' %i, recursive=False)
    #              tar.add(file, arcname = i+'_'+file.split("/")[-1])     
    #              tar.add(file, arcname = os.path.basename(file))
                 print file
                 shutil.copy2(file, sub_dir)

def make_tar(): 
    with tarfile.open("/tmp/log_collector.tar", "w:gz") as tar: 
        tar.add('%s' %cache_dir, arcname="log_collect")

def main():
    make_copy()
    make_tar()

if __name__ =="__main__":
    main()
