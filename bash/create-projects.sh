#!/bin/bash
mkdir -p DevOps
topics=("Linux" "Git" "Docker" "Kuberenetes" "Terraform")
for topic in "${topics[@]}"
do
mkdir -p "DevOps/$topic"
echo "Created: DevOps/$topic"
done

