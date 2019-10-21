# Pythono3 code to rename multiple
# files in a directory or folder

# importing os module
import os

# Function to rename multiple files
def main():
    i = 0

    for filename in os.listdir("Pictures/car"):
        dst = "car-" + str(i) + ".jpeg"
        src = 'Pictures/car/' + filename
        dst = 'Pictures/car/' + dst
        os.rename(src, dst)
        # dst ="Hostel" + str(i) + ".jpg"
        # src ='xyz'+ filename
        # dst ='xyz'+ dst
        # rename() functicdon will
        # rename all the files
        # os.rename(src, dst)
        i += 1

# Driver Code
if __name__ == '__main__':

    # Calling main() function
    main()
