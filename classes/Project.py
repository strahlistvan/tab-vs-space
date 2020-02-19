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
    def __init__(self, pathroot):
        self.pathroot = pathroot
        self.sources = []
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
            for filename in files:
                file_path = os.path.join(root, filename)
                if util.is_source_code_file(filename):
                    src = Source(file_path)
                    self.sources.append(src)

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
    
    def sourcefilecount(self):
        src_filt = filter(lambda x: util.is_source_code_file(x.path), self.sources)
        return len(list(src_filt))