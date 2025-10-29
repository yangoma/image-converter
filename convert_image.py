#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
画像変換スクリプト
複数の画像フォーマットに対応し、圧縮最適化も行います
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path
from PIL import Image
import pillow_heif  # HEIF/HEIC対応

# 対応フォーマット
SUPPORTED_INPUT_FORMATS = {'.webp', '.png', '.avif', '.tiff', '.tif', '.bmp', 
                           '.jpg', '.jpeg', '.gif', '.heic', '.heif'}

class ImageConverter:
    def __init__(self, output_format='jpg', quality=95, suffix='_converted'):
        self.output_format = output_format.lower()
        self.quality = quality
        self.suffix = suffix
        self.tools_dir = Path(__file__).parent / 'tools'
        
    def convert_image(self, input_path):
        """Convert image"""
        input_path = Path(input_path)
        
        if not input_path.exists():
            print(f"Error: File not found - {input_path}")
            return None
            
        if input_path.suffix.lower() not in SUPPORTED_INPUT_FORMATS:
            print(f"Skip: Unsupported format - {input_path}")
            return None
        
        # Generate output filename
        output_path = input_path.parent / f"{input_path.stem}{self.suffix}.{self.output_format}"
        
        try:
            # Open HEIC files with pillow_heif
            if input_path.suffix.lower() in {'.heic', '.heif'}:
                heif_file = pillow_heif.read_heif(str(input_path))
                image = Image.frombytes(
                    heif_file.mode,
                    heif_file.size,
                    heif_file.data,
                    "raw",
                )
            else:
                image = Image.open(input_path)
            
            # Convert RGBA to RGB (for JPG)
            if self.output_format in ['jpg', 'jpeg'] and image.mode in ['RGBA', 'LA', 'P']:
                # White background for transparency
                background = Image.new('RGB', image.size, (255, 255, 255))
                if image.mode == 'P':
                    image = image.convert('RGBA')
                background.paste(image, mask=image.split()[-1] if image.mode in ['RGBA', 'LA'] else None)
                image = background
            
            # Save
            save_kwargs = self._get_save_kwargs()
            image.save(output_path, **save_kwargs)
            
            print(f"✓ Converted: {input_path.name} -> {output_path.name}")
            
            # Optimization
            if self.output_format in ['jpg', 'jpeg']:
                self._optimize_jpeg(output_path)
            elif self.output_format == 'png':
                self._optimize_png(output_path)
            
            return output_path
            
        except Exception as e:
            print(f"✗ Error: {input_path.name} - {str(e)}")
            return None
    
    def _get_save_kwargs(self):
        """フォーマット別の保存オプション"""
        if self.output_format in ['jpg', 'jpeg']:
            return {
                'format': 'JPEG',
                'quality': self.quality,
                'optimize': True,
                'progressive': True
            }
        elif self.output_format == 'png':
            return {
                'format': 'PNG',
                'optimize': True
            }
        elif self.output_format == 'webp':
            return {
                'format': 'WEBP',
                'quality': self.quality,
                'method': 6  # 最高品質の圧縮
            }
        else:
            return {'format': self.output_format.upper()}
    
    def _optimize_jpeg(self, file_path):
        """Optimize JPEG"""
        # Optimize with jpegtran if available
        jpegtran = self.tools_dir / 'jpegtran.exe'
        if jpegtran.exists():
            try:
                temp_path = file_path.with_suffix('.tmp')
                subprocess.run([
                    str(jpegtran),
                    '-copy', 'none',
                    '-optimize',
                    '-progressive',
                    '-outfile', str(temp_path),
                    str(file_path)
                ], check=True, capture_output=True)
                temp_path.replace(file_path)
                print(f"  -> jpegtran optimized")
            except:
                pass
    
    def _optimize_png(self, file_path):
        """Optimize PNG"""
        # Quantize with pngquant if available
        pngquant = self.tools_dir / 'pngquant.exe'
        if pngquant.exists():
            try:
                subprocess.run([
                    str(pngquant),
                    '--quality=85-95',
                    '--speed', '1',
                    '--force',
                    '--output', str(file_path),
                    str(file_path)
                ], check=True, capture_output=True)
                print(f"  -> pngquant optimized")
            except:
                pass
        
        # Optimize with optipng if available
        optipng = self.tools_dir / 'optipng.exe'
        if optipng.exists():
            try:
                subprocess.run([
                    str(optipng),
                    '-o7',  # Maximum level
                    '-quiet',
                    str(file_path)
                ], check=True, capture_output=True)
                print(f"  -> optipng optimized")
            except:
                pass

def process_files(files, output_format='jpg', quality=95):
    """Process multiple files"""
    files = [Path(f) for f in files if Path(f).exists()]
    
    if not files:
        print("No files to process")
        return
    
    # Create folder for multiple files
    if len(files) > 1:
        output_dir = files[0].parent / f"converted_{output_format}"
        output_dir.mkdir(exist_ok=True)
        print(f"Output folder: {output_dir}")
        
        # Convert without suffix for moving to output folder
        converter = ImageConverter(output_format, quality, '')
        
        for file in files:
            result = converter.convert_image(file)
            if result and result.exists():
                # Move to output folder
                final_path = output_dir / result.name
                result.replace(final_path)
    else:
        # Single file: save with suffix in same location
        converter = ImageConverter(output_format, quality, '_converted')
        converter.convert_image(files[0])
    
    print("\nProcessing complete!")

def main():
    parser = argparse.ArgumentParser(description='Image Conversion Tool')
    parser.add_argument('files', nargs='+', help='Image files to convert')
    parser.add_argument('-f', '--format', default='jpg', 
                       choices=['jpg', 'jpeg', 'png', 'webp'],
                       help='Output format (default: jpg)')
    parser.add_argument('-q', '--quality', type=int, default=95,
                       help='Quality 0-100 (default: 95)')
    
    args = parser.parse_args()
    
    print(f"=== Image Conversion Tool ===")
    print(f"Output format: {args.format.upper()}")
    print(f"Quality: {args.quality}")
    print(f"Files: {len(args.files)}\n")
    
    # Debug: Show all files
    print("Files to convert:")
    for f in args.files:
        print(f"  - {f}")
        if not Path(f).exists():
            print(f"    WARNING: File does not exist!")
    print()
    
    process_files(args.files, args.format, args.quality)

if __name__ == '__main__':
    main()
