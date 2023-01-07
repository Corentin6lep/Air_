import os
import subprocess


a=["air[00].py","air[01].py","air[02].py","air[03].py","air[04].py","air[05].py","air[06].py","air[07].py","air[08].py""air[09].py","air[10].py","air[11].py","air[12].py"]
j=0
b=0
for i in a:
    j=j+1
    filename = 'C:/Users/cl/Desktop/github/air/'+ i
    if os.access(filename, os.X_OK) == "False":
        print(i, "\033[91m: failure\033[0m")
        
    else:
        print(i,"\033[32m:success\033[0m")
        b=b+1
print("Total success:(",b,"/",j,")")

