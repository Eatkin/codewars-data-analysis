# https://www.codewars.com/kata/56541980fa08ab47a0000040
# 2023-04-23T09:51:29.146+0000
#!/bin/bash
printerError() {
    echo $(echo $1 | grep -o [^a-m] | wc -l)"/"${#1}
}
printerError $1