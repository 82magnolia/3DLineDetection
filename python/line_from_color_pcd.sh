PCD_DIR=$1
NEW_PCD_DIR=$2
LINE_DIR=$3

# Convert color point cloud to xyz-only point cloud
echo "Step 1: Converting to xyz-only point cloud \n"
python convert_pcd.py --file_dir "$PCD_DIR" --new_file_dir "$NEW_PCD_DIR"

# Extract lines
echo "Step 2: Extracting lines \n"
python extract_line.py --file_dir "$NEW_PCD_DIR" --line_dir "$LINE_DIR"
