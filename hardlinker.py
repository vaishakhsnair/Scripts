# Script to create hardlinks
import os
import argparse

def linker(source,dest):
    arr = next(os.walk(source))[2]

    for i in arr:
        source_path = os.path.join(source,i)
        dest_path = os.path.join(dest,i)
        print(source_path,dest_path)
        try:
            
            os.link(source_path,dest_path)
        except FileExistsError:
            print(f"{dest_path} Already Exists\n")
            


if __name__ == "__main__":
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-s", "--source", help="Source Directory")
    argParser.add_argument("-d", "--destination", help="Destination Directory")

    args = argParser.parse_args()
    try :
        os.mkdir(args.destination)
    except FileExistsError:
        print("Destination Directory already exists")
        print("Continuing...")
    
    linker(args.source,args.destination)
