import subprocess
import sys


def printHelp():
    HELP = """
    This is a python script that help you download the best video quality using youtube_dl.
    To merge the file formats, you need ffmpeg or avconv installed.
    For this script to run, you have to be able to run youtube-dl from terminal.
    -h Prints help block.
    -l Specifies link to check for. Supports raw link or quoted link.
    --webm Download it in webm instead of the default mp4.
    --nomix Don't mix different video and audio formats. Easier to process.
    """.strip()

    print(HELP)


def getLink(args):
    linkMark = '-l'
    lnk = None
    try:
        lnk = args[args.index(linkMark) + 1].strip('"')
    except IndexError:
        print("No link specified! Use -h for help.", file=sys.stderr)
    except ValueError:
        print("Use -h for help.", file=sys.stderr)
    return lnk


def getTypes(link):
    proc = subprocess.Popen("youtube-dl -F " + link, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, shell=True)
    resp = proc.communicate()[0]
    proc.terminate()
    return resp


class VideoOptions:
    """Common base class for all download options."""

    def __init__(self, id, audio, resolution):
        self.id = id
        self.audio = audio
        self.resolution = resolution

    def getId(self):
        return self.id

    def getAud(self):
        return self.audio

    def getRes(self):
        return self.resolution


def getBestOO(response, ext, mix):
    responseBuffer = response.decode()
    lines = responseBuffer.split('\n')[3:-1]
    options = []
    bestAudioOption = VideoOptions(0, 0, 0)
    bestVideoOption = VideoOptions(0, 0, 0)

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

        options.append(VideoOptions(lineId, lineRes, lineAud))

    for option in options:
        if option.getAud() > bestAudioOption.getAud():
            bestAudioOption = option
        if option.getRes() > bestVideoOption.getRes():
            bestVideoOption = option

    return bestVideoOption.getId(), bestAudioOption.getId()


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
        link = getLink(args)

    if '--webm' in args:
        ext = 'webm'

    if '--nomix' in args:
        mix = False

    if link is not None:
        response = getTypes(link)

        if response.decode('utf-8').startswith('ERROR'):
            print("ERROR: Invalid link.", file=sys.stderr)
        else:
            bestA, bestV = getBestOO(response, ext, mix)
            print("bestv:" + bestV, bestA)
            # Older version,
            # bestA, bestV, infoA, infoV = getBest(response, ext, mix)
            # print("Best " + ext + " quality found:\n" + infoV + '\n' + infoA)
            request = input("Download? Y/N \n")

    if request.lower() in ['yes', 'y']:
        downloadBest(bestV, bestA, link, ext)


if __name__ == '__main__':
    main()
