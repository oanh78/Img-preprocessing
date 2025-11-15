# Image Preprocessing Tool 
This script automatically processes and resizes images to 1024x1024 pixels.

# System Requirements
- Python 3.x
- OpenCV

## Installation
If not already available Install OpenCV
pip install opencv-python

## Usage
1. Place the images you want to process inside the Data/ folder.
2. Run the script:
```bash
python resize_1024.py
```
3. The processed images will be saved in the Img-preprocessing/ folder.
## Folder Structure
```
Image_preprocessing/
├── Data/                   # Original images
├── Img-preprocessing/      # Processed images
├── Labeled data/          # Labeled images
└── resize_1024.py         # Main script 
```