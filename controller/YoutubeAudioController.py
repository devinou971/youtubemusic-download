from pytube import YouTube
from os import listdir, remove, mkdir
from os.path import isfile, join, exists

class YoutubeAudioController:
    
    def __init__(self, path) -> None:
        self.counter = 0
        self.path = path
        self.existingSongs = []

        if not exists(self.path):
            mkdir(self.path)

    def downloadYoutubeAudio(self, url : str, filename : str = None):
        musicFolder = [f for f in listdir(self.path) if isfile(join(self.path, f))]
        try:
            youtubeVideo = YouTube(url)
            
        except:
            return {
                "result" : 0,
                "error": "URL invalide"
            }
        if not filename:
            filename = youtubeVideo.title + ".mp3"

        if filename in musicFolder:
            return {
                "result": 1,
                "filename": filename,
                "filepath": join(self.path, filename)
            }
        
        audio = youtubeVideo.streams.filter(only_audio = True).first()
        audio.download(output_path=self.path,filename=filename)
        return {
            "result": 1,
            "filename": filename,
            "filepath": join(self.path, filename)
        }
    
    def deleteYoutubeMusic(self, filename: str):
        musicFolder = [f for f in listdir(self.path) if isfile(join(self.path, f))]
        if filename in musicFolder:
            remove(join(self.path, filename))
            return {
                "result" : 1
            }
        else :
            return {
                "result" : 0,
                "error" : "file doesn't exists"
            }
    
    def purgeFolder(self):
        musicFolder = [f for f in listdir(self.path) if isfile(join(self.path, f))]
        for musicFile in musicFolder:
            remove(join(self.path, musicFile))
        
        return {
            "result" : 1,
            "deletedFiles" : len(musicFolder)
        }