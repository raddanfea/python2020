#!/usr/bin/env python3

import subprocess
import sys


def printHelp():
    HELP = """
    This is a python script that help you download the best video quality using youtube_dl.
    To merge the file formats, you need ffmpeg or avconv installed.
    For this script to run, you have to be able to run youtube-dl from terminal.
    -h Prints help block.
    --webm Convert it to webm instead of the default mp4.
    --nomix Don't mix different video and audio formats. Easier to process.
    """.strip()

    print(HELP)


def getLink(args):

    lnk = ''

    for test in args[1:]:
        if 'youtu' in test:
            lnk = test

    return lnk


def getTypes(link):
    proc = subprocess.Popen("youtube-dl -F " + link, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, shell=True)
    resp = proc.communicate()[0]
    proc.terminate()
    return resp


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

    # analyzing lines for data
    for theLine in lines:

        splitLine = theLine.split()

        lineId = splitLine[0]

        if mix is True or ext in theLine:

            try:
                resolution = splitLine[3]
                lineRes = int(resolution[:resolution.find('p')])
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
            # saving data into our class object, storing object in list
            options.append(VideoOptions(lineId, lineRes, lineAud, theLine))

    for option in options:
        if option.getAud() > bestAudioOption.getAud():
            bestAudioOption = option
        if option.getRes() > bestVideoOption.getRes():
            bestVideoOption = option

    return bestVideoOption.getId(), bestVideoOption.getInfo(), bestAudioOption.getId(), bestAudioOption.getInfo()


def downloadBest(bestV, bestA, link, ext):
    proc = subprocess.Popen("youtube-dl -f " + bestV + '+' + bestA + ' ' + link + ' ' + '--merge-output-format ' + ext,
                            stdout=sys.stdout,
                            stderr=subprocess.STDOUT, shell=True)
    resp = proc.communicate()[0]
    proc.terminate()


def main():
    link = None
    args = sys.argv
    ext = 'mp4'
    mix = True
    request = ''

    if '-h' in args:
        printHelp()
    else:
        if getLink(args):
            link = getLink(args)
        else:
            print('Pass -h for help.')

    if '--webm' in args:
        ext = 'webm'

    if '--nomix' in args:
        mix = False

    if link is not None:
        response = getTypes(link)

        if response.decode('utf-8').startswith('ERROR'):
            print("ERROR: Invalid link.", file=sys.stderr)
        else:
            # I have no idea why, but these get flipped on return.
            bestA, bestAInfo, bestV, bestVInfo = getBestOO(response, ext, mix)
            print('Best Audio:  ' + bestAInfo + '\n' + 'Best Video:  ' + bestVInfo)
            request = input("Download? Y/N \n")

    if request.lower() in ['yes', 'y']:
        downloadBest(bestV, bestA, link, ext)


if __name__ == '__main__':
    main()
