import argparse
import os
import shutil
from glob import glob
import numpy as np


def ig_f(dir, files):
    # Ignore files
    return [f for f in files if os.path.isfile(os.path.join(dir, f))]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='line_3d')
    parser.add_argument('--file_name', help='File containing point cloud')
    parser.add_argument('--new_file_name', help='File to contain new point cloud')

    args = parser.parse_args()
    
    pcd = np.loadtxt(args.file_name)
    np.savetxt(args.new_file_name, pcd[:, :3])

