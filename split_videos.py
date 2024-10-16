from moviepy.editor import VideoFileClip
import os
import pandas as pd

# Video paths
video_path = []
video_path_2 = []
fps = 30
# print(f"FPS: {fps}")

# Load the CSV file
csv_path = ''
df = pd.read_csv(csv_path)
# Filter out all activities related to 'interacting_with_phone'
activities_drinking = df[df['activity'] == 'interacting_with_phone']
# print(activities_drinking)
# Output directory
output_dir = 'drive_and_act_ir//interacting_with_phone//'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def extract_and_save_clip(row):
    for i in range(1, 16):  # Only for participant_id 1 to 15
        if row['participant_id'] == i:
            start_frame = row['frame_start']
            end_frame = row['frame_end']
            start_time = start_frame / fps
            end_time = end_frame / fps
            
            # Try to load the video and extract the specified time segment
            try:
                clip = VideoFileClip(video_path_2[i - 1]).subclip(start_time, end_time)
                
                # Construct output file name and path
                output_filename = f"{row['file_id']}_frame_{start_frame}_to_{end_frame}.mp4"
                output_path = os.path.join(output_dir, output_filename)
                
                # Save the video clip
                clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
            except ValueError as e:
                # Print error message and continue when duration errors occur
                print(f"Error for participant {i}: {e}")
            except Exception as e:
                # Handle other potential errors
                print(f"Unexpected error for participant {i}: {e}")
        else:
            print(f"Skipping participant_id {row['participant_id']}")

# For each row in activities_df, perform video extraction and saving operations
activities_drinking.apply(extract_and_save_clip, axis=1)
