import os
import argparse
import cv2
import mediapipe as mp

def process_img(img, face_detection):
    H, W, _ = img.shape

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    out = face_detection.process(img_rgb)

    if out.detections is not None:
        for detection in out.detections:
            location_data = detection.location_data
            bbox = location_data.relative_bounding_box

            x1, y1, w, h = bbox.xmin, bbox.ymin, bbox.width, bbox.height

            x1 = int(x1 * W)
            y1 = int(y1 * H)
            w = int(w * W)
            h = int(h * H)

            # Ensure coordinates are within image bounds
            x1 = max(0, x1)
            y1 = max(0, y1)
            w = min(w, W - x1)
            h = min(h, H - y1)

            # blur faces (only if region is valid)
            if w > 0 and h > 0:
                img[y1:y1 + h, x1:x1 + w, :] = cv2.blur(img[y1:y1 + h, x1:x1 + w, :], (30, 30))

    return img

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("--mode", default='webcam', choices=['image', 'video', 'webcam'])
parser.add_argument("--filePath", default=None)
args = parser.parse_args()

# Create output directory
output_dir = './output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Initialize face detection
mp_face_detection = mp.solutions.face_detection

with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:

    if args.mode == "image":
        # Check if file path is provided
        if args.filePath is None:
            print("Error: Please provide a file path for image mode")
            exit()
        
        # Read image
        img = cv2.imread(args.filePath)
        if img is None:
            print(f"Error: Could not read image from {args.filePath}")
            exit()
            
        img = process_img(img, face_detection)

        # Save image
        output_path = os.path.join(output_dir, 'output.png')
        cv2.imwrite(output_path, img)
        print(f"Image saved to {output_path}")

    elif args.mode == 'video':
        # Check if file path is provided
        if args.filePath is None:
            print("Error: Please provide a file path for video mode")
            exit()
            
        cap = cv2.VideoCapture(args.filePath)
        if not cap.isOpened():
            print(f"Error: Could not open video from {args.filePath}")
            exit()
            
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read first frame")
            exit()

        output_video = cv2.VideoWriter(os.path.join(output_dir, 'output.mp4'),
                                       cv2.VideoWriter_fourcc(*'mp4v'),  # lowercase 'mp4v' works better
                                       25,
                                       (frame.shape[1], frame.shape[0]))

        frame_count = 0
        while ret:
            frame = process_img(frame, face_detection)
            output_video.write(frame)
            
            # Show progress
            frame_count += 1
            if frame_count % 30 == 0:  # Print every 30 frames
                print(f"Processed {frame_count} frames")
                
            ret, frame = cap.read()

        cap.release()
        output_video.release()
        print(f"Video saved to {output_dir}/output.mp4")

    elif args.mode == 'webcam':
        # Try different camera indices if 2 doesn't work
        camera_index = 0  # Changed from 2 to 0 (most common)
        cap = cv2.VideoCapture(camera_index)
        
        if not cap.isOpened():
            print(f"Error: Could not open webcam at index {camera_index}")
            print("Trying camera index 1...")
            cap = cv2.VideoCapture(1)
            
        if not cap.isOpened():
            print("Error: Could not open any webcam")
            exit()

        print(f"Webcam opened successfully! Press 'q' to quit.")
        
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame")
                break
                
            frame = process_img(frame, face_detection)
            cv2.imshow('Face Blur - Press Q to quit', frame)
            
            # Check for 'q' key to quit (waitKey(1) for real-time)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()