#!/bin/bash

echo "=== Ping Google ==="
ping -c 4 google.com

echo
echo "=== Example.com HTML ==="
curl https://example.com

echo
echo "=== GitHub API ==="
curl https://api.github.com

echo
echo "=== My IP Address ==="
hostname -I

echo
echo "=== Listening Ports ==="
ss -tuln
