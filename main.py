import sys
import shutil

argList = sys.argv
operation = argList[1]
inputPath = argList[2]

if len(argList) > 5:
    sys.stderr.write('Error! wrong argument length, please check that you have the right command from the list below. \nreverse\ncopy\nduplicate\nreplace')

if operation == 'reverse':
    with open(inputPath, 'r') as input:
        content = input.read()
        with open(argList[3], 'w') as output:
            output.write(content[::-1])
#<<<doing something different>>>
elif operation == 'copy':
    shutil.copy(inputPath, argList[3])
elif operation == 'duplicate':
    with open(inputPath, 'r') as input:
        content = input.read()
        with open(inputPath, 'w') as output:
            for n in range(0, int(argList[3])):
                output.write("\n" + content)
elif operation == 'replace':
    with open(inputPath, 'r') as input:
        content = input.read()
        with open(inputPath, 'w') as output:
            output.write(content.replace(argList[3], argList[4]))
else: sys.stderr.write('Error! wrong command, please check you have the right command from the list below. \nreverse\ncopy\nduplicate\nreplace')
