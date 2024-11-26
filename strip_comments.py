# Complete the solution so that it strips all text that follows any of a set of comment markers passed in.
# Any whitespace at the end of the line should also be stripped out.

def strip_comments(strng, markers):
    lines = strng.split('\n')
    for marker in markers:
        lines = [line.split(marker)[0].rstrip() for line in lines]
    return '\n'.join(lines)

