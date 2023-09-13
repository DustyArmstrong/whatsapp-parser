import csv
import regex as re


chatFile = '_chat.txt'

chat = open(chatFile, encoding='utf-8')
dateRegex = r"[0-9]{2}[\/\-\.]{1}[0-9]{2}[\/\-\.]{1}[0-9]{4}"
timeRegex = r"[\d]{2}:[\d]{2}:[\d]{2}"
nameRegex = r"(?<=[0-9]{2}[\/\-\.]{1}[0-9]{2}[\/\-\.]{1}[0-9]{4}, [\d]{2}:[\d]{2}:[\d]{2}]) [^:]*"
messageRegex = r"(?<=[0-9]{2}[\/\-\.]{1}[0-9]{2}[\/\-\.]{1}[0-9]{4}, [\d]{2}:[\d]{2}:[\d]{2}].+?(?=:):).*"
lines = []

with open('output.csv', "w", errors='ignore') as file:
    csv_file = csv.writer(file)
    csv_file.writerow(["Index", "Date", "Time", "Author", "Content"])
    count = 1
    for line in chat:
        try:
            dateIndex = re.search(dateRegex, line)
            timeIndex = re.search(timeRegex, line)
            nameIndex = re.search(nameRegex, line)
            messageIndex = re.search(messageRegex, line)
            mediaParse = re.search("[0-9]{8}-[A-Z]{5}-[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{2}-[0-9]{2}-[0-9]{2}.[a-z 0-9]{3}", messageIndex.group())
            if mediaParse:
                csv_file.writerow([count, dateIndex.group(), timeIndex.group(), nameIndex.group(), '=HYPERLINK("./media/' + mediaParse.group() + '", "SHARED FILE IN CHAT - CLICK TO VIEW")'])
                count = count + 1
            else:
                csv_file.writerow([count, dateIndex.group(), timeIndex.group(), nameIndex.group(), messageIndex.group()])
                count = count + 1
        except AttributeError:
            line = line.strip("\n") 
            csv_file.writerow([count, "", "", "", str(line)])
            count = count + 1
