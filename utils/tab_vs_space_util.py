# -*- coding: utf-8 -*-
import re

def read_file(filename):
    with open(filename, 'r', encoding='utf8', errors='replace') as file:
        return file.readlines()

def trim(lines):
    lines = list(map(lambda s: s.rstrip(), lines))
    lines = list(filter(lambda s: len(s) > 0, lines))
    return lines

def first_non_whitespace_pos(line):
    matcher = re.search('[^\s]',line)
    if matcher != None:
        return matcher.start()
    return 0

def get_extension(filename):
    pos = filename.rfind('.')
    if pos != -1:
        return filename[pos+1:]
    return None

def is_source_code_file(filename, allowed_extensions=['c', 'cpp', 'js', 'java', 'php']):
    pos = filename.rfind('.')
    if pos != -1:
        ext = filename[pos+1:]
        if ext in allowed_extensions:
            return True
    return False

def is_tabbed_or_spaced(lines, indent_space_size = 4):
    lines = trim(lines)
    space_count = 0
    tab_count = 0
    for line in lines:
        line_indent = line[:first_non_whitespace_pos(line)]
        space_count += line_indent.count(' ')
        tab_count += line_indent.count('\t')

    if space_count > tab_count:
        return 'spaced'
    elif tab_count > indent_space_size*space_count:
        return 'tabbed'
    elif tab_count > 0 or space_count > 0:
        return 'mixed'
    return None

def text_to_tabs(text, indent_space_size = 4):
    lines = text.splitlines()
    lines = trim(lines)
    for i in range(len(lines)):
        pos = first_non_whitespace_pos(lines[i])
        line_indent = lines[i][:pos]
        line_content = lines[i][pos:]
        line_indent = line_indent.replace(indent_space_size*' ', '\t')
        lines[i] = line_indent + line_content
    return '\n'.join(lines)

def text_to_spaces(text, indent_space_size = 4):
    lines = text.splitlines()
    lines = trim(lines)
    for i in range(len(lines)):
        pos = first_non_whitespace_pos(lines[i])
        line_indent = lines[i][:pos]
        line_content = lines[i][pos:]
        line_indent = line_indent.replace('\t', indent_space_size*' ')
        lines[i] = line_indent + line_content
    return '\n'.join(lines)

def whitespace_ratio(text):
    lines = text.splitlines()
    if len(lines) == 0:
        return (None, None, 0)
    space_len = 0
    text_len = 0
    for line in lines:
        space_len += first_non_whitespace_pos(line)
        text_len += len(line)
    if text_len == 0:
        return (0, 0, 0)
    return (text_len, space_len, space_len/text_len)
