# -*- coding: utf-8 -*-

import sys
sys.path.append('./classes')
sys.path.append('./utils')


import Project as proj 

import configparser
import matplotlib.pyplot as plt

all_tabbed = 0
all_spaced = 0
all_mixed  = 0

all_sources_by_ext = dict()

import pandas as pd
sourceData = pd.DataFrame()

# read config file
config = configparser.ConfigParser()
config.read('./config.ini')

for sect in config.sections():
    print(config[sect]['root_path'])

    ext = config[sect]['allowed_extensions'].split(',')
    project = proj.Project(config[sect]['root_path'], ext)
    print(project.allowed_extensions)
    project.countindentstats()

    indent_arr = [project.tabbed, project.spaced, project.mixed]
    labels = ['tabbed ('+str(project.tabbed)+')'
             ,'spaced ('+str(project.spaced)+')'
             ,'mixed ('+str(project.mixed)+')']

    plt.pie(indent_arr, labels=labels, autopct='%1.1f%%')
    plt.legend(labels, title=config[sect]['title'], loc='upper right')
    plt.show()

    all_tabbed += project.tabbed
    all_spaced += project.spaced
    all_mixed  += project.mixed

    print('tabbed: '+str(project.tabbed))
    print('spaced: '+str(project.spaced))
    print('mixed: ' +str(project.mixed))
    #print(project.getsourcesbyindent('mixed'))

    for ext in project.used_extensions:
       # print(project.sources_by_ext[ext])
        if ext in all_sources_by_ext:
            all_sources_by_ext[ext].extend(project.sources_by_ext[ext])
        else:
            all_sources_by_ext[ext] = project.sources_by_ext[ext]

    for source in project.sources:
        this_src_df = pd.DataFrame({'path': source.path, 'ext': source.extension, 'indentstat': source.indentstat, 'project': project.pathroot}, index=[0])
        sourceData = sourceData.append(this_src_df)

# Summarize sources by file extension
#print(all_sources_by_ext)

print(sourceData.to_string())

#for ext in all_sources_by_ext:
   # print(ext)
   # for src in all_sources_by_ext[ext]:
   #     print(src.path)
   #     print(src.indentstat)