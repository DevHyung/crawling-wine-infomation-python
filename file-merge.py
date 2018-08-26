import os
fileList =os.listdir('./미완/')
print(fileList)
print(len(fileList))

resultFile = open('vivino_url_list.txt','w')

for file in fileList:
    content = open('./미완/'+file).read()
    resultFile.write(content)
resultFile.close()