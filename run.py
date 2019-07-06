#!/usr/bin/env python3
"""converts kindle output csv file to txt file with chapter names"""
import csv
import json
import sys
import re

start_line = 8

column_annotation_type = 0
column_location = 1
column_annotation = 3

def write_paragraph_to_text(row, text):
    annotation_type = row[column_annotation_type]
    annotation = row[column_annotation]
    if re.match('highlight', annotation_type, re.IGNORECASE):
        return text + '\n\n' + annotation
    elif re.match('note', annotation_type, re.IGNORECASE):
        return  text + '/*' + annotation + '*/'



def extract_highlights(highlights_file):
    output_text = ''
    with open(highlights_file) as csv_file:
        csv_reader = csv.reader(csv_file)
        for i, row in enumerate(csv_reader):
            if i < start_line:
                continue
            else:
                output_text = write_paragraph_to_text(row, output_text)

    return output_text


def text_to_file(text, file):
    with open(file, 'w') as f:
        f.write(text)
    print(f'notes successfully stored in file: {file}')


if __name__ == '__main__':
    print('formatting csv notes to txt...')
    highlights_file = sys.argv[1]
    output_file = sys.argv[2]
    highlights_text = extract_highlights(highlights_file)
    text_to_file(highlights_text, output_file)
