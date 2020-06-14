# -*- coding: utf-8 -*-

import sys
sys.path.append('./classes')
sys.path.append('./utils')

import Project as proj 

import configparser
import matplotlib.pyplot as plt
import pandas as pd

all_tabbed = 0
all_spaced = 0
all_mixed  = 0

all_sources_by_ext = dict()
source_df = pd.DataFrame()

# read config file
config = configparser.ConfigParser()
config.read('./config_m.ini')

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

    all_tabbed = all_tabbed + project.tabbed
    all_spaced = all_spaced + project.spaced
    all_mixed  = all_mixed + project.mixed

    print('tabbed: '+str(project.tabbed))
    print('spaced: '+str(project.spaced))
    print('mixed: ' +str(project.mixed))

    # Add source files to a DataFrame for easier data filtering and aggregation
    for src in project.sources:
        source_df = source_df.append({'path': src.path, 'extension': src.extension, 'indent type': src.indentstat, 'project': project.pathroot}, ignore_index=True)

# Summarize sources by file extension
grouped_df = pd.crosstab(source_df['extension'], source_df['indent type'])
grouped_df.plot.bar()
