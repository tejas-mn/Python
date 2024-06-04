import argparse
import os
import pydoc

def list_files(module_dir):
    pydoc.writedoc(module_dir)
    for filename in os.listdir(module_dir):
        (file_name, ext) = os.path.splitext(filename)
        if ext == ".py":
            module_name = module_dir+"."+file_name
            print(module_name)
            pydoc.writedoc(module_name)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="List files in a directory.")
    parser.add_argument("path", help="Path to the target directory")
    args = parser.parse_args()

    list_files(args.path)
