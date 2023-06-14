# https://www.codewars.com/kata/53da3dbb4a5168369a0000fe
# 2023-06-02T08:29:10.611+0000
# TODO: solution
if [ $(expr $1 % 2) == "0" ]; then
  echo "Even"
else
  echo "Odd"
fi