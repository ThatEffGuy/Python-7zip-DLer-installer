from urllib.request import urlretrieve 
import os, subprocess, getpass

from urllib.request import urlretrieve
import getpass

url = 'https://www.7-zip.org/a/7z2107-x64.exe'

print('File Downloading')

usrname = getpass.getuser()
destination = f'C:\\Users\\{usrname}\\Downloads\\7z2107-x64.exe'

download = urlretrieve(url, destination)

print('File downloaded')
os.system(destination)

