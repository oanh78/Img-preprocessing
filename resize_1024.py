import cv2
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_folder = os.path.join(current_dir, 'Data')
output_folder = os.path.join(current_dir, 'Img-preprocessing')
target_size = (1024, 1024)

# --- Browse image files ---
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.tif', '.tiff', '.png')):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # Read images
        img = cv2.imread(input_path)
        if img is None:
            print(f"Không đọc được ảnh: {filename}")
            continue

        # Resize to 1024x1024
        resized = cv2.resize(img, target_size, interpolation=cv2.INTER_AREA)

        # Save images
        cv2.imwrite(output_path, resized)
        print(f"Processing: {filename}")

print("Complete!")


