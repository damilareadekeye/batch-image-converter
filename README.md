# 🖼️ Batch Image Format Converter

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/)
[![Pillow](https://img.shields.io/badge/Pillow-Latest-green.svg)](https://python-pillow.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](https://github.com/damilareadekeye/batch-image-converter)

A powerful Python-based utility that automates bulk image format conversions between WebP, JPG, PNG, and more. Say goodbye to manual image conversions and hello to efficiency!

## 📖 Full Documentation

For a comprehensive guide with visual demonstrations and detailed explanations, check out:
- **Portfolio Article**: [damilareadekeye.com/works/software/batch-image-converter](https://damilareadekeye.com/works/software/batch-image-converter)
- **Medium Article**: [Stop Converting Images Manually: Build a Universal Image Converter with a Simple Python Script](https://damilareadekeye.medium.com/stop-converting-images-manually-build-a-universal-image-converter-with-a-simple-python-script-75728e474e6d)

## ✨ Features

- 🚀 **Batch Processing**: Convert multiple images in one go
- 🎯 **Format Flexibility**: Support for WebP, JPG, PNG, BMP, GIF, TIFF, and more
- ⚙️ **Configurable Quality**: Fine-tune output quality (1-100)
- 🛡️ **Error Handling**: Robust error recovery for corrupted files
- 🎨 **Smart Conversion**: Automatic RGB mode for JPEG compatibility
- 💻 **Cross-Platform**: Works on Windows, macOS, and Linux
- 📊 **Progress Tracking**: Real-time conversion status updates

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher
- Pillow library (PIL fork)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/damilareadekeye/batch-image-converter.git
cd batch-image-converter
```

2. Install required dependencies:
```bash
pip install Pillow
```

3. Configure the script by editing the configuration section in `convert_webp_to_jpg.py`:
```python
# --- SCRIPT CONFIGURATION ---
IMAGE_DIRECTORY = r"C:\path\to\your\images"  # Your image folder
INPUT_FORMAT = ".webp"                        # Format to convert FROM
OUTPUT_FORMAT = ".jpg"                        # Format to convert TO
JPG_QUALITY = 95                              # Quality (1-100)
```

4. Run the script:
```bash
python convert_webp_to_jpg.py
```

## 📋 Usage Example

```bash
$ python convert_webp_to_jpg.py

Scanning for .webp files in 'C:\Users\YourName\Desktop\images'...
Successfully converted image1.webp to image1.jpg
Successfully converted image2.webp to image2.jpg
Successfully converted image3.webp to image3.jpg

Conversion process completed.
```

## 🔧 Configuration Options

| Parameter | Description | Example |
|-----------|-------------|---------|
| `IMAGE_DIRECTORY` | Path to folder containing images | `C:\Users\Desktop\images` |
| `INPUT_FORMAT` | Source image format | `.webp`, `.png`, `.bmp` |
| `OUTPUT_FORMAT` | Target image format | `.jpg`, `.png`, `.gif` |
| `JPG_QUALITY` | JPEG quality setting (1-100) | `95` (high quality) |

## 📂 Project Structure

```
batch-image-converter/
│
├── convert_webp_to_jpg.py    # Main conversion script
├── README.md                  # Documentation
├── LICENSE                    # MIT License
└── examples/                  # Example images
    ├── input/                 # Sample input images
    └── output/                # Converted output images
```

## 🎯 Use Cases

- **Web Development**: Convert modern WebP images to JPG/PNG for broader browser compatibility
- **Content Management**: Standardize image formats across different platforms
- **Storage Optimization**: Convert lossless formats to compressed JPEG with controlled quality
- **E-commerce**: Prepare product images for various marketplace requirements
- **Documentation**: Convert screenshots to appropriate formats
- **Social Media**: Format images for platform-specific requirements

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔮 Future Enhancements

- [ ] GUI interface using Tkinter or PyQt
- [ ] Multi-threading for parallel processing
- [ ] Image resizing and cropping options
- [ ] Configuration profiles for common scenarios
- [ ] EXIF metadata preservation
- [ ] Recursive directory processing
- [ ] Command-line argument support
- [ ] Detailed conversion logging

## 👨‍💻 Author

**Damilare Lekan Adekeye**

- 🌐 Portfolio: [damilareadekeye.com](https://damilareadekeye.com)
- 📧 Contact: [damilareadekeye.com/contact](https://damilareadekeye.com/contact)
- 💼 GitHub: [@damilareadekeye](https://github.com/damilareadekeye)
- 📝 Medium: [@damilareadekeye](https://damilareadekeye.medium.com)
- 🐦 Twitter: [@damilareadekeye](https://twitter.com/deewansonic)
- 💼 LinkedIn: [damilareadekeye](https://linkedin.com/in/damilareadekeye)

## 🙏 Acknowledgments

- [Pillow (PIL Fork)](https://python-pillow.org/) - The friendly PIL fork
- Python community for continuous support
- All contributors and users of this tool

## 📊 Stats

![Python](https://img.shields.io/badge/Python-100%25-blue.svg)
![Code Quality](https://img.shields.io/badge/Code%20Quality-A%2B-brightgreen.svg)
![Maintained](https://img.shields.io/badge/Maintained-Yes-green.svg)

---

⭐ **If you find this tool useful, please consider giving it a star on GitHub!**

🐛 **Found a bug?** Please open an issue with a detailed description.

💡 **Have a feature request?** Feel free to suggest new features in the issues section.

---

<p align="center">
  Made with ❤️ by <a href="https://damilareadekeye.com">Damilare Lekan Adekeye</a>
</p>
