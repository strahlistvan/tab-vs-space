# -*- coding: utf-8 -*-

import os
import sys
sys.path.append('./classes')
sys.path.append('./utils')

import tab_vs_space_util as util
import Project as proj 
import matplotlib.pyplot as plt

#recursive list with WALK
folder_name = '../../workspace-sts-3.9.0.RELEASE\AudioJavaGame'

for root, subdirs, files in os.walk(folder_name):
    for filename in files:
        file_path = os.path.join(root, filename)
        if util.is_source_code_file(filename):
            source_lines = util.trim(util.read_file(file_path))

#recursive list with function call
def recursive_list(folder_name):
    for entry in os.scandir(folder_name):
        if not entry.is_dir():
            print(entry.name + ' is not directory')
            print(entry.path)
        else:
            recursive_list(os.path.join(folder_name,entry.name))

minesweeper = proj.Project('../Minesweeper') #proj.Project('../../workspace-sts-3.9.0.RELEASE\AudioJavaGame') # 

#minesweeper.tospace()

minesweeper.countindentstats()
print(minesweeper)

ms_arr = [minesweeper.tabbed, minesweeper.spaced, minesweeper.mixed]

labels = ['tabbed', 'spaced', 'mixed']

plt.pie(ms_arr, labels=labels, autopct='%1.1f%%')
plt.legend(labels, title='Minesweeper')
plt.show()

print(minesweeper.tabbed)
print(minesweeper.spaced)
print(minesweeper.mixed)
print(minesweeper)
#############################################

wp = proj.Project('../WordPress')

arr = [wp.tabbed, wp.spaced, wp.mixed]

labels = ['tabbed', 'spaced', 'mixed']

plt.pie(arr, labels=labels, autopct='%1.1f%%')
plt.legend(labels, title='WordPress')
plt.show()

print(wp.tabbed)
print(wp.spaced)
print(wp.mixed)
#print(wp.getsourcesbyindent('mixed'))

