# https://www.codewars.com/kata/582cb0224e56e068d800003c
# 2023-04-08T14:49:00.663+0000
#!/bin/bash
time=$1
# The fun begins here.
echo "$(echo "scale=0; $time*0.5/1" | bc)"