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
    parser.add_argument('--file_dir', help='Directory where point clouds are located')
    parser.add_argument('--line_dir', help='Directory where lines will be saved')

    args = parser.parse_args()
    
    # Copy directories
    shutil.copytree(args.file_dir, args.line_dir, ignore=ig_f)

    # Get all point cloud filenames in file_dir
    filenames = sorted(glob(os.path.join(args.file_dir, '**', '*.txt'), recursive=True))

    os.chdir('../src/')
    for idx, f in enumerate(filenames):
        print(f"\n======== Progress: {idx + 1} / {len(filenames)} ========\n")
        line_f = f.replace(args.file_dir, args.line_dir).replace('.txt', '')
        subprocess.run(['./LineFromPointCloud', f, line_f])

    os.chdir('../python/')
