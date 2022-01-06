# open both files
with open('Check.txt','r') as firstfile, open('Basics.txt','w') as secondfile:

    # read content from first file
    for line in firstfile:
       for word in line.split():
          if word == 'WhatsApp':
             # append content to second file
             secondfile.write(line)
