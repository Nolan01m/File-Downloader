import os
import wget
from zipfile import ZipFile

os.mkdir("C:/Users/Nolan/Desktop/Downloads")
path = "C:/Users/Nolan/Desktop/Downloads"
os.chdir(path)

url = input('Paste your URL Here:')
wget.download(url)
print("File Downloaded!")

for f in os.listdir(path):
	if f.endswith(".zip"):
		print(os.path.join(path, f))
		file = f
		
with ZipFile(file, 'r') as zipobj:
			zipobj.extractall()
		
os.remove(file)
print('File extracted and Zip removed')
