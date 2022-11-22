from controller import *

youtubeController = YoutubeAudioController("./tempDownload")
youtubeController.purgeFolder()
youtubeController.downloadYoutubeAudio("https://www.youtube.com/watch?v=M0CfCdQ2zPU", "Tristam.mp3")

