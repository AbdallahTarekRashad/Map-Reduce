#!/usr/bin/env python

import sys


def _format_and_split(line, separator='\t'):
    return line.strip().split(separator)


def _emit(elements, separator='\t'):
    elements_as_string = map(str, elements)
    output_string = separator.join(elements_as_string)
    print output_string


def _city_changed(city_of_previous_line, city_of_current_line):
    return (city_of_previous_line) and (city_of_previous_line != city_of_current_line)
def _item_changed(item_of_previous_line,item_of_current_line):
    return (item_of_previous_line) and (item_of_previous_line != item_of_current_line)

def reducer():
    loc = None
    item = None
    Q = 0
    for line in sys.stdin:
        line_elements = _format_and_split(line)
        if len(line_elements) != 3:
            continue

        itemid, location,qua = line_elements
        try:
            qua= int(qua)
        except ValueError:
            continue
        if _city_changed(loc , location) or _item_changed(item , itemid):
            _emit([item, loc, Q])
            Q = 0
        loc = location
        item = itemid

        Q = Q + qua
    if loc and item :
        _emit([item, loc, Q])

if __name__ == '__main__':
    reducer()
