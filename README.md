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

<h2>Examples</h2>
