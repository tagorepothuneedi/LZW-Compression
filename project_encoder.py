#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#Title:LZW Compression Encoder Implementation in Python
#Author:Tagore Pothuneedi
#Date:03.09.2020
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import sys
from struct import *
def encode(fileloc,n):                                                                              ## Encoder definition with arguments as filelocation and bit length
    newloc=fileloc[:-4]                                                                             ##Extracting the file name from the given directory 
    try:                                                                    
        f=open(fileloc,"r")                                                                         ##Opening the input file 
    except FileNotFoundError:
        print("File Not Found .Check the path variable and Filename")
        return
    text2comp=f.read().strip()                                                                      ## reading the content of the file and removing unnecessary line information
    table_size=2**int(n)                                                                            ## creating a predefined table length 
    count=256
    string=''
    ascii_dict={}                                                                                   ## Extented ascii dictionary/hash table for storing the string and associated code
    compress_file=open("{}.lzw".format(newloc), "wb")                                               ## compressed file object
    for i in range(256):                                                                            ## initializing the extended ascii table 
        ascii_dict[chr(i)]=i
    for ch in text2comp:                                            
        if string+ch in ascii_dict.keys():                                                          ##For String in the table concatenate with the previous and check
            string=string+ch                                                        
        else:                                                                                       ## if not in the table convert the string 
            print(pack('>H',int(ascii_dict[string])))
            compress_file.write(pack('>H',int(ascii_dict[string])))                                 ##write the bits to the file in 16bit format('>H=2Bytes')
            if len(ascii_dict)<table_size:
                ascii_dict[string+ch]=count                                                         ##Add the string to the ascii_table and increment the count
                count=count+1
            string=ch                                          
    compress_file.write(pack('>H',int(ascii_dict[string])))                                          ##For the last string converting into 16bits and writing to the file
    compress_file.close()                                                                            ##Close file for commiting
    f.close()
    print('Compressed file location:{}.lzw'.format(newloc))
if __name__=='__main__':
    try:
        encode(sys.argv[1],sys.argv[2])                                                              ##Function call to the encode the given file by passing the command line arguments file location and bit length
    except IndexError:
        print('ERROR:Please enter the file location and bitlength in the command line')
        
