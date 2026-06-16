# Add jekyll-seo-tag gem to Gemfile if not present
import subprocess
import sys

def main():
    with open("Gemfile", "r") as f:
        content = f.read()
    
    if "jekyll-seo-tag" not in content:
        print("Adding jekyll-seo-tag to Gemfile...")
        new_line = chr(10) + 'gem "jekyll-seo-tag", "~> 2.8"' + chr(10)
        content += new_line
        with open("Gemfile", "w") as f:
            f.write(content)
        
        try:
            result = subprocess.run(["C:\\Ruby31-x64\\bin\\ruby.exe", "-S", "bundle", "install"], capture_output=True, text=True, check=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error: {e.stderr}", file=sys.stderr)
            sys.exit(1)
    else:
        print("jekyll-seo-tag already in Gemfile")

if __name__ == "__main__":
    main()
