#!/usr/bin/env python3

import os
import re


class Replacement:
    def __init__(self, to, comment):
        self.to = to
        self.comment = comment


def from_chromejs(lines):
    mappings = {}
    for line in lines:
        match = re.search('^"(?P<from>.+)": "\\\\u(?P<to>.+)", // (?P<comment>.+)$', line)
        if match is not None:
            f = match.group('from').replace('\\"', '"').replace('\\\\', '\\')
            t = chr(int(match.group('to'), 16))
            c = match.group('comment')
            mappings[f] = Replacement(t, c)
    return mappings


def to_tree(mappings):
    tree = {}
    for src, mapping in mappings.items():
        branch = tree
        for pos, char in enumerate(src):
            if pos == (len(src) - 1):  # last character
                if char in branch:
                    raise Exception("subpath is supposed to return a character")
                branch[char] = mapping
            else:  # not last character
                if char not in branch:
                    branch[char] = {}
            branch = branch[char]
    return tree


def to_macos(mappings, depth=0):
    if depth == 0:
        yield '{'
        depth = depth + 1
    for key, value in mappings.items():
        escaped = key.replace('\\', '\\\\').replace('"', '\\"')
        spaces = depth * '  '
        if isinstance(value, dict):
            yield '%s"%s" = {' % (spaces, escaped)
            yield from to_macos(value, depth+1)
            yield '%s};' % (spaces)
        else:
            yield '%s"%s" = ("insertText:", "%s"); /* %s */' % (spaces, escaped, value.to, value.comment)
    if depth == 1:
        yield '}'


def default():
    with open(os.path.dirname(os.path.realpath(__file__)) + '/google-chrome-os/composekey/background.js') as fin:
        for line in to_macos({'§': to_tree(from_chromejs(fin))}):
            print(line)


if __name__ == '__main__':
    default()
