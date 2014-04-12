#!/usr/bin/env python3
# encoding: utf-8

import sys
from itertools import islice
from pylib.decorators import memoized

@memoized
def get_line(fileName, lineNo):
    with open(fileName) as f:
        return f.read().splitlines()[lineNo-1].rstrip()

def trace_calls(frame, event, arg):
    if event != 'call':
        return
    co = frame.f_code
    func_name = co.co_name
    func_line_no = frame.f_lineno
    func_filename = co.co_filename

    line = get_line(func_filename, func_line_no)

    print('{}:({}) {}'.format(func_filename, func_line_no, line))

    return trace_calls

if __name__ == '__main__':
    def b():
        print('in b()')
    def a():
        print('in a()')
        b()
    sys.settrace(trace_calls)
    a()