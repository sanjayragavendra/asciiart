# ASCII Art Generator

Convert any image into ASCII art directly in your terminal with color support.

Python Version: 3.13+
License: MIT
Platform: Windows | Linux | Mac

## Features

- Colored ASCII Output - Vibrant colored ASCII art in terminal
- Monochrome Mode - Classic black and white ASCII art
- Save to File - Export monochrome ASCII art to text files
- Local Image Support - Convert images from your computer
- URL Support - Convert images directly from web URLs
- Error Handling - Robust input validation and error messages
- Fast Processing - Quick conversion even for large images

## Requirements

- Python 3.13 or higher
- Internet connection (for URL image loading)

## Installation

### 1. Clone the repository

git clone https://github.com/sanjayragavendra/asciiart.git
cd asciiart

### 2. Install required packages

pip install ascii_magic pillow requests

Or install all at once:

pip install -r requirements.txt

## Usage

### Run the program

python ImgArt.py

### Follow the interactive prompts:

1. Choose image source:
   - l - Load a local image file
   - u - Load an image from a URL

2. Choose output style:
   - c - Colored ASCII (terminal only)
   - m - Monochrome ASCII (can save to file)

3. For monochrome mode:
   - Choose to save the output as a text file
   - Files are saved to your Downloads folder

## Examples

### Colored Output

Enter choice: l
Path: C:\Users\YourName\Pictures\photo.jpg
Style: c

Displays colored ASCII art directly in terminal

### Monochrome with Save

Enter choice: u
URL: https://example.com/image.jpg
Style: m
Save? y
Filename: my_art

Creates: Downloads/my_art.txt

## Supported Image Formats

- JPEG / JPG
- PNG
- GIF
- BMP
- WebP
- And other formats supported by PIL

## How It Works

1. Loads image from local path or URL
2. Resizes image for optimal ASCII conversion
3. Maps pixel brightness/colors to ASCII characters
4. For colored mode: Preserves RGB values with ANSI codes
5. For monochrome mode: Uses character density mapping
6. Displays result in terminal (and saves if requested)

## Project Structure

asciiart/
├── ImgArt.py          # Main application file
├── README.md          # This file
└── requirements.txt   # Python dependencies

## Troubleshooting

### Common Issues and Solutions

Issue: ModuleNotFoundError: No module named 'ascii_magic'

Solution: pip install ascii_magic

Issue: AttributeError: 'PngImageFile' object has no attribute 'read'

Solution: Make sure you're passing file paths, not Image objects

Issue: Cannot save colored output to file

Note: Colored output contains ANSI escape codes and can't be saved as plain text

Issue: URL images not loading

- Check your internet connection
- Ensure URL points directly to an image file
- Some websites may block automated requests

## Tips

- For best results, use images with high contrast
- Large images may take longer to process
- Colored mode looks best in terminals that support ANSI colors
- Windows Terminal, PowerShell, and most Linux terminals work great

## Customization

You can modify these parameters in the code:
- ASCII character sets (in ascii_magic configuration)
- Image resize dimensions
- Output width/height

## License

This project is open source and available under the MIT License.

## Author

Sanjay Ragavendra
GitHub: https://github.com/sanjayragavendra

## Acknowledgments

- Built with ascii_magic library
- Image processing by Pillow

## Support

If you found this project helpful, please give it a star on GitHub.

---

Made by Sanjay Ragavendra
