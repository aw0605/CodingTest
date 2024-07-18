import re

def solution(files):

    def split_file(file):
        head,num,tail = re.match(r'([a-zA-Z-. ]+)(\d{,5})(.*)',file).groups()
        return [head,int(num)]

    return sorted(files, key = lambda x: split_file(x.lower()))