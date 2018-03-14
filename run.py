#!/usr/bin/env python3
"""converts kindle output csv file to txt file with chapter names"""
import sys

title_line = 2
start_line = 9

column_annotation_type = 0
column_location = 1
column_annotation = 3

chapters = {}

if __name__ == '__main__':
    highlights_file = sys.argv[1]
    chapters_file = sys.argv[2]