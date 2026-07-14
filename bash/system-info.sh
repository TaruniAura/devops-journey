#!/bin/bash
echo "What is your name?"
read name
echo "Hello, $name!"
echo "Current directory:"
pwd
echo "Today's date:"
date "+%a %b %d %H:%M:%S %Z %Y"
echo "Counting:"
for i in {1..5}
do
	echo $i
done
echo "Done!"



