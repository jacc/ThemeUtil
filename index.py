#!/usr/bin/env python3

# does this work

import shutil 
import os.path
import re
import json

def fileChecks():
    if os.path.exists('./DEBIAN/') and os.path.isfile('./DEBIAN/control'):
        print('[TU] DEBIAN folder and control file exist.')
    else:
        print('[TU] DEBIAN folder and control file do not exist, creating...')
        os.makedirs(os.path.dirname("./DEBIAN/"))
        buildControl('./DEBIAN/control')
            

def buildControl(control_path):
    with open(control_path, 'w') as control_file:
        print('[TU] Control file not created...please answer some questions about this package')
        theme_id = input('[TU] Theme bundle ID: ')
        theme_name = input('[TU] Theme name: ')
        theme_version = input('[TU] Theme version: ')
        theme_section = "Themes"
        theme_arch = "iphoneos-arm"
        theme_desc = input('[TU] Theme description: ')
        theme_author = input('[TU] Theme author(s): ')

        control_file.write('Package: {}\n'.format(theme_id))
        control_file.write('Name: {}\n'.format(theme_name))
        control_file.write('Version: {}\n'.format(theme_version))
        control_file.write('Section: {}\n'.format(theme_section))
        control_file.write('Package: {}\n'.format(theme_id))


        control_file.close()

        
        
def main():
    print('ThemeUtil [beta] [bad name] [internal testing v1]')
    print('[TU] Running file checks...')
    fileChecks()
    

main()