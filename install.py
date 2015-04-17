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

import subprocess, os.path

class Installer:
	def __init__(self):
		subprocess.call("clear")
		self.uefi = 0
	
	def DoBashCommand(self, bashcommand):
		subprocess.call(["arch-chroot", "/mnt", "/bin/bash", "-c", '"'+bashcommand+'"'])
	
	def CheckUefiBios(self):
		if os.path.exists("/sys/firmware/efi"):
			print("UEFI mode loaded !")
			self.uefi = 1
			subprocess.call(["efivar", "-l"])
			input("Press Enter to continue ...")
		else:
			print("BIOS mode loaded !")
			self.uefi = 0
			input("Press Enter to continue ...")
			
	def RefreshRepos(self):
		subprocess.call(["pacman", "-Sy"])
	
	'''def SetKeyMap(self):
		print("Setting KeyMap")
		print("KeyMap - https://wiki.archlinux.org/index.php/KEYMAP")
		print("The KEYMAP variable is specified in the /etc/rc.conf file.\nIt defines what keymap the keyboard is in the virtual consoles.\nKeytable files are provided by the kbd package.")
		#subprocess.call(["localectl", "list-keymaps"])
		print("localectl list-keymaps")
		keymap = input("Please enter the keymap: ")
		#subprocess.call(["loadkeys", keymap])
		print("loadkeys keymap")
		input("Press Enter to continue ...")'''
		
	def InfoTextEditor(self):
		subprocess.call("clear")
		print("Default text editor: nano text editor")
		input("Press Enter to continue installation ...")
		
	'''def Network(self):
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
			input("Press Enter to continue ...")'''
	
	def CreatePartitions(self):
		subprocess.call("clear")
		print("Option: 1 - Partition\n")
		input("Press Enter to continue to partition the disk ...")
		partition = input("Please select what is your program for partitionning: ")
		subprocess.call([partition, "/dev/sda"])
		print("/dev/sda")
		input("Press Enter to continue ... ")
	
	def CreateFileSystems(self):
		subprocess.call("clear")
		print("Option: 2 - Create File Systems\n")
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
	
	def MountPartition(self):
		subprocess.call("clear")
		print("Option: 3 - Mount Root Partition\n")
		input("Press Enter to mount the root partition ...")
		root = input("Please insert the root partition: ")
		subprocess.call(["mount", root, " /mnt"])
		input("Press Enter to continue ... ")
	
	def SelectMirrors(self):
		subprocess.call("clear")
		print("Option: 4 Step 1 - Select Mirrors\n")
		print("Selecting mirrors ...")
		print("If you want, you can make it the only mirror available by deleting all other lines,\nbut it is usually a good idea to have a few more,\nin case the first one goes offline.")
		print("If you are running x86_x64 (64 bits) iso image for your machine, next uncomment the multilib repo")
		print("Also, if you gonna install some package from AUR add this: ")
		input("Press Enter to continue ... ")
		subprocess.call(["nano","/etc/pacman.d/mirrorlist"])
		self.RefreshRepos()
		input("Press Enter to continue ... ")
	
	def InstallBaseSystem(self):
		subprocess.call("clear")
		print("Option: 4 Step 2 - Install Base System\n")
		print("Install: base , base-devel")
		input("Press Enter to continue ... ")
		subprocess.call(["pacstrap", "/mnt", "base", "base-devel"])
		print("Installed Base System !!!")
		input("Press Enter to continue ... ")
	
	def GeneratingFstab(self):
		subprocess.call("clear")
		print("Option: 5 - Generating fstab file\n")
		print("Generating an fstab file ...")
		print("Warning: The fstab file should always be checked after generating it.\nIf you encounter errors running genfstab or later in the install process, do not run genfstab again; just edit the fstab file.")
		subprocess.call(["genfstab", "-U", "-p", "/mnt", ">>", "/mnt/etc/fstab"])
		input("Check if everything went ok ... press enter")
		subprocess.call(["nano", "/mnt/etc/fstab"])
		input("Press Enter to continue ... ")
		
	def ConfigureSystem(self):
		subprocess.call("clear")
		print("Option: 6 - Configure System\n")
		print("Option: 6 Step 1 - Configure Locale")
		print("Locale - https://wiki.archlinux.org/index.php/Locale")
		print("Locales are used in Linux to define which language the user uses.\nAs the locales define the character sets being used as well, setting up the correct locale\n is especially important if the language contains non-ASCII characters.\nhttps://wiki.archlinux.org/index.php/Locale#Per_user\n")
		print("The locale specified in the LANG variable must be uncommented in /etc/locale.gen.\necho LANG=en_US.UTF-8 > /etc/locale.conf")
		input("Press Enter to continue ... ")
		self.DoBashCommand("nano /etc/locale.gen")
		input("Press Enter to continue ... ")
		print("Generating Locale: ... ")
		self.DoBashCommand("locale-gen")
		print("Setting en_US.UTF-8 as the system-wide locale allows to keep system logs in English for easier troubleshooting.\nUsers can override this setting for their environment as required.\n")
		input("Press Enter to continue ... ")		
		self.DoBashCommand("echo LANG=en_US.UTF-8 > /etc/locale.conf")
		print("echo LANG=en_US.UTF-8 > /etc/locale.conf")
		input("Press Enter to continue ... ")
		#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		subprocess.call("clear")
		print("Option: 6 Step 2 - Configure Keyboard Layout\n")
		print("If you changed the default console keyboard layout and font in the beginning of installation, you will have to edit /etc/vconsole.conf accordingly\n(create it if it does not exist) to make those changes persist in the installed system.\n Example: KEYMAP=de-latin1 FONT=lat9w-16")
		#subprocess.call(["localectl", "list-keymaps"])
		input("Press Enter to continue ... ")
		self.DoBashCommand("nano /etc/vconsole.conf")
		input("Press Enter to continue ... ")
		#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		subprocess.call("clear")
		print("Option: 6 Step 3 - Configure Time Zone\n")
		print("Available time zones and subzones can be found in the /usr/share/zoneinfo/Zone/SubZone directories.\nTo view the available zones, check the directory /usr/share/zoneinfo/")
		print("Listing: ls /usr/share/zoneinfo/")
		input("Press Enter to continue ... ")
		self.DoBashCommand("ls /usr/share/zoneinfo/")
		zone = input("Please insert your zone: ")
		self.DoBashCommand("ls /usr/share/zoneinfo/"+zone)
		input("Press Enter to continue ... ")
		subzone = input("Please insert your subzone: ")
		print("Processing: ln -s /usr/share/zoneinfo/"+zone+"/"+subzone+" /etc/localtime")
		self.DoBashCommand("ln -s /usr/share/zoneinfo/"+zone+"/"+subzone+" /etc/localtime")
		input("Press Enter to continue ... ")
		#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		subprocess.call("clear")
		print("Option: 6 Step 4 - Configure Hardware Clock\n")
		print("Hardware Clock Time - https://wiki.archlinux.org/index.php/Internationalization")
		print("Set the hardware clock mode uniformly between your operating systems.\nOtherwise, they may overwrite the hardware clock and cause time shifts.\n")
		print("It is recommended UTC, however, localtime is discouraged used by default in Windows:\nWarning: Using localtime may lead to several known and unfixable bugs.\nHowever, there are no plans to drop support for localtime.\n")
		opt = input("Please insert your option: (1 - UTC) (2 - LocalTime) ")
		if opt == "1":
			self.DoBashCommand("hwclock --systohc --utc")
			print("Chosed option: UTC")
		if opt == "2":
			self.DoBashCommand("hwclock --systohc --localtime")
			print("Chosed option: LocalTime")
		input("Press Enter to continue ... ")
		#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		subprocess.call("clear")
		print("Option: 6 Step 5 - Configure HostName\n")
		hostname = input("Please insert a name for your hostname: ")
		self.DoBashCommand("echo "+hostname+" > /etc/hostname")
		print("Add the same hostname to /etc/hosts: \n")
		print('''\
			#/etc/hosts: static lookup table for host names
			#
			#<ip-address> <hostname.domain.org> <hostname>
			127.0.0.1 localhost.localdomain localhost myhostname	
			::1 localhost.localdomain localhost myhostname
			# End of file\n''')
		input("Press Enter to continue ... ")
		self.DoBashCommand("nano /etc/hosts")
		input("Press Enter to continue ... ")
		#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		subprocess.call("clear")
		print("Option: 6 Step 6 - Configure Network\n")
		print("Checking wired network: ...\n")
		self.DoBashCommand("ip link")
		wired2 = input("Please insert the wired interface: ")
		self.DoBashCommand("systemctl enable dhcpcd@"+wired2+".service")
		input("Press Enter to continue ... ")
		
		print("Installing wireless packages: ... iw wpa_supplicant dialog wpa_actiond wireless_tools\n")
		input("Press Enter to continue ... ")
		self.DoBashCommand("pacman -S iw wpa_supplicant dialog wpa_actiond wireless_tools")
		print("Installed packages !!!\n")
		print("You gonna need to enable the wireless service")
		input("Press Enter to continue ... ")
		subprocess.call(["iw", "dev"])
		wireless2 = input("Please insert the name of wireless interface: ")
		self.DoBashCommand("systemctl enable netctl-auto@"+wireless2+".service")
		input("Press Enter to continue ... ")
		
		subprocess.call("clear")
		print("Option: 6 Step 7 - Install others packages ...\n")
		print("Installing: Python 3")
		self.DoBashCommand("pacman -S python")
		input("Press Enter to continue ... ")
	
	def CreateRamDisk(self):
		subprocess.call("clear")
		print("Option: 7 - Create Initial Ram Disk Environment")
		self.DoBashCommand("mkinitcpio -p linux")
		input("Press Enter to continue ... ")
		
	def SetRootPassword(self):
		subprocess.call("clear")
		print("Option: 8 - Set the Root Password\n")
		print("Please insert your root password: ")
		self.DoBashCommand("passwd")
		input("Press Enter to continue ... ")
		
	def InstallConfigureBootloader(self):
		subprocess.call("clear")
		print("Option: 9 - Install and Configure the Bootloader\n")
		if self.uefi:
			print("Installing grub and os-prober ... for UEFI")
			#self.DoBashCommand("pacman -S grub os-prober")
		else:
			print("Installing grub and os-prober ... for MBR")
			self.DoBashCommand("pacman -S grub os-prober lsb-release")
			self.DoBashCommand("grub-install --target=i386-pc --recheck /dev/sda")
			self.DoBashCommand("grub-mkconfig -o /boot/grub/grub.cfg")
		input("Press Enter to continue ... ")
	
	def UnmountPartitions(self):
		subprocess.call("clear")
		print("Unmount the partitions")
		self.DoBashCommand("exit")
		subprocess.call(["umount", "-R", "/mnt"])
		input("Press Enter to continue ... ")
	
	def Finish(self):
		print("A copy of the installer will be placed in /root directory of your new system\n")
		subprocess.call(["cp", "-R", "`pwd`", "mnt/root"])
		print("Done copying !")
		print("You can now reboot !!!")
		input("Press Enter to continue ... ")

def main():
	ins = Installer()
	ins.InfoTextEditor()
	ins.CheckUefiBios()
	ins.RefreshRepos()
	
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
		print("IF YOU PREVIOUSLY DONE THE PARTITIONS WITH GPARTED YOU CAN JUMP THAT OPTION !!!\n")
		print("To be using this program, it assumed that you setup the network connection and are in root mode !\n")
		print("For simplicity this program installs and configure root and swap !!!\n")
		print("1 - Create Partitions")
		print("2 - Create File Systems")
		print("3 - Mount Root Partition")
		print("4 - Install: base base-devel")
		print("5 - Generating an fstab file")
		print("6 - Configure the New Installed System")
		print("7 - Create Init Ram Disk")
		print("8 - Set Root Password")
		print("9 - Install and Configure the Bootloader\n")
		
		print("to exit press 'e' and then 'enter'")
		print("to finish press 'd' and then 'enter'\n")
		
		Option = input("Press number option: ")
		
		if Option == "1":
			ins.CreatePartitions()
		if Option == "2":
			ins.CreateFileSystems()
		if Option == "3":
			ins.MountPartition()
		if Option == "4":
			ins.SelectMirrors()
			ins.InstallBaseSystem()
		if Option == "5":
			ins.GeneratingFstab()
		if Option == "6":
			ins.ConfigureSystem()
		if Option == "7":
			ins.CreateRamDisk()
		if Option == "8":
			ins.SetRootPassword()
		if Option == "9":
			ins.InstallConfigureBootloader()
		if Option == "d":
			ins.UnmountPartitions()
			ins.Finish()
		if Option == "e":
			break

if __name__ == "__main__":
	main()
