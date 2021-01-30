# LZW-Compression
IMPLEMENTATION OF LZW COMPRESSION ALGORITHM
LZW algorithm works for compressing and decompressing the data in a lossless manner, this algorithm works at its 
best when there is some redundancy in data.In this project we are implementing the algorithm with some practical 
usecases of encoding and decoding the strings that have redundancy.

MINIMUM REQUIREMENTS TO RUN ENCODER/DECODER:
Install Python3.7.4
set the environment path for python to excecute “.py” files
The program can be viewed in Notepad++ or any other IDE

RUNNING ENCODER:
1.Know the path location and bit length and pass as command line arguments as shown below.
“python /Users/tagore_pothuneedi/Desktop/algsv2_2/project_encoder.py /Users/tagore_pothuneedi/Downloads/examples/input2.txt 9”
2.Once the program executes successfully the output file location is displayed in the command prompt/terminal in which the program is executed.
3.The compressed output from the Encoder is the same filename with a “.lzw” extention.(To read this use xxd -b file_name.lzw for linux base os/or any online tool to decode into 16bit binary dump).
4.For example the output for the above given path will be at “/Users/tagore_pothuneedi/Downloads/examples/input2.lzw”

RUNNING DECODER:
1.The Decoder process only ‘.lzw’ formats.so only this format can be decompressed. Otherwise an error is displayed.
2.To start decode use the as specified below and pass the compressed file location and bitlength as command line arguments.
“python /Users/tagore_pothuneedi/Desktop/algosv2_2/project_decoder.py /Users/tagore_pothuneedi/Downloads/examples/input2.lzw 9”
3.Once the program executes the output location is displayed in the command prompt/terminal. The program typically outputs the decompressed file from where it was taken.
4.For example the decompressed file for above arguments will be at  “/Users/tagore_pothuneedi/Downloads/examples/input2_decoded.txt”
