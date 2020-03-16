import os

print('Start Search...')
print('Make o file list')

for (path, dir, files) in os.walk("E:/MyFolder/Source\eclipse/test200313"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.c' or ext == '.cpp' or ext =='.S' or ext == '.s':
            print("%s/%s.o" % (path, filename.split('.')[0]))

