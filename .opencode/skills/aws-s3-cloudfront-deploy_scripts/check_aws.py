#!/usr/bin/env python3
"""
Check AWS credentials and connectivity.
Usage: python check_aws.py
"""

import subprocess
import sys

def main():
    try:
        result = subprocess.run(['aws', 'sts', 'get-caller-identity'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print('AWS credentials OK')
            return 0
        else:
            print(f'AWS Error: {result.stderr}')
            return 1
    except FileNotFoundError:
        print('Error: aws CLI not found. Install via winget install AWS.AWSCLI')
        return 1
    except Exception as e:
        print(f'Error checking AWS credentials: {e}')
        return 1

if __name__ == '__main__':
    sys.exit(main())
