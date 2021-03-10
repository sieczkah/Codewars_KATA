"""https://www.codewars.com/kata/597770e98b4b340e5b000071/train/python"""

import re

class FileNameExtractor:
    def extract_file_name(dirty_file_name):
        x = re.findall(r'\d+_(.+?\..+?)\.', dirty_file_name)
        return x[0]
