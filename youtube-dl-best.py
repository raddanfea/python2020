#!/usr/bin/env python3

import subprocess
import sys
import os


def printHelp():
    HELP = """
    USAGE: ./youtube-dl-best [URL] [extra arg]
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
    """.strip()
    print(HELP)


def getLink(args):
    if len(args) > 1:
        return args[1]
    else:
        print("No link?")
        return None


def getTypes(link):
    proc = subprocess.Popen("youtube-dl -F " + link, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, shell=True)
    resp = proc.communicate()[0]
    proc.terminate()
    return resp


def printYtDlHelp():
    proc = subprocess.Popen("youtube-dl --help ", stdout=sys.stdout,
                            stderr=sys.stderr, shell=True)
    resp = proc.communicate()[0]  # Do NOT delete this or you get no response from proc.
    proc.terminate()


class VideoOptions:
    """Common base class for all download options."""

    def __init__(self, id, audio, resolution, info):
        self.id = id
        self.audio = audio
        self.resolution = resolution
        self.info = info

    def getId(self):
        return self.id

    def getAud(self):
        return self.audio

    def getRes(self):
        return self.resolution

    def getInfo(self):
        return self.info


def getBestOO(response, ext, mix):
    responseBuffer = response.decode()
    lines = responseBuffer.split('\n')[3:-1]
    options = []
    bestAudioOption = VideoOptions(0, 0, 0, 'Not found')
    bestVideoOption = VideoOptions(0, 0, 0, 'Not found')

    for theLine in lines:

        splitLine = theLine.split()

        lineId = splitLine[0]

        if mix is True or ext in theLine:

            try:
                lineRes = int(splitLine[3][:splitLine[3].find('p')])
            except ValueError:
                lineRes = 0

            try:
                audioPos = theLine.index('@')
            except ValueError:
                audioPos = 0

            if audioPos != 0:
                lineAud = int(theLine[audioPos + 1:audioPos + 4])
            else:
                lineAud = 0

            options.append(VideoOptions(lineId, lineRes, lineAud, theLine))

    for option in options:
        if option.getAud() > bestAudioOption.getAud():
            bestAudioOption = option
        if option.getRes() > bestVideoOption.getRes():
            bestVideoOption = option

    return bestVideoOption.getId(), bestVideoOption.getInfo(), bestAudioOption.getId(), bestAudioOption.getInfo()


def downloadBest(bestV, bestA, link, ext, extraArgs):
    proc = subprocess.Popen("youtube-dl -f " + bestV + '+' + bestA + ' ' + link + ' '
                            + '--merge-output-format ' + ext
                            + extraArgs,
                            stdout=sys.stdout,
                            stderr=sys.stdout, shell=True)
    resp = proc.communicate()[0]


def parseArgs(args):
    buffer = [' ' + str(x) for x in args]
    return "".join(buffer)


def main():
    args = sys.argv
    ext = 'mp4'
    mix = True

    if '--webm' in args:
        ext = 'webm'
        args.remove('--webm')

    if '--nomix' in args:
        mix = False
        args.remove('--nomix')

    if '--help' in args:
        printYtDlHelp()
        args.remove('--help')
        sys.exit(0)

    if '-h' in args:
        printHelp()
        args.remove('-h')
        sys.exit(0)

    link = getLink(args)
    if link is not None:
        response = getTypes(link)

        # removing unnecessary data to prepare for passing extra arguments
        args = args[2:]

        if response.decode('utf-8').startswith('ERROR') or response.decode('utf-8').startswith('Usage'):
            print("ERROR: Invalid link.", file=sys.stderr)
        else:
            extraArgs = parseArgs(args)

            # I have no idea why, but these get flipped on return.
            bestA, bestAInfo, bestV, bestVInfo = getBestOO(response, ext, mix)
            print('Best Audio:  ' + bestAInfo + '\n' + 'Best Video:  ' + bestVInfo)
            request = input("Download? Y/N \n")

            if request.lower() in ['yes', 'y']:
                downloadBest(bestV, bestA, link, ext, extraArgs)


if __name__ == '__main__':
    main()
