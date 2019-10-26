#!/bin/bash

# taken from https://digifesto.com/2013/04/16/bash-script-for-converting-all-wav-files-in-a-directory-to-mp3/

SAVEIF=$IFS
IFS=$(echo -en "\n\b")

for file in $(ls *wav)
do
  name=${file%%.wav}
  lame -V0 -h -b 160 --vbr-new $name.wav $name.mp3
done


IFS=$SAVEIFS
