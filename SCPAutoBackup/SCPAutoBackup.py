#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Eric.yue


import paramiko,os,sys,time

class Paramiko_get(object):
    def __init__(self,host,username,pwd,remote_dir,local_dir):
        self.host = host
        self.username = username
        self.passwd =pwd
        self.port = 22
        self.local_dir = local_dir
        self.remote_dir = remote_dir
        self.tt = None

    def pk_connect(self):
        self.tt = paramiko.Transport((self.host, self.port))
        self.tt.connect(username = self.username, password = self.passwd)
        try:
            return paramiko.SFTPClient.from_transport(self.tt)
        except Exception as e:
            print 'Connect error:',e
            exit()

    def get_file(self):
        sftp = self.pk_connect()
        files = sftp.listdir(self.remote_dir)
        cnt = 0
        if not os.path.exists(self.local_dir):
            os.makedirs(self.local_dir)
        for file in files:
            dstfile=os.path.join(self.local_dir, file)
            if not os.path.exists(dstfile):
                print file+ ' is downloading'
                sftp.get(self.remote_dir+'/'+file,dstfile)
            else:
                print file +' is exist'
            cnt += 1


        if cnt == len(files):
            print str(cnt) +' files get successful'
        else:
            print 'get failure'

    def __del__(self):
        self.tt.close()



if __name__ == "__main__":
    if(len(sys.argv)!=6):
        print '''
        SCPAutoBackup is a tool of synchronizing the two computer path.
        Can use for backup website;

        Please privide 6 parameters for this command:

        host--SCP server IP or domain name
        username--SCP login user name
        pwd--User password
        hour--clock per day
        remote_dir--the dir of remote dir.
        local_dir--the dir of local dir
        '''
    else:
        while True:    
            current_time = time.localtime(time.time())
            if((current_time.tm_hour == 2) and (current_time.tmin == 0) and (current_time.tsec == 0)):
                pk = Paramiko_get(sys.argv[0],sys.argv[1],[2],sys.argv[3],sys.argv[4],sys.argv[5])
                pk.get_file()
            time.sleep(300)   
    
