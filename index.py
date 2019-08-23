#!/usr/bin/env python3

# does this work

import shutil 
import os.path
import re
import json

def fileChecks():
    if os.path.exists('./DEBIAN/') and os.path.isfile('./DEBIAN/control'):
        print('[TU] DEBIAN folder and control file exist.')
        edit_prompt = input('[TU] Would you like to make any changes to your control file? (y/n) ')

        if edit_prompt == "y":
            overrideControl('./DEBIAN/control')
        else:
            print('[←] Returning to main menu.\n')
            runMenu()

    else:
        create_prompt = input('[TU] Your DEBIAN and control file both do not exist. Would you like to create them now? (y/n) ')
        
        if create_prompt == "y":
            os.makedirs(os.path.dirname("./DEBIAN/"))
            buildControl('./DEBIAN/control')
        else:
            print('[←] Returning to main menu.\n')
            runMenu()
        
            
def buildControl(control_path):
    with open(control_path, 'w') as control_file:
        
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
        control_file.write('Architecture: {}\n'.format(theme_arch))
        control_file.write('Description: {}\n'.format(theme_desc))
        control_file.write('Author: {}\n'.format(theme_author))
    
        control_file.close()

def overrideControl(control_path):
    with open(control_path, "r+") as control_file:
        content = control_file.read().splitlines()
        print('[TU] Your current control file looks like this:')
        print('')

        for line in content:
            print(line)
        
        print('')
        override = input('[TU] What line would you like to make an edit to? (use 0-{}) '.format(len(content)-1))
        override_int = int(override)
        override_str = input('[TU] Enter new information (currently \'{}\'): '.format(content[override_int]))
        replace_line('./DEBIAN/control', override_int, override_str + "\n")

        loop = input('[TU] Would you like to edit another line? (y/n)')
        if loop == "y":
            overrideControl('./DEBIAN/control')
        else:
            print('[←] Returning to main menu.\n')
            runMenu()


# thanks stack overflow <3
def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    print('[TU] Line successfully overwritten.')
    out.close()

def runMenu():
    print('ThemeUtil Menu [internal testing v1]')
    print('Welcome back. What tasks would you like to run?')
    select = input('[1] Run file checks\n[2] Edit control file\n[3] Build new theme hierarchy\n[4] Quick-compile existing theme\n[5] Project information\n\n[!] Select 1-5: ')
    
    if select == "1":
        fileChecks()
    elif select == "2":
        overrideControl('./DEBIAN/control')
    elif select == "3":
        print('[!] Not yet programmed.')
    elif select == "4":
        print('[!] Not yet programmed.')
    elif select == "5":
        print('[!!] Jack is lazy and doesn\'t want to write this :(\n')
        runMenu()



runMenu()