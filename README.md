# Image Converter Tool

A simple and powerful tool to convert WebP, PNG, AVIF, TIFF, HEIC, and other image formats to JPG/PNG/WebP with optimization.

[日本語版はこちら](README_ja.md)

## Features

- Convert various image formats (WebP, PNG, AVIF, TIFF, HEIC/HEIF, BMP, GIF, JPEG)
- Output to JPG, PNG, or WebP
- Automatic image optimization
- Easy-to-use batch file for Windows
- Support for iPhone HEIC images
- Optional external optimizer integration (pngquant, optipng, jpegtran)

## Quick Start

### Using simple_converter.bat (Windows)

1. Double-click `simple_converter.bat`
2. Select an option from the menu:

```
[1] Convert single image
[2] Convert all images in a folder
[3] Exit
```

#### Single File Conversion

1. Select option `1`
2. Drag and drop your image file
3. Choose output format (1-4)
4. Done! The converted file will be saved with `_converted` suffix

#### Batch Folder Conversion

1. Select option `2`
2. Drag and drop a folder containing images
3. Choose output format (1-4)
4. All images will be converted to a new `converted_[format]` folder

## Output Formats

| Option | Format | Quality | Use Case |
|--------|--------|---------|----------|
| 1 | JPG | 95% | High quality, printing |
| 2 | JPG | 85% | Standard, recommended |
| 3 | PNG | Optimized | Transparency preservation |
| 4 | WebP | 90% | High quality, small size |

## Supported Formats

**Input**: WebP, PNG, AVIF, TIFF, HEIC/HEIF (iPhone), BMP, GIF, JPEG

**Output**: JPG, PNG, WebP

## Output Location

### Single File
Saved in the same location as the original with `_converted` suffix.

Example: `photo.webp` → `photo_converted.jpg`

### Multiple Files
A new folder `converted_[format]` is created in the original folder.

## Requirements

- Windows 10/11 (or Python 3.7+ for other OS)
- Python 3.7 or later
- Pillow, pillow-heif (auto-installed)

### Installing Python

Download from: https://www.python.org/downloads/

**Important**: Check "Add Python to PATH" during installation!

### Installing Dependencies

```bash
python -m pip install Pillow pillow-heif
```

Or use the requirements file:

```bash
pip install -r requirements.txt
```

## Advanced Usage

### Command Line Batch Conversion

```bash
cd /path/to/image-converter
python convert_image.py /path/to/images/*.webp -f jpg -q 95
```

### Command Line Options

```bash
python convert_image.py [files...] [options]

Options:
  -f, --format {jpg,png,webp}  Output format (default: jpg)
  -q, --quality 0-100          Quality level (default: 95)
```

### Enhanced Compression (Optional)

Place the following tools in the `tools` folder for enhanced compression:

- `pngquant.exe` - PNG color quantization (50-70% size reduction)
- `optipng.exe` - PNG lossless optimization (5-20% additional reduction)
- `jpegtran.exe` - JPEG lossless optimization (5-15% reduction)

See [tools/README.md](tools/README.md) for details.

## Troubleshooting

### Error Messages

Open Command Prompt and run:

```cmd
python -m pip install --upgrade pip
python -m pip install Pillow pillow-heif
```

### Conversion Fails

1. Check if Python is installed: `python --version`
2. Verify file path contains no special characters
3. Confirm file format is supported

### Module Not Found Error

```bash
pip install --upgrade pillow pillow-heif
```

## Project Structure

```
image-converter/
├── convert_image.py         # Main conversion script
├── simple_converter.bat     # Windows batch interface
├── requirements.txt         # Python dependencies
├── README.md               # This file (English)
├── README_ja.md            # Japanese documentation
├── LICENSE                 # MIT License
└── tools/                  # Optional optimization tools
    └── README.md           # Tools installation guide
```

## Use Cases

- Convert iPhone HEIC photos to JPG
- Batch convert WebP images for compatibility
- Optimize images for web use
- Convert modern formats (AVIF) to standard formats
- Reduce image file sizes while maintaining quality

## Technical Details

- Handles transparency by converting to white background for JPG
- Progressive JPEG encoding for faster web loading
- Metadata preservation options
- Color space conversion (RGBA → RGB)
- Quality-based compression control

## License

MIT License - See [LICENSE](LICENSE) file for details

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## Support

If you encounter any issues:
1. Check the [Troubleshooting](#troubleshooting) section
2. Verify all requirements are installed
3. Open an issue on GitHub

## Credits

Built with:
- [Pillow](https://python-pillow.org/) - Python Imaging Library
- [pillow-heif](https://github.com/bigcat88/pillow_heif) - HEIF support for Pillow

## Version History

- **v1.0** - Initial release with basic conversion
- Support for WebP, PNG, AVIF, TIFF, HEIC, BMP, GIF, JPEG
- Optional external optimizer integration
- Windows batch interface
