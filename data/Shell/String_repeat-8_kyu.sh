# https://www.codewars.com/kata/57a0e5c372292dd76d000d7e
# 2023-03-27T12:31:12.252+0000
#!/bin/bash
repeat=$1
string=$2

i=1
concat_str=""
while [ $i -le $repeat ]
do
  concat_str=$concat_str$string
  i=$((i+1))
done

echo $concat_str