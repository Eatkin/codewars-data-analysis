# https://www.codewars.com/kata/5ae62fcf252e66d44d00008e
# 2023-05-30T19:22:41.745+0000
a=$1
b=$2
c=$3
# your code here
sum=0
maxSeen=$((a + b + c))
temp=$((a * b * c))
# Fucking stupid dumb way of doing it cause I'm terrible at Bash
if [ $temp -gt $maxSeen ]; then
  maxSeen=$temp
fi
temp=$((a + b * c))
if [ $temp -gt $maxSeen ]; then
  maxSeen=$temp
fi
temp=$(((a + b) * c))
if [ $temp -gt $maxSeen ]; then
  maxSeen=$temp
fi
temp=$((a * (b + c)))
if [ $temp -gt $maxSeen ]; then
  maxSeen=$temp
fi
temp=$((a * b + c))
if [ $temp -gt $maxSeen ]; then
  maxSeen=$temp
fi

echo $maxSeen