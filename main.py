import os
import shutil
from pathlib import Path

def main():
    src = Path("image.png")
    dst_dir = Path("/output")
    dst_dir.mkdir(parents=True, exist_ok=True)
    dst = dst_dir / "entry.png"
    
    shutil.copy2(src, dst)
    print(f"Copied {src} to {dst}")

if __name__ == "__main__":
    main()
