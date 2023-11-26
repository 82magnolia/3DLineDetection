PCD_DIR=$1
NEW_PCD_DIR=$2
LINE_DIR=$3

# Convert color point cloud to xyz-only point cloud
echo "Step 1: Converting to xyz-only point cloud \n"
python convert_pcd_single.py --file_name "$PCD_DIR" --new_file_name "$NEW_PCD_DIR"

# Extract lines
echo "Step 2: Extracting lines \n"
python extract_line_single.py --file_name "$NEW_PCD_DIR" --line_name "$LINE_DIR"
