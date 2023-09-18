import cv2
import os

# Set the directory containing your image files
image_directory = 'path_to_image_folder'

# List all image files in the directory
image_files = [f for f in os.listdir(image_directory) if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

# Sort the image files in alphabetical order (you can change the sorting criteria)
image_files.sort()

# Define the output video file name
output_video = 'friendship_day_video.mp4'

# Set the video frame size and frame rate
frame_width = 640
frame_height = 480
frame_rate = 30

# Create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use the appropriate codec for your desired output format
out = cv2.VideoWriter(output_video, fourcc, frame_rate, (frame_width, frame_height))

for image_file in image_files:
    # Read the image
    img = cv2.imread(os.path.join(image_directory, image_file))

    # Resize the image to fit the video frame size
    img = cv2.resize(img, (frame_width, frame_height))

    # Write the image to the video
    out.write(img)

# Release the video writer
out.release()

print(f"Friendship day video '{output_video}' created successfully.")
