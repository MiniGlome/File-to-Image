from PIL import Image
import numpy as np
import math
import time
import sys
import os

def show_usage():
    print(f"\nUsage --> {sys.argv[0]} <input_file> <output_image_name>\n")
    print(f"Don't add any extension to <output_image_name>")
    print(f"<output_image_name> is optional, default is \"output\"")

def get_execution_time(data_length):
    return time

def hex_to_rgb(value):
    length = len(value)  
    return tuple(int(value[i:i+length//3], 16) for i in range(0, length, length//3))  # Return a tuple with RGB values

def find_length(n):
    sqrt = int(math.sqrt(n))  # Square root
    for i in range(0, sqrt+1)[::-1]:  # Iterate from the square root to 0
        if n%i == 0:   # Check if the current value is a divisor of data length
            return i, int(n/i)  # Return width, length

def run(input_file, output_file):
    t=time.time()  # Start timer

    print("File "+input_file+"\n...")
    with open(input_file, 'rb') as f:
        hexdata = f.read().hex()  # Get hex data from input_file

    if len(hexdata)%6 == 0:   # Data length must be a multiple of 6
        pass
    elif len(hexdata)%6 == 4:
        print("Adding '00' at the end of hexdata")  # Pad with zeros
        hexdata += '00'
    elif len(hexdata)%6 == 2:
        print("Adding '0000' at the end of hexdata")
        hexdata += '0000'

    data_length = len(hexdata)
    print(f"Data length = {data_length}")

    print(f"Estimated execution time : {int(data_length*0.0000007)} seconds")  # This value depends on your computer : data_length*(execution_time/data-length)

    hex_pixels = [hexdata[i:i+6] for i in range(0, data_length, 6)] # Split hexdata every 6 characters
    print("Pixels splited")

    rbg_pixels = []
    for hex_pixel in hex_pixels:                   # This step can take a long time
        rbg_pixels.append(hex_to_rgb(hex_pixel))   # Convert every hex pixel value to RGB
    print("Hex pixels converted to RGB")

    width, length = find_length(len(rbg_pixels))  # Determine width and length of the output image so that it is as close as possible to a square.
    print(f"Image length = {length}\nImage width = {width}")

    matrice = []
    for i in range(len(rbg_pixels)):
        if i%length == 0:
            array = []                        # Split rbg_pixels into lines depending on length to create the matrice.
            for j in range(length):
                array.append(rbg_pixels[i+j])
            matrice.append(array)
    print("Matrice done")

    array = np.array(matrice, dtype=np.uint8)  # Convert matrice to numpy array

    new_image = Image.fromarray(array)  # Create the image with PIL
    new_image.save(output_file)
    print("...\nFile saved as "+output_file)
    print('Execution time : '+str(time.time()-t)+" seconds")

if __name__ == '__main__':
    if 1 < len(sys.argv) and len(sys.argv) < 4:
        if os.path.isfile(sys.argv[1]):
            if sys.argv[2]:
                run(sys.argv[1], sys.argv[2]+".png")
            else:
                run(sys.argv[1], "output.png")
        else:
            print(f"File {sys.argv[1]} doesn't exist")      
    else:
        show_usage()
        