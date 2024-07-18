import re

def solution(files):
    def split_file(file):
        original = file
        file = file.lower()
        num = re.search(r'[0-9]+', file).group()
        head, tail = re.split(num, file, maxsplit=1)
        return [head, int(num), original]

    fileInfo = [split_file(file) for file in files]
    
    fileInfo.sort(key = lambda x: (x[0], x[1]))

    return [file[2] for file in fileInfo]
