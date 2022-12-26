import os
folder = r'[folderpath]' #example: [folder = r'C:\Users\Student.ICSPLAB11\Downloads\images\\']  
count = 1 # count increase by 1 in each iteration

for file_name in os.listdir(folder): # iterate all files from a directory
    
    source = folder + file_name # Construct old file name    
    destination = folder + "img" + str(count) + ".jpg" # Adding the count to the new file name and extension
    
    os.rename(source, destination) # Renaming the file
    count += 1
    
print('Rename Successful')

print('Updated names')

res = os.listdir(folder)
print(res)
