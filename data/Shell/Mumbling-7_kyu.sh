# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039
# 2023-06-02T08:53:59.411+0000
#!/bin/bash
accum () {
    str=""
    num=0
    for (( i=0; i<${#1}; i++ )); do
      char=${1:$i:1}
      str+=${char^}
      for (( j=0; j<$num; j++ )); do
        str+=${char,,}
      done
      str+="-"
      ((num++))
    done
    # Remove final character because there's an extra hyphen
    echo ${str::-1}
}
accum "$1"