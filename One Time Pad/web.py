import webbrowser
import os
new = 2
filename = os.getcwd()
url = "file://"+filename+"/templates/index.html"
webbrowser.open(url,new=new)