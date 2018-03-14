#!/usr/bin/env python3
"""converts kindle output csv file to txt file with chapter names"""
import csv
import json
import sys
import re

start_line = 9

column_annotation_type = 0
column_location = 1
column_annotation = 3


def load_chapter_locations(chapter_locations_file='chapter_locations.json'):
    chapter_locations = json.load(open(chapter_locations_file))
    return chapter_locations


def format_highlight_row(row):
    annotation_type = row[column_annotation_type]
    annotation = row[column_annotation]
    if re.match('highlight', annotation_type, re.IGNORECASE):
        return annotation
    elif re.match('note', annotation_type, re.IGNORECASE):
        return '--' + annotation + '--'

def new_chapter(current_chapter_location_index, chapter_locations, annotation_location):
    current_highlight_location = int(annotation_location.split(' ')[1])
    current_chapter_location = chapter_locations[current_chapter_location_index]
    current_location = int(current_chapter_location['location'])
    if current_highlight_location > current_location:
        return True
    return False

def write_title_to_text(title, text):
    return text + '\n' + ('*' * 30) + '\n' + title + '\n' + ('*' * 30) + '\n'

def write_paragraph_to_text(paragraph, text):
    return text + '\n' + paragraph + '\n'


def extract_highlights(highlights_file, chapter_locations):
    current_chapter_location_index = 0
    output_text = ''
    output_text = write_title_to_text(chapter_locations[current_chapter_location_index]['chapter'], output_text)
    with open(highlights_file) as csv_file:
        csv_reader = csv.reader(csv_file)
        for i, row in enumerate(csv_reader):
            if i < start_line:
                continue
            else:
                annotation_location = row[column_location]
                if new_chapter(current_chapter_location_index, chapter_locations, annotation_location):
                    current_chapter_location_index += 1
                    output_text = write_title_to_text(chapter_locations[current_chapter_location_index]['chapter'], output_text)

                annnotation = format_highlight_row(row)
                output_text = write_paragraph_to_text(annnotation, output_text)

    return output_text

def text_to_file(text, file):
    with open(file, 'w') as f:
        f.write(text)
    print(f'notes succesfully store in file: {file}')

if __name__ == '__main__':
    print('formatting csv notes to txt...')
    highlights_file = sys.argv[1]
    output_file = sys.argv[2]
    chapter_locations_file = sys.argv[3]
    chapter_locations = load_chapter_locations(chapter_locations_file)
    highlights_text = extract_highlights(highlights_file, chapter_locations)
    text_to_file(highlights_text, output_file)
