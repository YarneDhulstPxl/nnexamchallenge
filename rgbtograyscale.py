import os
from PIL import Image

def main():
    for filename in os.listdir("Pictures/car"):
    img = Image.open('image.png').convert('LA')
    img.save('greyscale.png')

# Driver Code
if __name__ == '__main__':

    # Calling main() function
    main()
