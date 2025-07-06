#!/usr/bin/env python3
import PyInstaller.__main__
import platform
import shutil
import os

# Configuration
script_name = "openwebui_gui_converter.py"
app_name = "OpenWebUI Chat Exporter"
icon_path = "Icons/app_icon.icns"  # Create or get an .icns (macOS), .ico (Windows), or .png (Linux)

# Platform-specific settings
system = platform.system()
if system == "Windows":
    icon = icon_path.replace(".icns", ".ico")
    extra_args = ["--windowed"]
elif system == "MacOS":  # macOS
    icon = icon_path
    extra_args = ["--windowed", "--osx-bundle-identifier", "com.gameDirection.openwebuiconverter"]
else:  # Linux
    icon = icon_path.replace(".icns", ".png")
    extra_args = []

# PyInstaller command
PyInstaller.__main__.run([
    script_name,
    "--name=%s" % app_name,
    "--icon=%s" % icon,
    "--onefile",
    "--noconsole",
    "--add-data=app_icon.icns:." if system == "Darwin" else "",
    *extra_args,
    "--clean"
])

# Clean up and organize builds
print("\nOrganizing build files...")
build_dir = "dist"
platform_dir = os.path.join("builds", system)

os.makedirs(platform_dir, exist_ok=True)

# Move the executable
if system == "MacOS":
    app_path = os.path.join("dist", f"{app_name}.app")
    target_path = os.path.join(platform_dir, f"{app_name}.app")
    shutil.move(app_path, target_path)
    print(f"macOS app bundle created at: {target_path}")
else:
    exe_ext = ".exe" if system == "Windows" else ""
    exe_name = f"{app_name}{exe_ext}"
    source = os.path.join("dist", exe_name)
    target = os.path.join(platform_dir, exe_name)
    shutil.move(source, target)
    print(f"Executable created at: {target}")

print("Build complete!")
