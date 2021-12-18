#Opening File OR We Say Read The File.

with open("F_1.txt",'r',encoding = "UTF-8") as file:
    content = file.read()

#After Read The File I Want to Repalce the "India" TO "America".

content = content.replace('America','India') 

#Write The File After the Changing.
with open("F_1.txt",'w',encoding = "UTF-8") as file:
    file.write(content)
