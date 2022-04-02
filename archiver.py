#! user/bin/env python3
import os, sys

"""
function to archive files
input:
     files = array of files to be archived
     output_file = name of newly archived file
output: a single file
"""
def arch(files, output_file):
  
    arch_file = open(output_file, 'wb')       # 'wb' = 'write binary'

    for file in files:

        try:
            bfs = os.path.getsize(file)       # get size of file in bytes
            bf = open(file, 'rb')             # bf = binary_file; 'rb' = 'read binary'
            bfn = file.encode()               # name of file converted to bytes

            data = bytearray()

            data += bytearray(len(bfn).to_bytes(4, 'big'))   # 1: filename len; byte ord 'big'
            data += bytearray(bfn)                           # 2: filename
            data += bytearray(bfs.to_bytes(4, 'big'))        # 3: file contents len; byte ord 'big'
            data += bytearray(bf.read())                     # 4: file contents

            arch_file.write(data)
            bf.close()

        except:
            print('File does not exist')

    arch_file.close()

    
if sys.argv[1] == '-help':
    print('To archive: arch <file1> [file2] <output_file>.arch')
    print('To unarchive: unarch <file>.arch')

elif sys.argv[1] == 'arch':    
    print('archiving files...')
    files = sys.argv[2:-1]
    output = sys.argv[-1]
    arch(files, output)
    print('files have been archived to {}'.format(sys.argv[-1]))

elif sys.argv[1] == 'unarch':
    print('extracting files...')
    print('files have been extracted')

else:
    print('unable to use archiver. Type -help to check syntax.')




    

            
            
        
    
    
