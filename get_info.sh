#!/bin/bash

locate_file="/tmp/zip_job.py"
echo "OS-type= "$(cat /etc/os-release | sed -n 's/PRETTY_NAME=//p')
echo "architecture= "$(uname -m)
if [ -f "$locate_file" ];
  then
      echo "Python script exists under " $locate_file
  else
      echo "Python script can not be found under " $locate_file 
fi
