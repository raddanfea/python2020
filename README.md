This is a repo for my script languages class.
All its contents are under MIT license.

Includes youtube-dl-best, which is a python script that uses youtube_dl to download a youtube video in the best possible quality. 

    USAGE: ./youtube-dl-best.py [URL] [extra args]
    
    This is a python script that help you download the best video quality using youtube_dl.
    To merge the file formats, you need ffmpeg or avconv installed.
    For this script to run, you have to be able to run youtube-dl from terminal.
    Your first argument MUST be a link, additional arguments may be in any order after that.
    You can use youtube_dl arguments.
    
    Warning: ffmpeg often fails combining different formats. Use --nomix if needed!
    
    -h          Prints this help block.
    --help      Prints youtube_dl's help.
    --webm      Convert it to webm instead of the default mp4.
    --nomix     Don't mix different video and audio formats. Easier to process.
