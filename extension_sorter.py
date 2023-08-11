#script to copy files and sort according to extension type

import os
import shutil
import argparse

def chkdir(ext,dest):
    folder = os.path.join(dest,ext)
    print(f"Extension :{ext}")
    if os.path.isdir(folder):
        print("Extension Path Exists")
        
    else:
        print("Extension Folder not present.Creating It ....")
        folder = folder.rstrip()
        os.mkdir(folder)
    return folder
        

def copyf(filename,source,dest):

    source_path = os.path.join(source,filename)
    dest_path = os.path.join(dest,filename)
    print(f"copying :{source_path} to {dest}")
    shutil.copy2(source_path, dest_path)  

    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s","--source",help="Source Directory")
    parser.add_argument("-d","--destination",help="Destination Directory")
    args = parser.parse_args()
    source_content = next(os.walk(args.source))[2]
    extensions = []
    for file in source_content:
        filename = file.split(".")
        if len(filename)<2:
            continue
        ext_folder = os.path.join(args.destination,filename[-1])
        if ext_folder not in extensions:  
            extensions.append(chkdir(filename[-1],args.destination)) 

        copyf(file,args.source,ext_folder)
    