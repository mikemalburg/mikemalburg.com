#!/bin/bash

# Deploy mikemalburg.com to AWS S3

echo "Building Jekyll site..."
jekyll build

echo "Uploading to S3..."
aws s3 sync _site/ s3://mikemalburg.com --delete

echo "Done! Site available at:"
echo "http://mikemalburg.com.s3-website-us-east-1.amazonaws.com"
