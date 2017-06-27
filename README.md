# SCPAutoBackup
auto backup files from the remote server via SCP in python.




SCPAutoBackup is a tool of synchronizing the two computer director.
        Can use for backup website;

        # Please privide 6 parameters for this command:

        host--SCP server IP or domain name
        username--SCP login user name
        pwd--User password
        hour-The hour for starting excute task. e.g：Every morning at 8 o'clock
        remote_dir--the dir of remote dir.
        local_dir--the dir of local dir
        


SCPAutoBackp '127.0.0.2' 'root' 'password' '8' '\temp' 'd:/temp'

means: Every morning at 8 o'clock , connect server 127.0.0.2, login this server via user root and password , synchronize remote  path \temp to the local path d:/temp
