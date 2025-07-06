# OpenWebUI_JATT
This converts OpenWebUI json export to individual text files for your journaling apps or easier refrence.

---

![App Icon](app_icon.png)  
*Convert Open WebUI chat exports to organized text files with this cross-platform tool*

## Features

- 🖥️ **GUI Interface** - Easy-to-use graphical interface
- 📂 **Batch Processing** - Convert multiple conversations at once
- ⏱️ **Timestamp Preservation** - Maintains original message timestamps
- 🏫 **Cross-Platform** - Works on Windows, macOS, and Linux
- 🎚️ **Custom Output** - Choose your output directory

## Installation

### Method 1: Download Prebuilt Binaries

Download the latest release for your OS:

- [Windows (.exe)]()
- [macOS (.app)]()
- [Linux (executable)]()

### Method 2: Run from Source

1. Ensure you have Python 3.8+ installed
2. Install dependencies:
   ```bash
   pip install tkinter
   ```
3. Download the script:
   ```bash
   wget https://raw.githubusercontent.com/yourrepo/openwebui_gui_converter.py
   ```

## Usage

### Graphical Interface (Recommended)
1. Launch the application
2. Click "Select JSON Export File"
3. Choose output directory (optional)
4. Click "Convert to TXT"

![GUI Screenshot](gui_screenshot.png)

### Command Line
```bash
python3 openwebui_gui_converter.py path/to/export.json --output custom_output_dir
```

## Output Format

Each conversation is saved as a separate `.txt` file with this structure:
```
=== Conversation Title ===

[2023-01-01 12:00:00] You: Hello AI!
[2023-01-01 12:00:05] AI: Hello human!

========================================
```

## Building from Source

To compile for your platform:

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```
2. Run the build script:
   ```bash
   python build.py
   ```

Built files will appear in `builds/[your_os]/`

## Requirements

- Python 3.8+
- Tkinter (usually included with Python)
- 50MB disk space

## Troubleshooting

**Problem**: "TKinter not found"  
**Solution**:
- Windows: Install [ActiveState Tcl/Tk](https://www.activestate.com/products/tcl/)
- macOS: `brew install python-tk`
- Linux: `sudo apt-get install python3-tk`

**Problem**: Blank output files  
**Solution**: Ensure your JSON export isn't corrupted

## Support

For issues or feature requests:
- [Open a GitHub Issue]()
- Email: support@gamedirection.net

---

Developed by [GameDirection LLC](https://gamedirection.net)  
© 2025 Alexander Sierputowski
