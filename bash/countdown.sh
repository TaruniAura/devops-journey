#!/bin/bash
echo "Enter a number:"
read num
for ((i=1; i<=10; i++))
do
	result=$((num * i))
	echo "$num * $i = $result"
done


