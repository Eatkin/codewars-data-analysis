# https://www.codewars.com/kata/526571aae218b8ee490006f4
# 2023-06-02T08:36:06.915+0000
#!/bin/bash
n=$1
echo "$(echo "ibase=10;obase=2;$n" | bc | sed "s/0//g" | wc -c) - 1" | bc