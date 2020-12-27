# File-to-Image
Python script to convert any file to a PNG image.

The script <strong>file_to_png.py</strong> aims to create a PNG file that can store any file format (video, image, pdf, archive...). The file data is stored in the hexadecimal values of the pixels of the image.

The script <strong>png_to_file.py</strong> aims to recover the file from the previously generated PNG file.


<h2>How to use</h2>
<div>
	<ul><li><code>file_to_png.py &ltinput_file&gt &ltoutput_image_name&gt</code></li></ul>
<p>
	<i>Don't add any extension to &ltoutput_image_name&gt</i>
</p>
<p>
	&ltoutput_image_name&gt is optional, default is "output"
</p>
</div>

<p></p>


<div>
<ul><li><code>png_to_file.py &ltinput_png&gt &ltoutput_file&gt</code></li></ul>
<p>
	&ltoutput_file&gt is optional, default is "output.dat"
</p>
</div>

<h2>Example</h2>
<ul><li><code>python file_to_png.py Document.pdf Document</code>  This create a file Document.png from Document.pdf</li></ul>
<ul><li><code>python png_to_file.py Document.png recovered_Document.pdf</code> This read the file Document.png and recreate the file recovered_Document.pdf</li></ul>

The new recovered_Document.pdf is the same as recovered_Document.pdf, there may be a few extra bytes \x00 at the end of recovered_Document.pdf but this should not cause any problems.
