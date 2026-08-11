#!/bin/bash

echo "===== Linux Process Commands Demo ====="

echo
echo "1. Current shell processes:"
ps

echo
echo "2. All running processes (first 10):"
ps -ef | head

echo
echo "3. Running a background process..."
sleep 10 &

echo
echo "4. Current jobs:"
jobs

echo
echo "5. Processes containing 'sleep':"
ps -ef | grep sleep

echo
echo "6. Killing sleep process..."
pkill sleep

echo
echo "7. Jobs after killing:"
jobs

echo
echo "Demo completed."
