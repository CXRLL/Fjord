# Welcome To Fjord!
An 16-Bit Virtual CPU. Comes Prepackaged with Fssembler, Fjords Assembler.

Fjords Specifications are :

<b>16 Bit Virtual Processor<b>

<b>40 General Purpose Registers<b>

<b>65536 Kilobytes of Memory<b>

<b>Tri-Core With Threading<b>

<b>A Stack Pointer for Stack Operations<b>

<b>25 Insturctions<b>


# Installation
Currently Fjord And FSSEMBLER is supported on Linux and Windows

The only way to install Fjord and FSSEMBLER right now is buliding it,
Heres how to bulid it.

## 1. Install Python

Of Course, You need to install the Python Enviorment for FSSEMBLER And Fjord to work,
You can install python on their website.

## 2. Download Git.
To bulid from source you need to download Git.

### Installation for Linux

sudo apt install git - For Debian/Ubuntu Based Distros

dnf install git - For Fedora Based Distros

pacman -S git - For Arch Based Distros

zypper install git - For SUSE Based Distros

emerge --ask --verbose dev-vcs/git - For Gentoo Based Distros

nix-env -i git - For NixOS

apk add git - For Alphine Linux

urpmi - For Mageia

### Installation for Windows

You could use the setup or (winget install --id Git.Git -e --source winget) to install Git on Windows.

## 3. Find the Source

git clone https://github.com/CXRLL/Fjord

## 4. Change Directory

cd Fjord

## 5. Run Fjord.
Run Fjord by typing in .\Fjord in the Fjord Directory (For Windows Only) or use an Python Interpreter, or add Fjord To $PATH and type in Fjord (For Linux and Windows)

