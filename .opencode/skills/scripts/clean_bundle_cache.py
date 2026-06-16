# Fix bundle cache corruption by deleting vendor/bundle and reinstalling
import subprocess
import sys
import shutil
import os

def main():
    bundle_path = "vendor/bundle"
    
    if os.path.exists(bundle_path):
        print(f"Removing {bundle_path}...")
        shutil.rmtree(bundle_path)
    
    gemfile_lock = "Gemfile.lock"
    if os.path.exists(gemfile_lock):
        print("Removing Gemfile.lock...")
        os.remove(gemfile_lock)
    
    ruby_path = "C:\\Ruby31-x64\\bin\\ruby.exe"
    try:
        result = subprocess.run([ruby_path, "-S", "bundle", "install"], capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
