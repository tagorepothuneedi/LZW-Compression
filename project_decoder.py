#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#Title:LZW Compression Decoder Implementation in Python
#Author:Tagore Pothuneedi
#Date:03.09.2020
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import sys
from struct import *
def decoder(fileloc,n):                                                                 ##decoder definion with arguments: compressed file location and bit length
    try:
        f=open(fileloc,"rb+")                                                           ##Opening the compressed file
    except FileNotFoundError:                                                           ##File Location error stop execution 
        print("File Not Found .Check the path variable and Filename")
        return
    dir_list=fileloc.split('/')                                                         ##Getting the compressed file location
    fileext=dir_list[len(dir_list)-1].split('.')[1]                                     ##Getting File extention
    destloc=fileloc[:-4]
    if fileext=='lzw':                                                                  ## Condition for correct file format
        decomp_file=open("{}_decoded.txt".format(destloc), "a+")                        ##Creating decoded output file object
        comp_code=[]
        len1=len(f.read())                                                              ##bytes to read
        f.seek(0)                                                                       ##moving cursor back to index 0                                                                       
        for i in range(0,len1,2):                                                       ## Reading 2Bytes chuncks at a time and appeding to compressed code list
            encoded=f.read(2)
            comp_code.append(unpack('>H',encoded)[0])                                   ##Reading the encoded file
        print(comp_code)
        ascii_dict={}                                                                   ##table for mapping code and strings         
        table_size=2**int(n)                                                            
        for i in range(256):                                                            ##initializing the ascii_dict for 0 to 255 values
            ascii_dict[i]=chr(i)
        code=comp_code[0]                                                               ##getting the first binary value from the file 
        string=ascii_dict[int(code)]                                                    ##converting the 16bit binary into character
        comp_code.pop(0)                                                                ## Removing the converted code from the list of comp_code
        decomp_file.write(string)                                                       ## Writing the decompressed string to the file 
        counter=256                                                                     ## Variable counter to keep track of the ascii_dict insertion of key-> value pairs
        for code in comp_code:
            if int(code) not in ascii_dict.keys():                                      ##creating a new string if the code is not in available in the dictionary
                new_string=string+string[0]
            else:
                new_string=ascii_dict[int(code)]                                      
            #print(new_string)
            decomp_file.write(new_string)                                               ##writing the new_string to the decompressed file 
            if len(ascii_dict)<table_size:                                              ##As the new string is not see add to ascii_dictonary and increment the counter
                ascii_dict[counter]=string+new_string[0]
                counter=counter+1
            string=new_string
        decomp_file.close()
        f.close()
        print("Decompressed file location:{}_decoded.txt".format(destloc))
    else:
        print("Unknown File Format")                                                    ##If the file format is not in .lzw 

if __name__=='__main__':
    try:
        decoder(sys.argv[1],sys.argv[2])                                                ##function call by passing the command line arguments
    except IndexError
        print('ERROR:Please enter the file location and bitlength in the command line')