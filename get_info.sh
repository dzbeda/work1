#!/bin/bash

locate_file="/tmp/zip_job.py"
echo "OS-type= "$(cat /etc/os-release | sed -n 's/PRETTY_NAME=//p')
echo "architecture= "$(uname -m)
if [ -f "$locate_file" ];
  then
      echo $locate_file "File exists"
  else
      echo $locate_file "File can not be found"
fi
