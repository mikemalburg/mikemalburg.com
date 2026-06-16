# Fix Gemfile.lock platform mismatch by adding x86_64-linux
import subprocess
import sys

def main():
    try:
        result = subprocess.run(["bundle", "lock", "--add-platform", "x86_64-linux"], capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
