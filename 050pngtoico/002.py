from PIL import Image
import os
import win32api
import win32con
import win32gui

def make_icon(png_file, icon_file, size=(128, 128)):
    try:
        img = Image.open(png_file)
        img = img.resize(size)
        
        img.save(icon_file)
        print(f"Converted {png_file} to {icon_file}")
    except Exception as e:
        print(f"Error converting {png_file}: {e}")

def main():
    png_files = [f for f in os.listdir('.') if f.endswith('.png')]
    if not png_files:
        print("No PNG files found in the current directory.")
        return
    
    size = (128, 128)  # Adjust the size as needed
    for png_file in png_files:
        icon_file = os.path.splitext(png_file)[0] + ".ico"
        make_icon(png_file, icon_file, size)
        # Set the icon for the file
        win32api.SetFileAttributes(png_file, win32con.FILE_ATTRIBUTE_NORMAL)
        win32gui.ExtractIconEx(icon_file, 0)

if __name__ == "__main__":
    main()

