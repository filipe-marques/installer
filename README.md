## instALler - Arch Linux installer

#### Copyright (C) 2015 Filipe Marques eagle.software3@gmail.com
#### Project licensed under GNU GPL v.3+

instALler is a easy installer for Arch Linux operating system.

Currently doesn't have UEFI support ! In the future my change.

This project needs your testing.

#### To execute:

In virtualbox or in a real machine: 

1. boot archlinux iso
1.1 run in root mode

2. install python3 and git

```shell
pacman -S python git
```

3. clone this repository

```shell
git clone https://www.github.com/filipe-marques/installer
```

4. execute the file install.py

```shell
python install.py
```

After install Arch Linux, login as root and execute:

```shell
python config.py
```

it will help you install desktop environments, drivers, themes, ... (currently not implemented)

### All trademarks and registered trademarks are the property of their respective owners.
