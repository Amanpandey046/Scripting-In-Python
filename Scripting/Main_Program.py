# open both files
with open('Check.txt','r') as firstfile, open('Basics.txt','a') as secondfile:
      
    # read content from first file
    for line in firstfile:
               
             # append content to second file
             secondfile.write("WhatsApp ")
