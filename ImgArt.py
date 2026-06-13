import os
import requests
from ascii_magic import AsciiArt, from_image
from PIL import Image
import io

def save(output_art, color_choice):
    """Save the ASCII art to a text file"""
    if color_choice == "m":
        save_choice = input("\n\nSave to a text file? <y/n>: ").lower()
        if save_choice == "y":
            filename = input("Enter file name (without extension):\t")
            # Remove any invalid characters from filename
            filename = "".join(c for c in filename if c.isalnum() or c in (' ', '-', '_')).rstrip()
            if not filename:
                filename = "ascii_art"
            
            filepath = f"{os.environ['USERPROFILE']}/Downloads/{filename}.txt"
            output_art.to_file(filepath)
            print(f"Image saved as a text file in the 'Downloads' directory as {filename}.txt")
        elif save_choice == "n":
            print("Image not saved")
        else:
            print("Not a valid choice. Image not saved.")

def generate(image_path, color_choice):
    """Generate and display ASCII art from image"""
    try:
        os.system('cls')  # Clear screen
        
        if color_choice == "c":
            # Create colored ASCII art
            output = from_image(image_path)
            output.to_terminal()
            return output
            
        elif color_choice == "m":
            # Create monochrome ASCII art
            output = from_image(image_path)
            output.to_terminal(monochrome=True)
            save(output, color_choice)
            return output
        else:
            print("Not a valid choice. Defaulting to colored mode.")
            output = from_image(image_path)
            output.to_terminal()
            return output
            
    except Exception as e:
        print(f"Error generating ASCII art: {e}")
        return None

def validate_image(image_path):
    """Validate if the image can be opened"""
    try:
        with Image.open(image_path) as img:
            # Just check if it opens successfully
            return True
    except Exception as e:
        print(f"Error opening image: {e}")
        return False

def main():
    print("=" * 60)
    print("ASCII ART GENERATOR".center(60))
    print("=" * 60)
    
    image_source = None
    valid_image = False
    
    while not valid_image:
        open_choice = input("\nOpen local image file or from a URL? <l for local/u for URL>: ").lower()
        
        if open_choice == "l":
            path = input("Enter a valid path to an image:\n")
            # Remove quotes if present
            path = path.strip().replace('"', "").replace("'", "")
            
            # Check if file exists
            if os.path.exists(path):
                if validate_image(path):
                    image_source = path
                    valid_image = True
                    print("✓ Image loaded successfully!")
                else:
                    print(f"✗ {path} is not a valid image file.")
            else:
                print(f"✗ File not found: {path}")
                
        elif open_choice == "u":
            url = input("Enter a valid URL to an image:\n")
            url = url.strip().replace('"', "").replace("'", "")
            
            try:
                # Download the image
                response = requests.get(url, stream=True, timeout=10)
                response.raise_for_status()  # Raise an error for bad status codes
                
                # Check content type
                content_type = response.headers.get('content-type', '')
                if 'image' not in content_type:
                    print("✗ URL does not point to an image.")
                    continue
                
                # Save to a temporary file or use directly
                img_data = io.BytesIO(response.content)
                with Image.open(img_data) as test_img:
                    # Just test if it's a valid image
                    test_img.verify()
                
                # Store the URL as the source
                image_source = url
                valid_image = True
                print("✓ Image loaded successfully from URL!")
                
            except requests.exceptions.RequestException as e:
                print(f"✗ Error downloading image: {e}")
            except Exception as e:
                print(f"✗ Error opening image from URL: {e}")
        else:
            print("✗ Not a valid choice. Please enter 'l' or 'u'.")
    
    # Get color preference
    os.system('cls')
    print("=" * 60)
    print("ASCII ART GENERATOR".center(60))
    print("=" * 60)
    
    color_choice = ""
    while color_choice not in ['c', 'm']:
        color_choice = input("\nColoured or monochrome?\n<c for colour / m for monochrome>\n").lower()
        if color_choice not in ['c', 'm']:
            print("✗ Not a valid choice. Please enter 'c' or 'm'.")
    
    if color_choice == 'c':
        print("\n✨ Generating COLORED ASCII art...")
        print("   (Note: Colored images cannot be saved to a text file)\n")
    else:
        print("\n✨ Generating MONOCHROME ASCII art...")
        print("   (Monochrome images can be saved to a text file)\n")
    
    input("Press Enter to generate the ASCII art...")
    
    # Generate the ASCII art
    os.system('cls')
    print("=" * 60)
    print("YOUR ASCII ART".center(60))
    print("=" * 60)
    print()
    
    generate(image_source, color_choice)
    
    print("\n" + "=" * 60)
    print("Thank you for using ASCII Art Generator!".center(60))
    print("=" * 60)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
    
    input("\nPress Enter to exit...")
    os.system('cls')