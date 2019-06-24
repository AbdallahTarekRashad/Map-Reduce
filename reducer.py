#!/usr/bin/env python

import sys


def _format_and_split(line, separator='\t'):
    return line.strip().split(separator)


def _emit(elements, separator='\t'):
    elements_as_string = map(str, elements)
    output_string = separator.join(elements_as_string)
    print output_string


def _city_changed(city_of_previous_line, city_of_current_line):
    return  (city_of_previous_line != city_of_current_line) and (city_of_current_line != 'ZZZZZZZZ')


def reducer():
    loc= None
    for line in sys.stdin:
        line_elements = _format_and_split(line)
        if len(line_elements) != 4:
            continue
        userid, location,item,qua = line_elements
        if _city_changed(loc, location):
            loc = location
        if item == 'None' or qua == 'None' :
            continue
        _emit([ item , loc , qua])

if __name__ == '__main__':
    reducer()
