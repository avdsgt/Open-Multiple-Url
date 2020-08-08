import webbrowser

file1=open('urls.txt', 'r')
file2=file1.readlines()

for urls in file2:
	webbrowser.open(url);
