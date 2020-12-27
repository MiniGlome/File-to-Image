from PIL import Image
import time
import sys
import os

def show_usage():
	print(f"\nUsage --> {sys.argv[0]} <input_png> <output_file>\n")
	print(f"<output_file> is optional, default is \"output.dat\"")

def run(input_file, output_file):

	t=time.time()  # Start timer

	print("File "+input_file+"\n...")
	img = Image.open(input_file, 'r')
	rgb_pixels = list(img.getdata())

	data_length = len(rgb_pixels)*6
	print(f"Data length = {data_length}")

	print(f"Estimated execution time : {int(data_length*0.0000002)} seconds") 

	hex_values = []
	for pixel in rgb_pixels:
		hex_values.append('%02x%02x%02x' % pixel)  # Convert RBG values to hex
	print("RGB pixels converted to Hex")

	hex_string = "".join(hex_values)

	with open(output_file, "wb") as f:
		f.write(bytearray.fromhex(hex_string))

	print("...\nFile saved as "+output_file)
	print('Execution time : '+str(time.time()-t)+" seconds")

if __name__ == '__main__':
    if 1 < len(sys.argv) and len(sys.argv) < 4:
        if os.path.isfile(sys.argv[1]):
            try:
                run(sys.argv[1], sys.argv[2])
            except:
                run(sys.argv[1], "output.modify_this_extension")
        else:
            print(f"File {sys.argv[1]} doesn't exist")      
    else:
        show_usage()

