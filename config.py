#!/usr/bin/env python

'''
    Copyright (C) 2014 2015 Filipe Marques eagle[dot]software3[at]gmail[dot]com

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 3 of the License, or
    any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You received a copy of the GNU General Public License
    along with this program in License folder; if not, write to the Free Software
    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
    MA 02110-1301, USA.
'''

import subprocess

class Config:
	def __init__(self):
		subprocess.call("clear")
		
	def AddUser(self):
		print("Add User")

def main():
	conf = Config()
	
	while True:
		subprocess.call("clear")
		print("#########################################################################################")
		print("#                                                                                       #")
		print("#      instALler - Arch Linux installer - version 1.0.0                                 #")
		print("#      This program will install Arch Linux in this computer                            #")
		print("#      https://github.com/filipe-marques/installer                                      #")
		print("#                                                                                       #")
		print("#      instALler is developed by https://github.com/filipe-marques                      #")
		print("#     and is free software licensed under GNU GPL v.3+                                  #")
		print("#                                                                                       #")
		print("#      Please help me making this project better, by contributing:                      #")
		print("#     your code, ideas and feedback !                                                   #")
		print("#                                                                                       #")
		print("# All trademarks and registered trademarks are the property of their respective owners. #")
		print("#########################################################################################\n")
		print("THIS CONFIG FILE WILL HELP YOU INSTALL DESKTOP ENVIRONMENTS, DRIVERS, THEMES, ...\n")
		print("To be using this program, it assumed that you setup the network connection and are in root mode !\n")
		print("1 - Add User")
		print("2 - ")
		print("3 - ")
		print("4 - ")
		print("5 - ")
		print("6 - ")
		print("7 - ")
		print("8 - ")
		print("9 - \n")
		
		print("to exit press 'e' and then 'enter'")
		print("to finish press 'd' and then 'enter'\n")
		
		Option = input("Press number option: ")
		
		if Option == "1":
			conf.AddUser()
		if Option == "e":
			break

if __name__ == "__main__":
	main()
