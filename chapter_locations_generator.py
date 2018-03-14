#!/usr/bin/env python3
"""script to create json file that maps kindle book locations to chapters"""
import json

def chapter_locations_from_input():
    """creates a dict with book locations as keys and chapter names as values from user input

    it will keep on asking for input until you type in 'q'
    """
    chapter_locations = []
    while True:
        print('register new chapter-location mapping')
        chapter_name = input('chapter name: ')
        if chapter_name == 'q':
            break
        location = input('last chapter location: ')
        if location == 'q':
            break

        chapter_locations.append({'chapter': chapter_name, 'location': location})
        print('chapter-location mapping registered')

    return chapter_locations

def dict_to_json_file(d, filename='chapter_locations.json'):
    with open(filename, 'w') as file:
        json.dump(d, file)

    print(f'chapter-locations mapping stored at {filename}')

if __name__ == '__main__':
    print('starting chapter-location registering')
    print('enter "q" to stop the script from asking for more input and store existing mappings in json file')
    chapter_locations = chapter_locations_from_input()
    dict_to_json_file(chapter_locations)
