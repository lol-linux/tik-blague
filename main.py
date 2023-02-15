from gtts import gTTS
from moviepy.editor import *
import asyncio
from blagues_api import BlaguesAPI, BlagueType
from moviepy.editor import VideoFileClip, AudioFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.compositing.concatenate import concatenate_videoclips
from Tiktok_uploader import uploadVideo
import os





async def main():
    blagues = BlaguesAPI("tocken")
    blague = await blagues.random_categorized(BlagueType.DARK)
    blague_type = blague.type
    blague_answer = blague.answer
    blague_joke = blague.joke
    print(blague_type)
    print(blague_joke)
    print(blague_answer)
    text = blague_joke

    test = gTTS(blague_answer, lang='fr')

    test.save("repo.mp3")
    audio = AudioFileClip("repo.mp3")
    duree = audio.duration


    tts = gTTS(blague_joke, lang='fr')

    tts.save("blague.mp3")

    clip = VideoFileClip("test.mp4") 
    
    clip = clip.subclip(0, 6) 
    
    clip = clip.volumex(1) 
    
    test = TextClip(blague_type, font="Lane", fontsize = 15, color = 'black') 
    
    test = test.set_pos('left').set_duration(6)  
    txt_clip = TextClip(blague_joke, font="Lane", fontsize = 30, color = 'black') 
    
    txt_clip = txt_clip.set_pos('center').set_duration(6) 
    
    video = CompositeVideoClip([clip, txt_clip]) 
    
    video.ipython_display(width = 280)
    video.write_videofile("blague.mp4")

    audio_clip1 = AudioFileClip("blague.mp3")

    audio_final = concatenate_audioclips([audio_clip1])

    video_clip = VideoFileClip("blague.mp4")

    final_video = video_clip.set_audio(audio_final)

    final_video.write_videofile("blague.mp4")



    clip = clip.subclip(0, 6) 
    
    clip = clip.volumex(1) 
    
    test = TextClip(blague_type, font="Lane", fontsize = 15, color = 'black') 
    
    test = test.set_pos('left').set_duration(6)  
    txt_clip = TextClip(blague_answer, font="Lane", fontsize = 30, color = 'black') 
    
    txt_clip = txt_clip.set_pos('center').set_duration(6) 
    
    video = CompositeVideoClip([clip, txt_clip]) 
    
    video.ipython_display(width = 280)
    video.write_videofile("repo.mp4")


    video.ipython_display(width = 280)
    video.write_videofile("repo.mp4")

    audio_clip1 = AudioFileClip("repo.mp3")

    audio_final = concatenate_audioclips([audio_clip1])

    video_clip = VideoFileClip("repo.mp4")

    final_video = video_clip.set_audio(audio_final)

    final_video.write_videofile("repo.mp4")

    clip1 = VideoFileClip("blague.mp4")
    clip2 = VideoFileClip("repo.mp4")
    final_clip = concatenate_videoclips([clip1, clip2])
    final_clip.write_videofile("video_finale.mp4")




    session_id = "session_id"
    file = "video_finale.mp4"
    title = "La blague crée par un bot."
    tags = ["humour"]
    schedule_time = 1672592400
    uploadVideo(session_id, file, title, tags, verbose=True)








 
asyncio.run(main())

