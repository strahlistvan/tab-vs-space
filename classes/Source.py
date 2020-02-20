# -*- coding: utf-8 -*-
import sys
sys.path.append('../utils')

import tab_vs_space_util as util

class Source:
    path = ''
    sourcecode = []

    extension = 'unknown'
    indentstat = 'unknown'
    ratio = 0.0

    def __init__(self, path):
        self.sourcecode = []
        self.path = path
        self.readsourcefrompath()
        self.analyze()

    def __str__(self):
        pattern = '[Object: Source]{{path: {}, ratio: {:02.4f}%, indentstat: {}}}';
        return pattern.format(self.path, 100*float(self.ratio), self.indentstat)

    def __repr__(self):
        return self.__str__()

    def readsourcefrompath(self):
        if self.path != '':
            self.sourcecode = util.read_file(self.path)

    def tospace(self):
        text = '\n'.join(self.sourcecode)
        self.sourcecode = util.text_to_spaces(text).split('\n')
        return self.sourcecode

    def totab(self):
        text = '\n'.join(self.sourcecode)
        self.sourcecode = util.text_to_tabs(text).split('\n')
        return self.sourcecode

    def analyze(self):
        self.indentstat = util.is_tabbed_or_spaced(self.sourcecode)
        text = '\n'.join(self.sourcecode)
        self.ratio = util.whitespace_ratio(text)[2]
