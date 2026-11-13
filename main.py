import os
import shutil
from pathlib import Path

def main():
    src = Path("image.png")
    dst_dir = Path("/output")
    dst_dir.mkdir(parents=True, exist_ok=True)
    dst = dst_dir / "entry.png"
    
    shutil.copy2(src, dst)
    
    if not dst.exists():
        raise FileNotFoundError(f"Output file {dst} does not exist.")
    
    file_size = dst.stat().st_size
    max_size = 1024 * 1024  # 1 MiB
    
    if file_size > max_size:
        raise ValueError(f"File size {file_size} bytes exceeds maximum limit of 1 MiB ({max_size} bytes).")
    
    png_magic = b'\x89PNG\r\n\x1a\n'
    with open(dst, "rb") as f:
        header = f.read(8)
        
    if header != png_magic:
        raise ValueError("Invalid PNG magic bytes in output file.")
        
    print(f"Successfully copied and verified {src} to {dst}. Size: {file_size} bytes, Valid PNG.")

if __name__ == "__main__":
    main()
