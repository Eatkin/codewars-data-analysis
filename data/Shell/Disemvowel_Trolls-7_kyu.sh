# https://www.codewars.com/kata/52fba66badcd10859f00097e
# 2023-06-02T08:18:59.244+0000
#!/bin/bash

# your code here #input text as $1,output as result
echo $1 | sed 's/[aeiou]//gI'