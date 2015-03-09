#! /usr/bin/env python

import sys, webbrowser

def main():
    args = sys.argv[1:]
    if not args:
        #print "Usage: %s querystring" % sys.argv[0]
        url = "http://unixhelp.ed.ac.uk/CGI/man-cgi"
        webbrowser.open(url)
        return
    list = []
    for arg in args:
        if '+' in arg:
            arg = arg.replace('+', '%2B')
        if ' ' in arg:
            arg = '"%s"' % arg
        arg = arg.replace(' ', '+')
        list.append(arg)
    s = '+'.join(list)
    url = "http://unixhelp.ed.ac.uk/CGI/man-cgi?%s" % s
    webbrowser.open(url)

if __name__ == '__main__':
    main()
