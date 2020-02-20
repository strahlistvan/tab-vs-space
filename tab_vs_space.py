# -*- coding: utf-8 -*-

import sys
sys.path.append('./classes')

import Project as proj 

import configparser
import matplotlib.pyplot as plt

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
    labels = ['tabbed', 'spaced', 'mixed']
    
    plt.pie(indent_arr, labels=labels, autopct='%1.1f%%')
    plt.legend(labels, title=config[sect]['title'])
    plt.show()
    
    print('tabbed: '+str(project.tabbed))
    print('spaced: '+str(project.spaced))
    print('mixed: ' +str(project.mixed))
    #print(project.getsourcesbyindent('mixed'))
