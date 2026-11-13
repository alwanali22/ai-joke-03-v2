import os
import sys

def main():
    joke = 'The AI\'s solution is a 1000-line script that just returns true.'
    
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    output_path = os.path.join(output_dir, "entry.txt")
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(joke)

if __name__ == "__main__":
    main()
