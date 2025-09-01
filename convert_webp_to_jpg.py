import os
from PIL import Image

# --- SCRIPT CONFIGURATION ---
# 1. Set the folder containing your images
IMAGE_DIRECTORY = r"C:\Users\Aorus15\Desktop\damilare" 

# 2. Set the format you want to convert FROM (e.g., ".webp", ".png")
INPUT_FORMAT = ".webp"

# 3. Set the format you want to convert TO (e.g., ".jpg", ".png")
OUTPUT_FORMAT = ".jpg"

# 4. Set the quality for the output JPG images (1-100)
JPG_QUALITY = 95
# --- END OF CONFIGURATION ---


def batch_convert_images(directory, input_ext, output_ext, quality=95):
    """
    Scans a directory for images of a specific format and converts them.
    """
    # Ensure the directory exists to avoid errors
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return

    print(f"Scanning for {input_ext} files in '{directory}'...")

    # Iterate through all files in the given directory
    for filename in os.listdir(directory):
        # Check if the file matches the input format (case-insensitive)
        if filename.lower().endswith(input_ext):
            
            # Construct the full file paths
            input_path = os.path.join(directory, filename)
            # Create the new filename by replacing the extension
            output_filename = os.path.splitext(filename)[0] + output_ext
            output_path = os.path.join(directory, output_filename)
            
            try:
                # Open the image using Pillow
                with Image.open(input_path) as img:
                    # If the output is JPG, convert to RGB mode first
                    # This removes any transparency (alpha channel) which JPG doesn't support
                    if output_ext.lower() == ".jpg" or output_ext.lower() == ".jpeg":
                        img = img.convert("RGB")
                    
                    # Save the new image in the desired format
                    img.save(output_path, quality=quality)
                
                print(f"Successfully converted {filename} to {output_filename}")

            except Exception as e:
                print(f"Could not convert {filename}. Error: {e}")

# This block ensures the script runs only when executed directly
if __name__ == "__main__":
    batch_convert_images(IMAGE_DIRECTORY, INPUT_FORMAT, OUTPUT_FORMAT, JPG_QUALITY)
    print("\nConversion process completed.")
