def nani():
    import difflib
    import sys

    # fromfile = "xxx"
    # tofile = "zzz"
    # fromlines = open(fromfile, 'U').readlines()
    # tolines = open(tofile, 'U').readlines()
    fromlines = "aabccd"
    tolines = "aabcccd"


    # diff = difflib.HtmlDiff().make_file(fromlines, tolines, fromfile, tofile)
    diff = difflib.HtmlDiff().make_table(fromlines, tolines)
    print(diff)

if __name__ == '__main__':
    nani()
