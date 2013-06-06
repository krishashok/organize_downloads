#!/usr/bin/python
import sys
import os
from datetime import datetime
import shutil

required_directories_and_filetypes = {'images':['jpg','jpeg','png','tiff','psd','bmp'],
                                        'audio':['mp3','m4a','wav'],
                                        'video':['avi','mpg','mpeg','m4v','3gp','mp4','mkv'],
                                        'archives':['zip','rar','gz'],
                                        'documents':['doc', 'docx', 'ppt', 'pptx', 'pdf', 'xls', 'xlsx', 'txt','epub'],
                                        'installables':['dmg','pkg','ipa', 'apk'],
                                        'extracted':[]
                                        }


LOGFILENAME = "organize_downloads.log"
ERRORFILENAME = "organizer_downloads_error.log"


def makedir_ifnotexists(dir):
    # Make a directory if it doesn't exist

    if not os.path.exists(dir):
        os.makedirs(dir) 


def initial_setup():
    # Check if folders named images, audio etc already exist in our working directory. 
    # If they do, use them, otherwise create them
    
    map(lambda dir: makedir_ifnotexists(dir),required_directories_and_filetypes.keys())


def process_files():

    logfile = open(LOGFILENAME, 'a+')
    errorfile = open(ERRORFILENAME, 'a+')

    for f in os.listdir('.'):

        # if it's a file, then check extension and do blah blah

        if not os.path.isdir(f):

            extension = f.split('.')[-1].lower()
            if extension in required_directories_and_filetypes['images']:
                try:
                    shutil.move(f, 'images')
                    log(f, 'images',logfile)
                except Exception as e:
                    errorfile.write(str(e)+"\n")
            elif extension in required_directories_and_filetypes['documents']:
                try:
                    shutil.move(f,'documents')
                    log(f,'documents',logfile)
                except Exception as e:
                    errorfile.write(str(e)+"\n")
            elif extension in required_directories_and_filetypes['audio']:
                try:
                    shutil.move(f,'audio')
                    log(f,'audio',logfile)
                except Exception as e:
                    errorfile.write(str(e)+"\n")
            elif extension in required_directories_and_filetypes['archives']:
                try:
                    shutil.move(f,'archives')
                    log(f,'archives',logfile)
                except Exception as e:
                    errorfile.write(str(e)+"\n")
            elif extension in required_directories_and_filetypes['installables']:
                try:
                    shutil.move(f,'installables')
                    log(f,'installables',logfile)
                except Exception as e:
                    errorfile.write(str(e)+"\n")
            elif extension in required_directories_and_filetypes['video']:
                try:
                    shutil.move(f,'video')
                    log(f,'video',logfile)
                except Exception as e:
                    errorfile.write(str(e)+"\n")

        else:

            # it's a directory! Move it to the "Extracted" directory if it's not one of our standard directories
            if f not in required_directories_and_filetypes.keys():
                try:
                    shutil.move(f,'extracted')
                    log(f,'extracted',logfile)
                except Exception as e:
                    errorfile.write(str(e)+"\n")


    logfile.close()
    errorfile.close()
    

def log(filename,folder, logfile):
    # When a file is moved successfully, log it so that we can undo shit later

    logfile.write("%s\t%s\t%s\n" % (filename, folder, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    
    

def main():

    # Do an initial setup to see if the subfolders we need are there and create them if required
    initial_setup()

    # Process files in the current directory now
    process_files()


if __name__ == '__main__':
    main()
