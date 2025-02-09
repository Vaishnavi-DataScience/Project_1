import os
import subprocess


video_directory = '/Users/nvaishnavi/Documents/Instructional_Video_analysis/1_all_videos'  
output_directory = '/Users/nvaishnavi/Documents/Instructional_Video_analysis/7_extracted_frames'  



if not os.path.exists(output_directory):
    os.makedirs(output_directory)


video_files = [f for f in os.listdir(video_directory) if f.endswith('.mp4')]  


def extract_frames(video_path, output_dir):
    
    video_folder_name = os.path.splitext(os.path.basename(video_path))[0] 
    video_output_dir = os.path.join(output_dir, video_folder_name)
    
    if not os.path.exists(video_output_dir):
        os.makedirs(video_output_dir)
    
   
    output_filename = os.path.join(video_output_dir, f"{video_folder_name}_%03d.jpg")  # Save as JPG
    command = [
        'ffmpeg', 
        '-i', video_path,                # Input video
        '-vf', 'fps=1/60',               # Extract frame every 60 seconds (1 minute)
        '-q:v', '2',                     # Quality of the extracted frames (lower is better)
        output_filename                  # Output path for frames
    ]
    
    subprocess.run(command)


for video_file in video_files:
    video_path = os.path.join(video_directory, video_file)
    extract_frames(video_path, output_directory)

print(f"Frames have been successfully extracted and saved in {output_directory}")
