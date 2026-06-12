#!/bin/bash

set -e

BUCKET="mikemalburg.com"
REGION="us-east-1"

echo "Building Jekyll site..."
jekyll build

echo "Creating S3 bucket if not exists..."
aws s3 mb s3://$BUCKET 2>/dev/null || echo "Bucket may already exist"

echo "Configuring static website hosting..."
aws s3 website s3://$BUCKET --index-document index.html --error-document error.html

echo "Uploading files to S3..."
aws s3 sync _site/ s3://$BUCKET --delete

echo "Setting bucket policy..."
aws s3api put-bucket-policy --bucket $BUCKET --policy file://s3-policy.json

echo "Done! Site available at:"
echo "http://$BUCKET.s3-website-$REGION.amazonaws.com"
