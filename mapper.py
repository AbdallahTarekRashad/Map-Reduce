#!/usr/bin/env python
import sys
location = "ZZZZZZZZ"
soc = None
qua = None
def _format_and_split(line, separator='\t'):
    return line.strip().split(separator)


def _emit(elements, separator='\t'):
    elements_as_string = map(str, elements)
    output_string = separator.join(elements_as_string)
    print output_string



def mapper():
    for line in sys.stdin:
        line_elements = _format_and_split(line)
        if len(line_elements) == 5 :
            InvoiceNo, StockCode, Description, Quantity,CustomerID = line_elements
            _emit([CustomerID,location,StockCode, Quantity ])
        if len(line_elements) == 4 :
            userid, loc, e_mail, language = line_elements
            _emit([userid,loc, soc, qua])
        if len(line_elements) != 5 or len(line_elements) != 4 :
            continue

if __name__ == '__main__':
    mapper()
