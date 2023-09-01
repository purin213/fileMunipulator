import sys

argList = sys.argv
inputPath = argList[2]

if len(argList) > 4:
    sys.stderr.write('Error! wrong argument length, please check from the list below. \n')

match argList[1]:
    case 'reverse':
        with open(inputPath, 'w') as f:
            content = f.read()
            outputPath = argList[3]

    case 'copy':
        with open(inputPath, 'x') as f:
            content = f.read()

    case 'duplicate':
        with open(inputPath, 'a') as f:
            content = f.read()
            for n in range(0, int(argList[3]):
                f.write("\n" + content)
