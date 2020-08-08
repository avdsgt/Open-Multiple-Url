import webbrowser #importing browser library 

file1=open('url.txt', 'r') # Open text file as read argument
file2=file1.readlines() #Reading all urls line by line

#inserting url in loop
for urls in file2:
	webbrowser.open(urls);
print ("Code Run Successfuly")
