'''
Created on 19 Apr 2016

@author: Dev2
'''

import time
import sys
import pysftp
import os

class IsilonHelper():
    '''
    -pip install pysftp
    -url -http://pysftp.readthedocs.io/en/release_0.2.8/cookbook.html
    -FTP User name
    -FTP Password
    -Location of the .UVP
    -Location of the Drop Zone for the Signiant to pick up the .mxf or .uvp 
    -portal dropzone=/mnt/dmz/atlas_provider_1 or /mnt/dmz/atlas_provider_2
    
    Scenario:
        Login to isilon
        check for package 
        Move package to dropzone
        End.
        
    '''
    cinfo = {}
    
    '''
    @summary: Set the connection details to the SFTP server, currently they are set to default OTT Atlas
    '''
    def __init__(self,_host='10.80.194.86',_username='root',_password='0TT3rdParTy!',_port=22):
        #set connection details
        self.host=_host
        self.username=_username
        self.password=_password
        self.port=_port
        IsilonHelper.cinfo = {'host':_host, 'username':_username, 'password':_password, 'port':_port}
        print 'set connection details', self.cinfo
    
    '''
    @summary: Create a secure connection to the FTP server e.g. SFTP connection and set the current working directory
    '''
    def secure_FTP(self,destination_folder='/mnt/dmz/atlas_provider_1'):
            sftp = pysftp.Connection(**self.cinfo)
            sftp.cwd(destination_folder)
            print 'set current working directory -',sftp.getcwd()
            return sftp
    
    '''
    @summary: Send media assets to the drop zone location given via the method secure_FTP e.g. example.jpgs or example.mxfs
    '''
    def send(self,sftp,_file):
        print("File:"+_file)
        sftp.put(_file, preserve_mtime=True)
        return sftp.exists(os.path.basename(_file))
    
    '''
    @summary: Close the connection to the SFTP server when finished
    '''
    def close_FTP(self,sftp):
        print("close connection....")
        sftp.close()
        print("connection closed")
        
        
    def file_exists(self,sftp,_file):
        return sftp.exists(_file)
    
    '''
    @todo: Create a function to rename the file
    @rename the existing file and move on need random gen for name
    '''
    def rename_file(self,sftp,_file,new_name=None):
        sftp.rename()
        return sftp.exists(os.path.basename(new_name))
    
if __name__=='__main__':
    connection = IsilonHelper()
    _sftp = connection.secure_FTP()
    print connection.send(_sftp,'C:\\workspace\\AtlasPortalAutomation\\isilon\\test media\\auto_test_media_asset_01.mxf')
    print connection.rename_file(_sftp, 'C:\\workspace\\AtlasPortalAutomation\\isilon\\test media\\auto_test_media_asset_01.mxf', 'New MXF name goes here')
     
    connection.close_FTP(_sftp)
    
    
    