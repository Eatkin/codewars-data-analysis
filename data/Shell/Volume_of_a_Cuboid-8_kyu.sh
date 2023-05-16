# https://www.codewars.com/kata/58261acb22be6e2ed800003a
# 2023-03-29T09:01:36.238+0000
#!/bin/bash
length=$1
width=$2
height=$3

volume=$(echo "$length * $width * $height" |bc)

echo $volume