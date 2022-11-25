# YoutubeMusic - Download

## Descirption : 

This is a fork of many-youtube-mp3 by emma-orset.

The purpose of this software, is that you can download audio from Youtube, as well as whole playlists if you want.

## Installation 

To use this tool, you'll need Python3.

then install the requirements : 

```
pip install -r requirements.txt
```

You might also want to add the src folder to your *PATH* if you want to use this from everywhere.  

## How to use 

You can use this tool from your terminal.

If you want to download 1 audio, you can use:
```
ytdwn.py audio https://www.youtube.com/watch?v=dQw4w9WgXcQ --name="<Music Name>" --path="<Download path>"
```

If you want to download a whole playlist : 

```
ytdwn.py playlist "https://www.youtube.com/watch?v=xfr64zoBTAQ&list=PLKIxB9vhdS_3x0A5za3mmu1wdoolgRQ65" --name="<Playlist Name>" --path="<Download path>"
```
