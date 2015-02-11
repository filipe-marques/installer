#!/usr/bin/env python

'''
    Copyright 2014 2015 Filipe Marques <eagle.software3@gmail.com>

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

class Installer:
	def __init__(self):
		subprocess.call("clear")
		print("###################################################################################")
		print("#                                                                                 #")
		print("#      instALler - Installer for Arch Linux                                       #")
		print("#      This program will install Arch Linux in this computer                      #")
		print("#                                                                                 #")
		print("###################################################################################")
		
		print("Installation sequence: ")
		print("For simplicity this program installs and configure root and swap !!!")
		print(" - Set Network Connection (Wired or Wireless)")
		print(" - Set Keyboard Layout")
		print(" - Define Partitions")
		print(" - Create File Systems")
		print(" - Mount Partitions")
		print(" - Install Packages: base base-devel")
		print(" - Generating an fstab file")
		input("Press Enter to begin installation ...")
		
	
	#def check_uefi(self):
		
	
	#def check_bios(self):
		
	def network(self):
		subprocess.call("clear")
		print("Checking if you have wired network ...")
		if subprocess.call(["ping", "-c", "3", "www.google.com"]) == 0:
			print("You have wired network")
			input("Press Enter to continue ...")
		else:
			print("Checking wireless network ... please wait !")
			subprocess.call(["iw", "dev"])
			input("Press Enter to continue ...")
			subprocess.call("wifi-menu")
			if subprocess.call(["ping", "-c", "3", "www.google.com"]) == 0:
				print("You have now network connection !!!")
			else:
				print("You don't have network connection - Executing again wifi-menu !!!")
				subprocess.call("wifi-menu")
			input("Press Enter to continue ...")
	
	def set_keyboard_layout(self):
		subprocess.call("clear")
		print("Setting Keyboard Layout")
		input("Press Enter to continue ... ")
		subprocess.call(["localectl", "list-keymaps"])
		keys = input("Set Keyboard Layout: ")
		subprocess.call(["loadkeys", keys])
		print("Setting Language - Default English (U.S.)")
		subprocess.call(["nano", "/etc/locale.gen"])
		print("Generating Language Settings")
		subprocess.call("locale-gen")
		language = input("Please tell what is your language to run export command: ")
		subprocess.call(["export","LANG=",language])
		input("Press Enter to continue ... ")
	
	def partition(self):
		subprocess.call("clear")
		input("Press Enter to continue to partition the disk ...")
		partition = input("Please select what is your program for partitionning: ")
		subprocess.call([partition, "/dev/sda"])
		input("Press Enter to continue ... ")
	
	def create_filesystems(self):
		subprocess.call("clear")
		print("Listing partitions on hard disk: ")
		subprocess.call(["lsblk", "/dev/sda"])
		root_part = input("Please insert the partition for root: ")
		subprocess.call(["mkfs.ext4", root_part])
		input("Press Enter to continue ... ")
		swap = input("Please insert the partition for swap: ")
		subprocess.call(["mkswap", swap])
		print("Swapon running: ")
		subprocess.call(["swapon" + swap])
		input("Press Enter to continue ... ")
	
	def mount_partitions(self):
		subprocess.call("clear")
		input("Press Enter to mount the root partition ...")
		root = input("Please insert the root partition: ")
		subprocess.call(["mount", root, " /mnt"])
		input("Press Enter to continue ... ")
	
	def select_mirrors(self):
		subprocess.call("clear")
		print("Selecting mirrors ...")
		print("If you want, you can make it the only mirror available by deleting all other lines, but it is usually a good idea to have a few more, in case the first one goes offline.")
		input("Press Enter to continue ... ")
		subprocess.call(["nano","/etc/pacman.d/mirrorlist"])
		input("Press Enter to continue ... ")
	
	def install_the_base_system(self):
		subprocess.call("clear")
		print("Installing base system ...")
		input("Press Enter to continue ... ")
		subprocess.call(["pacstrap", "/mnt", "base", "base-devel"])
		print("Installed Base System !!!")
		input("Press Enter to continue ... ")
	
	def generating_an_fstab(self):
		subprocess.call("clear")
		print("Generating an fstab file ...")
		print("Warning: The fstab file should always be checked after generating it. If you encounter errors running genfstab or later in the install process, do not run genfstab again; just edit the fstab file.")
		subprocess.call(["genfstab", "-U", "-p", "/mnt", ">>", "/mnt/etc/fstab"])
		input("Check if everything went ok ... press enter")
		subprocess.call(["nano", "/mnt/etc/fstab"])
		input("Press Enter to continue ... ")
	
def main():
	ins = Installer()
	ins.network()
	ins.set_keyboard_layout()
	ins.partition()
	ins.create_filesystems()
	ins.mount_partitions()
	ins.select_mirrors()
	ins.install_the_base_system()
	ins.generating_an_fstab()
	
	# how to execute commands in arch chroot bash environment - someone test this subject !!!

if __name__ == "__main__":
	main()
