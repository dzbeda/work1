import logging
import os
import zipfile
from pathlib import Path
import time

                                                    ## Functions ##

def create_file(full_file_name):
    with open(full_file_name,'w+') as f:
    #time.sleep(20)  #Using sleep will give you the option to delete the file manually in order to check the if statment in case the file was not created
        if os.path.exists(full_file_name) == True:
            print("Created filename: " + filename + file_extension + " under " + file_path)
            logging.info("Created filename: " + filename + file_extension + " under " + file_path)
        else:
            print("Failed to create file  - exiting")
            logging.error("Could not create filename: " + filename + file_extension + " under " + file_path + " exiting")
            exit()

def create_zip(zip_file_name,full_file_name):

    handle = zipfile.ZipFile(zip_file_name,"w")
    handle.write(full_file_name,compress_type= zipfile.ZIP_DEFLATED)
    handle.close()
    #time.sleep(20)  #Using sleep will give you the option to delete the file manually in order to check the if statment in case the file was not created
    if os.path.exists(zip_file_name) == True:
        print("Zip file was created under : " + zip_file_name)
        logging.info("Zip file was created under : " + zip_file_name)
    else:
        print("Failed to create file  - exiting")
        logging.error("Could not create file under : " + zip_file_name + " exiting")
        exit()

                                             ####  variables   #####
## Log file parameters ##
logFile = '/tmp/output.log'
logging.basicConfig(filename=logFile,filemode='w',format='%(asctime)s - %(levelname)s - %(message)s' , level=logging.INFO)


## Program variables ##
files = {'a','b','c','d'}
file_extension= '.txt'
file_path='/tmp/'  #define the path were txt files will be created
version=os.getenv('VERSION')
zip_file_path= '/zip/'   #define the path were zip files will be created


                                                        ## Start program ##

## Check if env Version exists
if os.getenv('VERSION') is not None:
    print(version)
    version = os.getenv('VERSION')
    logging.info("Running version is: " + version)
else:
    print("env VERSION is not defined - exiting")
    logging.error("env VERSION is not defined - exiting")
    exit()

# ## Create folder if are not exists - This is required when running the script as standalone
#
# Path(file_path).mkdir(parents=True, exist_ok=True)
# Path(zip_file_path).mkdir(parents=True, exist_ok=True)
# os.chmod(zip_file_path, 0o777)

## Generate files

for filename in files:
    full_file_name = file_path+filename+file_extension
    create_file(full_file_name)
    zip_file_name = zip_file_path+filename+"_"+version+".zip"
    create_zip(zip_file_name,full_file_name)
