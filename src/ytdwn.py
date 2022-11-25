#!/usr/bin/python3
from controller import YoutubeAudioController
from sys import argv

youtubeController = YoutubeAudioController("./Musics")

arguments = argv

if "help" in argv:
    print("Help")

elif "audio" in argv:
    filename = None
    filepath = None
    url = ""
    for arg in argv:
        if "--name=" in arg:
            filename = arg.split("--name=")[-1]
            if filename[-4:] == ".mp3":
                filename += ".mp3"
        elif "--path=" in arg:
            filepath = arg.split("--path=")[-1]
        else:
            url = arg
    
    result = youtubeController.downloadAudio(url, filename, filepath)
    print(result)

elif "playlist" in argv:
    foldername = None
    folderpath = None
    url = ""
    for arg in argv:
        if "--name=" in arg:
            foldername = arg.split("--name=")[-1]
        elif "--path=" in arg:
            folderpath = arg.split("--path=")[-1]
        else:
            url = arg
    result = youtubeController.downloadPlaylist(url, foldername, folderpath)
    print(result)
else :
    print("You can see all commands with ytdwn help")

