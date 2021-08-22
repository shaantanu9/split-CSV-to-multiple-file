

csvfile = open('/home/shantanu/Downloads/noeven123.csv', 'r').readlines()
filename = 1
for i in range(len(csvfile)):
     if i % 1000 == 0:
         open(str(filename) + '.csv', 'w+').writelines(csvfile[i:i+1000])
         filename += 1