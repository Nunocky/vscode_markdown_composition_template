#!/usr/bin/env python3

import json


def lastone(iterable):
    it = iter(iterable)
    last = next(it)

    for val in it:
        yield last, False
        last = val

    yield last, True



with open("INPUT.md", "w") as out : 
    with open("files.json", "r") as json_inp:
        fileList = json.load(json_inp)

        for file,isLast in lastone(fileList):
            with open(file, "r") as inp:
                out.write("<!-- %s -->\n" % file)
                s = inp.read()
                out.write(s)

                if not isLast:
                    out.write("<div class=\"page\"></div>\n\n")


