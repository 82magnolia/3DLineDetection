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
    parser.add_argument('--file_dir', help='Directory where point clouds are located')
    parser.add_argument('--new_file_dir', help='Directory where new point clouds will be saved')

    args = parser.parse_args()
    
    # Copy directories
    shutil.copytree(args.file_dir, args.new_file_dir, ignore=ig_f)

    # Get all point cloud filenames in file_dir
    filenames = sorted(glob(os.path.join(args.file_dir, '**', '*.txt'), recursive=True))

    os.chdir('../src/')
    for idx, f in enumerate(filenames):
        print(f"\n======== Progress: {idx + 1} / {len(filenames)} ========\n")
        new_f = f.replace(args.file_dir, args.new_file_dir)
        pcd = np.loadtxt(f)
        np.savetxt(new_f, pcd[:, :3])

    os.chdir('../python/')
