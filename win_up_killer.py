# -*- coding: utf-8 -*-
# =============================================================================
#                     GNU GENERAL PUBLIC LICENSE
#                        Version 3, 29 June 2007
# 
#  Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
#  Everyone is permitted to copy and distribute verbatim copies
#  of this license document, but changing it is not allowed.
#
#  Created on Sat Oct  6 18:16:03 2018
#
#  @author: Kikones
#
# =============================================================================
from winreg import *
import sys

def win_update_service_killer(aReg):
    try:
        my_proccess = 'Opening Windows Update Service'
        print('{}...'.format(my_proccess))
        bKey = OpenKey(aReg,r"SYSTEM\CurrentControlSet\Services\wuauserv", 0, KEY_SET_VALUE)  
        print('{} opened successfully!!!'.format(my_proccess))
        print('Changing {} initialization status...'.format(my_proccess))
        SetValueEx(bKey, 'Start',0,REG_DWORD, 4)
        print('{} initialization status changed successfully!!!'.format(my_proccess))
        print('Closing {}...'.format(my_proccess))
        CloseKey(bKey)
        print('{} closed successfully!!!'.format(my_proccess))
    except:
        print('Access Denied, are you root?')
        sys.exit()

def win_update__medice_service_killer(aReg):
    my_proccess = 'Windows Update Medic Service'
    try:
        print('Opening {}...'.format(my_proccess))
        bKey = OpenKey(aReg,r"SYSTEM\CurrentControlSet\Services\WaaSMedicSvc", 0, KEY_SET_VALUE)  
        print('{} opened successfully!!!'.format(my_proccess))
        print('Changing {} initialization status...'.format(my_proccess))
        SetValueEx(bKey, 'Start',0,REG_DWORD, 4)
        print('{} initialization status changed successfully!!!'.format(my_proccess))
        print('Closing {}...'.format(my_proccess))
        CloseKey(bKey)
        print('{} closed successfully!!!'.format(my_proccess))
    except:
        print('Access Denied, are you root?')
        sys.exit()
        
def win_orchestrator_service_killer(aReg):
    my_proccess = 'Update Orchestrator Service'
    try:
        print('Opening {}...'.format(my_proccess))
        bKey = OpenKey(aReg,r"SYSTEM\CurrentControlSet\Services\UsoSvc", 0, KEY_SET_VALUE)  
        print('{} opened successfully!!!'.format(my_proccess))
        print('Changing {} initialization status...'.format(my_proccess))
        SetValueEx(bKey, 'Start',0,REG_DWORD, 4)
        print('{} initialization status changed successfully!!!'.format(my_proccess))
        print('Closing {}...'.format(my_proccess))
        CloseKey(bKey)
        print('{} closed successfully!!!'.format(my_proccess))
    except:
        print('Access Denied, are you root?')
        sys.exit()
        
def main():
    print('Made by Kikones @2018 https://github.com/Kikones/')
    print('Initializing - Windows no More Updates...')
    print('Setting Up Local Machine Key')
    aReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)
    print('Starting to kill update services at registry.')
    win_update_service_killer(aReg)
    win_update__medice_service_killer(aReg)
    win_orchestrator_service_killer(aReg)
    print('Local Machine Key closed successfully!!!')
    CloseKey(aReg) 
    print('Finished the killing, closing Local Machine Key...')
    print('Finished - Windows no More Updates!!!')
    print('Please, restart your computer.')
    
if __name__ == '__main__':
    main()