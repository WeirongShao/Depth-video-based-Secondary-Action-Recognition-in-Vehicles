import cv2
import numpy as np
import keras

# Path to the pre-trained model
CLASSES_LIST = ["drinking", "eating", "fastening_seat_belt", "fetching_an_object", "interacting_with_phone","interacting_with_backpack"
                , "interacting_with_laptop", "interacting_with_sunglasses"
                , "placing_an_object", "preparing_food", "pressing_automation_button", "putting_on_jacket", "reading_magazine"
                , "reading_newspaper", "taking_off_jacket", "talking_on_phone", "unfastening_seat_belt"
                , "using_multimedia_display", "working_on_laptop", "writing", "looking_or_moving_around (e.g. searching)"
                , "sitting_still"]
model_path = "D:/PoseEstimation/Human_Activity_Recognition_using_TensorFlow_CNN_LSTM_Code/LRCN_model_drive_and_act_Date_Time_2024_04_27__22_13_18___Loss_0.9746441841125488___Accuracy_0.7447761297225952.h5"
model = keras.models.load_model(model_path.replace("\\", "/"))  # Use forward slashes to ensure the correct path

# Path to the video file
video_path = "D:/PoseEstimation/Grad-CAM/run1_2018-05-03-14-08-31.kinect_depth (online-video-cutter.com)7.mp4"
cap = cv2.VideoCapture(video_path.replace("\\", "/"))  # Also use forward slashes

# Get video information for VideoWriter
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Path to save the output video file
output_path = "D:/PoseEstimation/Grad-CAM/output_video_prediction.mp4"  # You can modify this path to save to your desired location

# Initialize the VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Define the codec
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

def process_and_save_video(model, video_capture, num_frames, frame_size, video_writer):
    frames = []
    last_prediction = ("", 0)

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        frame_processed = cv2.resize(frame, frame_size)
        frame_processed = frame_processed / 255.0
        frames.append(frame_processed)

        if len(frames) == num_frames:
            frames_array = np.array(frames)
            frames_array = np.expand_dims(frames_array, axis=0)
            prediction = model.predict(frames_array)[0]
            predicted_class_id = np.argmax(prediction)
            predicted_class_name = CLASSES_LIST[predicted_class_id]
            confidence = np.max(prediction)

            last_prediction = (predicted_class_name, confidence)
            frames = []

        if last_prediction[0] and last_prediction[1] and last_prediction[1] > 0.5:
            cv2.putText(frame, f"{last_prediction[0]}: {last_prediction[1]:.2f}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2, cv2.LINE_AA)

        video_writer.write(frame)  # Write the frame to the output file
        cv2.imshow('Video Prediction', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    video_writer.release()
    cv2.destroyAllWindows()

# Call the function
process_and_save_video(model, cap, num_frames=10, frame_size=(128, 128), video_writer=out)
