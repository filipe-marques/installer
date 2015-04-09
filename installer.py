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
	
	#def check_uefi(self):
	#def check_bios(self):
	
	def SetKeyMap(self):
		print("Setting KeyMap")
		print("KeyMap - https://wiki.archlinux.org/index.php/KEYMAP")
		print("The KEYMAP variable is specified in the /etc/rc.conf file.\nIt defines what keymap the keyboard is in the virtual consoles.\nKeytable files are provided by the kbd package.")
		subprocess.call(["localectl", "list-keymaps"])
		keymap = input("Please enter the keymap: ")
		subprocess.call(["loadkeys", keymap])
		input("Press Enter to continue ...")
		
	def InfoTextEditor(self):
		subprocess.call("clear")
		print("Default text editor: nano text editor")
		input("Press Enter to continue ...")
		
	def Network(self):
		subprocess.call("clear")
		print("Option: 1 - Network")
		print("Do you want to use Wired or Wireless network ?")
		choice = input("Please insert your choice: (1 - Wired) (2 - Wireless) ")
		
		if choice == "1":
			subprocess.call(["ping", "-c", "3", "www.google.com"])
			print("Printing available networks: ")
			subprocess.call(["systemctl", "stop", "dhcpcd.service"])
			subprocess.call(["ip", "link"])
			wired = input("Please insert the wired network interface: ")
			subprocess.call(["ip", "link", "set", wired, "up"])
			print("You have now network ...")
			subprocess.call(["ping", "-c", "3", "www.google.com"])
		
		if choice == "2":
			print("Checking wireless network ... please wait !")
			subprocess.call(["iw", "dev"])
			wireless = input("Please insert the wireless network interface: ")
			subprocess.call("wifi-menu", wireless)
			if subprocess.call(["ping", "-c", "3", "www.google.com"]) == 0:
				print("You have now network connection !!!")
			else:
				print("You don't have network connection - Executing again wifi-menu !!!")
				subprocess.call("wifi-menu", wireless)
			input("Press Enter to continue ...")
	
	def Partition(self):
		subprocess.call("clear")
		print("Option: 3 - Partition")
		input("Press Enter to continue to partition the disk ...")
		partition = input("Please select what is your program for partitionning: ")
		subprocess.call([partition, "/dev/sda"])
		input("Press Enter to continue ... ")
	
	def CreateFileSystems(self):
		subprocess.call("clear")
		print("Option: 4 - Create File Systems")
		print("Listing partitions on hard disk: ")
		subprocess.call(["lsblk", "/dev/sda"])
		root_part = input("Please insert the partition for root: ")
		subprocess.call(["mkfs.ext4", root_part])
		input("Press Enter to continue ... ")
		swap = input("Please insert the partition for swap: ")
		subprocess.call(["mkswap", swap])
		print("Swapon running: ")
		subprocess.call(["swapon", swap])
		input("Press Enter to continue ... ")
	
	def MountPartitions(self):
		subprocess.call("clear")
		print("Option: 5 - Mount Partitions")
		input("Press Enter to mount the root partition ...")
		root = input("Please insert the root partition: ")
		subprocess.call(["mount", root, " /mnt"])
		input("Press Enter to continue ... ")
	
	def SelectMirrors(self):
		subprocess.call("clear")
		print("Option: 6 Step 1 - Select Mirrors")
		print("Selecting mirrors ...")
		print("If you want, you can make it the only mirror available by deleting all other lines,\nbut it is usually a good idea to have a few more,\nin case the first one goes offline.")
		input("Press Enter to continue ... ")
		subprocess.call(["nano","/etc/pacman.d/mirrorlist"])
		input("Press Enter to continue ... ")
	
	def InstallBaseSystem(self):
		subprocess.call("clear")
		print("Option: 6 Step 2 - Install Base System")
		print("Install base system: base , base-devel , python , \n iw , wireless_tools , wpa_actiond , wpa_supplicant , dialog")
		input("Press Enter to continue ... ")
		subprocess.call(["pacstrap", "/mnt", "base", "base-devel", "python", "iw", "wireless_tools", "wpa_actiond", "wpa_supplicant", "dialog"])
		print("Installed Base System !!!")
		input("Press Enter to continue ... ")
	
	def GeneratingFstab(self):
		subprocess.call("clear")
		print("Option: 7 - Generating Fstab")
		print("Generating an fstab file ...")
		print("Warning: The fstab file should always be checked after generating it.\nIf you encounter errors running genfstab or later in the install process, do not run genfstab again; just edit the fstab file.")
		subprocess.call(["genfstab", "-U", "-p", "/mnt", ">>", "/mnt/etc/fstab"])
		input("Check if everything went ok ... press enter")
		subprocess.call(["nano", "/mnt/etc/fstab"])
		input("Press Enter to continue ... ")
		
	def ConfigureSystem(self):
		subprocess.call("clear")
		print("Option: 8 - Configure System")
		print("Option: 8 Step 1 - Configure Locale")
		print("Locale - https://wiki.archlinux.org/index.php/Locale")
		print("Locales are used in Linux to define which language the user uses.\nAs the locales define the character sets being used as well, setting up the correct locale\n is especially important if the language contains non-ASCII characters.\nhttps://wiki.archlinux.org/index.php/Locale#Per_user")
		print("The locale specified in the LANG variable must be uncommented in /etc/locale.gen.\necho LANG=en_US.UTF-8 > /etc/locale.conf")
		
		input("Press Enter to continue ... ")
		subprocess.call(["arch-chroot", "/mnt", "/bin/bash", "-c", "nano /etc/locale.gen"])
		input("Press Enter to continue ... ")

		print("Generating Locale: ... ")
		subprocess.call(["arch-chroot", "/mnt", "/bin/bash", "-c", "locale-gen"])
		print("Setting en_US.UTF-8 as the system-wide locale allows to keep system logs in English for easier troubleshooting. Users can override this setting for their environment as required.")
		input("Press Enter to continue ... ")
		
		subprocess.call(["arch-chroot", "/mnt", "/bin/bash", "-c", "echo LANG=en_US.UTF-8 > /etc/locale.conf"])
		print("echo LANG=en_US.UTF-8 > /etc/locale.conf")
		input("Press Enter to continue ... ")
		
		subprocess.call("clear")
		print("Option: 8 Step 2 - Configure KeyMap")
		print("If you changed the default console keymap and font in the beginning of installation, you will have to edit /etc/vconsole.conf accordingly\n(create it if it does not exist) to make those changes persist in the installed system.\n Example: KEYMAP=de-latin1 FONT=lat9w-16")
		subprocess.call(["localectl", "list-keymaps"])
		input("Press Enter to continue ... ")
		subprocess.call(["arch-chroot", "/mnt", "/bin/bash", "-c", "nano /etc/vconsole.conf"])
		input("Press Enter to continue ... ")
		
		subprocess.call("clear")
		print("Option: 8 Step 3 - Configure Time Zone")
		print("Available time zones and subzones can be found in the /usr/share/zoneinfo/Zone/SubZone directories.\nTo view the available zones, check the directory /usr/share/zoneinfo/")
		print("Listing: ls /usr/share/zoneinfo/")
		input("Press Enter to continue ... ")
		subprocess.call(["arch-chroot", "/mnt", "/bin/bash", "-c", "ls /usr/share/zoneinfo/"])
		zone = input("Please insert your zone: ")
		subprocess.call(["arch-chroot", "/mnt", "/bin/bash", "-c", "ls /usr/share/zoneinfo/"+zone])
		input("Press Enter to continue ... ")
		subzone = input("Please insert your subzone: ")
		print("Processing: ln -s /usr/share/zoneinfo/"+zone+"/"+subzone+" /etc/localtime")
		subprocess.call(["arch-chroot", "/mnt", "/bin/bash", "-c", "ln -s /usr/share/zoneinfo/"+zone+"/"+subzone+" /etc/localtime"])
		input("Press Enter to continue ... ")
		
		subprocess.call("clear")
		print("Option: 8 Step 4 - Configure Hardware Clock")
		print("Hardware Clock Time - https://wiki.archlinux.org/index.php/Internationalization")
		print("Set the hardware clock mode uniformly between your operating systems.\nOtherwise, they may overwrite the hardware clock and cause time shifts.")
		print("It is recommended UTC, however, localtime is discouraged used by default in Windows:\nWarning: Using localtime may lead to several known and unfixable bugs.\nHowever, there are no plans to drop support for localtime.")
		opt = input("Please insert your option: (1 - UTC) (2 - LocalTime) ")
		if opt == "1":
			subprocess.call(["arch-chroot", "/mnt", "/bin/bash", "-c", "hwclock --systohc --utc"])
			print("Chosed option: UTC")
		if opt == "2":
			subprocess.call(["arch-chroot", "/mnt", "/bin/bash", "-c", "hwclock --systohc --localtime"])
			print("Chosed option: LocalTime")
		input("Press Enter to continue ... ")
		
		subprocess.call("clear")
		print("Option: 8 Step 5 - Configure HostName")
		hostname = input("Please insert a name for your hostname: ")
		subprocess.call(["arch-chroot", "/mnt", "/bin/bash", "-c", "echo "+hostname+" > /etc/hostname"])
		print("Add the same hostname to /etc/hosts: ")
		print('''	# /etc/hosts: static lookup table for host names
					#
					#<ip-address>		<hostname.domain.org>	<hostname>
					127.0.0.1			localhost.localdomain	localhost myhostname	
					::1					localhost.localdomain	localhost myhostname
					# End of file\n''')
		input("Press Enter to continue ... ")
		subprocess.call(["arch-chroot", "/mnt", "/bin/bash", "-c", "nano /etc/hosts"])
		input("Press Enter to continue ... ")
		
		subprocess.call("clear")
		print("Option: 8 Step 6 - Configure Network")
		print("Checking wired network: ...")
		subprocess.call(["arch-chroot", "/mnt", "/bin/bash", "-c", "ip link"])
		print("Wired ...")
		wired2 = input("Please insert the wired interface: ")
		subprocess.call(["arch-chroot", "/mnt", "/bin/bash", "-c", "systemctl enable dhcpcd@"+wired2+".service"])
		input("Press Enter to continue ... ")
		
		# After installation and rebooting
		#print("Wireless ...")
		#subprocess.call(["arch-chroot", "/mnt", "/bin/bash", "-c", "ip link"])
		#wireless2 = input("Please insert the wireless interface: ")
		#subprocess.call(["arch-chroot", "/mnt", "/bin/bash", "-c", "systemctl enable dhcpcd@"+wireless2+".service"])
		
	def CreateRamDisk(self):
		subprocess.call("clear")
		print("Option: 9 - Create Initial Ram Disk Environment")
		subprocess.call(["arch-chroot", "/mnt", "/bin/bash", "-c", "mkinitcpio -p linux"])
		input("Press Enter to continue ... ")
		
	def SetRootPassword(self):
		subprocess.call("clear")
		print("Option: 10 - Set the Root Password")
		print("Please insert your root password: ")
		subprocess.call(["arch-chroot", "/mnt", "/bin/bash", "-c", "passwd"])
		input("Press Enter to continue ... ")
		
	def InstallConfigureBootloader(self):
		subprocess.call("clear")
		print("Option: 11 - Install and Configure the Bootloader")
		#print("Please insert your root password: ")
		#subprocess.call(["arch-chroot", "/mnt", "/bin/bash", "-c", "passwd"])
		input("Press Enter to continue ... ")
		
		
		subprocess.call(["arch-chroot", "/mnt", "/bin/bash", "-c", ""])
		subprocess.call(["arch-chroot", "/mnt", "/bin/bash", "-c", ""])
		subprocess.call(["arch-chroot", "/mnt", "/bin/bash", "-c", ""])
		subprocess.call(["arch-chroot", "/mnt", "/bin/bash", "-c", ""])
		subprocess.call(["arch-chroot", "/mnt", "/bin/bash", "-c", ""])
		subprocess.call(["arch-chroot", "/mnt", "/bin/bash", "-c", ""])
		subprocess.call(["arch-chroot", "/mnt", "/bin/bash", "-c", ""])
		
#		arch-chroot /mnt /bin/bash -c "ln -s /usr/share/zoneinfo/${ZONE}/${SUBZONE} /etc/localtime"
#		subprocess.call(["arch-chroot", "/mnt", "/bin/bash", "-c", "ln -s /usr/share/zoneinfo/${ZONE}/${SUBZONE} /etc/localtime"])
#		print("A copy of the installer will be placed in /root directory of your new system\n")
#		subprocess.call(["cp", "-R", "`pwd`", "mnt/root"])
#		input("Press Enter to continue ... ")

def main():
	ins = Installer()
	ins.SetKeyMap()
	ins.InfoTextEditor()
	
	while True:
		subprocess.call("clear")
		print("###################################################################################")
		print("#                                                                                 #")
		print("#      instALler - Installer for Arch Linux                                       #")
		print("#      This program will install Arch Linux in this computer                      #")
		print("#                                                                                 #")
		print("#      instALler is developed by https://github.com/filipe-marques                #")
		print("#      and is free software licensed under GNU GPL v.3+                           #")
		print("#                                                                                 #")
		print("###################################################################################\n")
		print("FOLLOW THIS INSTALLATION SEQUENCE IN ORDER: \n")
		print("IF YOU PREVIOUSLY DONE THE PARTITIONS WITH GPARTED YOU CAN JUMP THAT OPTION !!!\n")
		print("To be using this program, it assumed that you setup the network connection, so you can skip that option !\n")
		print("For simplicity this program installs and configure root and swap !!!\n")
		print("1 - Set Network Connection (Wired or Wireless)")
		print("2 - Set Keyboard Layout")
		print("3 - Define Partitions")
		print("4 - Create File Systems")
		print("5 - Mount Partitions")
		print("6 - Install Packages: base base-devel python")
		print("7 - Generating an Fstab File")
		print("8 - Configure the New Installed System")
		print("9 - Create Ram Disk")
		print("10 - Set Root Password")
		print("11 - Install and Configure the Bootloader\n")
		
		numberOption = input("Press number option: (to exit press e) ")
		
		if numberOption == "1":
			ins.Network()
		if numberOption == "2":
			ins.SetKeyboardLayout()
		if numberOption == "3":
			ins.Partition()
		if numberOption == "4":
			ins.CreateFileSystems()
		if numberOption == "5":
			ins.MountPartitions()
		if numberOption == "6":
			ins.SelectMirrors()
			ins.InstallBaseSystem()
		if numberOption == "7":
			ins.GeneratingFstab()
		if numberOption == "8":
			ins.ConfigureSystem()
		if numberOption == "9":
			ins.CreateRamDisk()
		if numberOption == "10":
			ins.SetRootPassword()
		if numberOption == "11":
			ins.InstallConfigureBootloader()
		if numberOption == "e":
			break
		
		# how to execute commands in arch chroot bash environment - someone test this subject !!!

if __name__ == "__main__":
	main()
