import sys
import codecs

lines = []
lines.append("[")
temp= ""
fileName = sys.argv[1]
withTime = len(sys.argv) > 2 and sys.argv[2].lower() == "t"
index = -1

f = codecs.open(fileName, 'r')
for line in f:
    if line.isspace():
        continue
    
    if "-->" in line:
        lines.pop()
        if index > 0:
            lines.append('"},\n')

        text = ""
        if withTime:
            timeDetails = line.strip().replace(" ", "").replace(",", ":").split("-->")
            text = '{{"Number": {}, "StartTime": {}, "EndTime": {},"Text": "'.format(temp, timeDetails[0], timeDetails[1])
	else:		
            text = '{{"Number": {}, "Text": "'.format(temp)
        lines.append(text) 
        continue
    
    temp = line.strip().replace('"', '\\"')   
    lines.append(' {}'.format(temp))
    index += 1

lastLine = lines.pop()[:-2]
lines.append(lastLine)
lines.append("\"}]")

newFileName = '{}.json'.format(fileName.split('.')[0])
rf = codecs.open(newFileName, 'w')
rf.write(''.join(lines))
rf.close()

print '{} is created.'.format(newFileName)
