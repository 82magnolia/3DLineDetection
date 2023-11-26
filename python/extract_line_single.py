import subprocess
import argparse
import os
import shutil
from glob import glob


def ig_f(dir, files):
    # Ignore files
    return [f for f in files if os.path.isfile(os.path.join(dir, f))]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='line_3d')
    parser.add_argument('--file_name', help='File containing point cloud')
    parser.add_argument('--line_name', help='File to contain line cloud')

    args = parser.parse_args()
    os.chdir('../src')
    subprocess.run(['./LineFromPointCloud', args.file_name, args.line_name])
    os.chdir('../python')

