# -*- coding: utf-8 -*-

import os
import sys

sys.path.append('../utils')

import tab_vs_space_util as util
from Source import Source

class Project:
    pathroot =''
    sources =[]
    mixed = 0
    tabbed = 0
    spaced = 0
    allowed_extensions = []
    used_extensions = set()

    def __init__(self, pathroot, allowed_extensions=['c', 'cpp', 'js', 'java', 'php'], indent_space_size = 4):
        print('Initet hívjuk itt')
        self.tabbed = 0
        self.mixed  = 0
        self.spaced = 0
        self.pathroot = pathroot
        self.sources = [] #sources
        self.allowed_extensions = allowed_extensions
        self.used_extensions = set()
        self.indent_space_size = indent_space_size
        self.readsourcefiles()
        self.countindentstats()

    def __str__(self):
        result = 'files in project: {}\n'.format(self.sourcefilecount())
        result += 'tabbed: {:d}\nspaced: {:d}\nmixed: {:d}\n'.format(self.tabbed, self.spaced, self.mixed)
        for src in self.sources:
            result += '{}\n'.format(src)
        return result

    def __repr__(self):
        return self.__str__()

    def readsourcefiles(self):
        for root, subdirs, files in os.walk(self.pathroot):
            subdirs[:] = [d for d in subdirs if d not in ['.git', '.github']] #exclude
            for filename in files:
                file_path = os.path.join(root, filename)
                if util.is_source_code_file(filename, allowed_extensions = self.allowed_extensions):
                    src = Source(file_path, indent_space_size = self.indent_space_size)
                    self.sources.append(src)
                    self.used_extensions.add(src.extension)

    def countindentstats(self):
        if len(self.sources) == 0:
            return
        self.filecount = len(self.sources)
        self.mixed = len(self.getsourcesbyindent('mixed'))
        self.tabbed = len(self.getsourcesbyindent('tabbed'))
        self.spaced = len(self.getsourcesbyindent('spaced'))
        return (self.tabbed, self.spaced, self.mixed)
    
    def getsourcesbyindent(self, indent):
        return list(filter(lambda src: src.indentstat == indent, self.sources))
    
    def tospace(self):
        for src in self.sources:
            src = src.tospace()

    def totab(self):
        for src in self.sources:
            src = src.totab()

    def sourcefilecount(self):
        src_filt = filter(lambda x: util.is_source_code_file(x.path), self.sources)
        return len(list(src_filt))