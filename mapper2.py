#!/usr/bin/env python
import sys
def _format_and_split(line, separator='\t'):
    return line.strip().split(separator)


def _emit(elements, separator='\t'):
    elements_as_string = map(str, elements)
    output_string = separator.join(elements_as_string)
    print output_string



def mapper():
    for line in sys.stdin:
        line_elements = _format_and_split(line)
        if len(line_elements) !=3:
            continue
        itemid, location, Quantity= line_elements
        _emit([itemid,location, Quantity ])

if __name__ == '__main__':
    mapper()
