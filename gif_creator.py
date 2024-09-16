from moviepy.editor import VideoFileClip


video_clip = VideoFileClip("6.mp4")


start_time = 15  
end_time = 20  


gif_clip = video_clip.subclip(start_time, end_time)


gif_clip = gif_clip.resize(0.5)  


gif_clip.write_gif("out.gif", fps=10)  
