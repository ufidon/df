# its452 lectures
course materials and references for its452 lectures

## Module00: Build environments for computer forensics
* [Popular Computer Forensics Top 21 Tools](https://resources.infosecinstitute.com/computer-forensics-tools)
* [Kali Linux](https://www.kali.org)
* [CAINE Linux](https://www.caine-live.net)
* [Parrot Linux](https://parrotlinux.org/)



## Module01: A complete forensic process with open-source forensics tools

Guided study through a complete forensic process with open-source forensics tools:

1. [Linux and disk forensics](https://resources.infosecinstitute.com/linux-and-disk-forensics/)

2. [Disk images]( http://dftt.sourceforge.net/)


## Module02: Disk, partition & volume
1. [Data storage](https://en.wikipedia.org/wiki/Data_storage)
2. [Computer data storage](https://en.wikipedia.org/wiki/Computer_data_storage)
3. [Hard disk drive](https://en.wikipedia.org/wiki/Hard_disk_drive)
4. [Cylinder-head-sector](https://en.wikipedia.org/wiki/Cylinder-head-sector)
5. [Disk partitioning](https://en.wikipedia.org/wiki/Disk_partitioning)
5. [Logical volume management](https://en.wikipedia.org/wiki/Logical_volume_management)
6. [Master boot record](https://en.wikipedia.org/wiki/Master_boot_record)
7. [GUID Partition Table](https://en.wikipedia.org/wiki/GUID_Partition_Table)
6. [Unified Extensible Firmware Interface](https://uefi.org/)

## Module03: File system
### Windows file system: FAT & NTFS
Concepts

6. [File system](https://en.wikipedia.org/wiki/File_system)
7. [Comparison of file systems](https://en.wikipedia.org/wiki/Comparison_of_file_systems)
8. [File Allocation Table](https://en.wikipedia.org/wiki/File_Allocation_Table)
9. [FAT](https://www.forensicswiki.org/wiki/FAT)
10. [Manual Analysis of the FAT12 File System](http://alexander.khleuven.be/courses/bs1/fat12/fat12.html)
10. [OSDEV FAT](https://wiki.osdev.org/FAT)
11. [Understanding FAT32 Filesystems](https://www.pjrc.com/tech/8051/ide/fat32.html)
12. [Windows File system info](https://www.ntfs.com/index.html)
13. [An overview of FAT12](http://www.disc.ua.es/~gil/FAT12Description.pdf)
3. [Microsoft FAT Specification, August 30 2005](http://read.pudn.com/downloads77/ebook/294884/FAT32%20Spec%20%28SDA%20Contribution%29.pdf)
4. [Microsoft Extensible Firmware Initiative FAT32 File System Specification](https://staff.washington.edu/dittrich/misc/fatgen103.pdf)
6. [Data recovery](https://en.wikipedia.org/wiki/Data_recovery)
7. [Microsoft NTFS](https://docs.microsoft.com/en-us/windows-server/storage/file-server/ntfs-overview)
8. [MS Local File Systems](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/legacy/aa364407\(v%3Dvs.85\))
8. [MSDN File System Functionality Comparison](https://docs.microsoft.com/en-us/windows/win32/fileio/filesystem-functionality-comparison)
9. [NTFS Documentation](http://dubeyko.com/development/FileSystems/NTFS/ntfsdoc.pdf)
10. [Open Source: NTFS-3G](https://www.tuxera.com/community/open-source-ntfs-3g/)
11. [FAT32 vs. NTFS ](http://www.campus64.com/digital_learning/data/cyber_forensics_essentials/info_fat32-ntfs.pdf)
12. [File System Forensics FAT and NTFS](http://topdownbook.com/uploads/1/0/8/4/108471219/filesystemforensics.pdf)
13. [NTFS file system intro](http://itc.upt.al/_opsys/ntfs%20file%20system.pdf)
14. [MSDN Local File System](https://docs.microsoft.com/en-us/windows/win32/fileio/file-systems)

Tools
1. [fatback](https://github.com/gaul/fatback)


### Linux file system: Ext2/3/4
0. [Ext2 on Wikipedia](https://en.wikipedia.org/wiki/Ext2)
1. [Ext3 on Wikipedia](https://en.wikipedia.org/wiki/Ext3)
2. [Ext4 on Wikipedia](https://en.wikipedia.org/wiki/Ext4)
1. [Ext2: Second Extended Filesystem (ext2fs) ](https://wiki.osdev.org/Ext2)
2. [The Second Extended File System](https://www.nongnu.org/ext2-doc/ext2.html)
2. [ext4 Data Structures and Algorithms](https://www.kernel.org/doc/html/latest/filesystems/ext4/index.html)

### Encrypted disks
1. [Mount a FileVault Drive Encrypted (FVDE) volume](https://github.com/libyal/libfvde/wiki/Mounting)
2. [Open Bitlocker Drive on Linux](https://www.ceos3c.com/open-source/open-bitlocker-drive-linux/)
3. [How To Mount BitLocker-Encrypted Windows Partitions On Linux](https://www.linuxuprising.com/2019/04/how-to-mount-bitlocker-encrypted.html)

## Module04: Windows Registry
* Concepts
  * [Windows registry on Wikipedia](https://en.wikipedia.org/wiki/Windows_Registry)
  * [Windows registry on MSDN](https://docs.microsoft.com/en-us/windows/win32/sysinfo/registry)
  * [The Internal Structure of the Windows Registry](http://amnesia.gtisc.gatech.edu/~moyix/suzibandit.ltd.uk/MSc/)
* Tools
  * [Windows Sysinternals](https://docs.microsoft.com/en-us/sysinternals/)
    * [Regmon](https://docs.microsoft.com/en-us/sysinternals/downloads/regmon)
    * [Autoruns](https://docs.microsoft.com/en-us/sysinternals/downloads/autoruns)
    * [RegDelNull](https://docs.microsoft.com/en-us/sysinternals/downloads/regdelnull)
    * [Registry Usage](https://docs.microsoft.com/en-us/sysinternals/downloads/ru)
    * [RegJump](https://docs.microsoft.com/en-us/sysinternals/downloads/regjump)
  * [Registry editor](https://wiki.winehq.org/Regedit)
  * [Windows Registry Tools on NirSoft](https://www.nirsoft.net/windows_registry_tools.html)
  * [Autopsy 3rd Party Modules: Windows Registry Ingest Module](https://wiki.sleuthkit.org/index.php?title=Autopsy_3rd_Party_Modules)
  * [regslack](https://github.com/keydet89/Tools/blob/master/source/regslack.pl)
  * [RegRipper](https://github.com/keydet89/RegRipper2.8)
  * [Parse::Win32Registry](https://metacpan.org/pod/Parse::Win32Registry)
* Tips
  * [Windows 10 Registry Tweaks](https://technicalustad.com/a-complete-guide-to-windows-10-registry-tweaks/)
  * [Collection of Windows 10 Hidden Secret Registry Tweaks](https://www.askvg.com/collection-of-windows-10-hidden-secret-registry-tweaks/)
  * [Best Windows 10 Registry Hacks to Optimize Your PC](https://blogs.systweak.com/best-windows-10-registry-hacks-to-optimize-your-pc/)
  * [The 50 Best Registry Hacks that Make Windows Better](https://www.howtogeek.com/howto/37920/the-50-best-registry-hacks-that-make-windows-better/)
  * [Windows registry information for advanced users](https://support.microsoft.com/en-us/help/256986/windows-registry-information-for-advanced-users)
  * [Complete Windows Registry Information](http://www.woodsmall.com/registry.htm)
* USB Devices
  * [USB Device Registry Entries](https://docs.microsoft.com/en-us/windows-hardware/drivers/usbcon/usb-device-specific-registry-settings)
  * [USBDeview](https://www.nirsoft.net/utils/usb_devices_view.html)
  * [USB Device Tree Viewer](https://www.uwe-sieber.de/usbtreeview_e.html)
  * [USBView](https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/usbview)
  * [USB Storage Device Forensics for Windows 10](https://www.researchgate.net/publication/318514858_USB_Storage_Device_Forensics_for_Windows_10)

* WiFi
  * [WiFi Related Registry Keys](http://www.iccyber.org/2009/uploads/trabalhos/20090925/RCMP_Eric_Rowe.pdf)
  * [Wireless Networks and the Windows Registry - Just where has your computer been?](https://www.sans.org/reading-room/whitepapers/forensics/wireless-networks-windows-registry-computer-been-33659)
  * [How to manually delete WiFi Network Profile in Windows 10/8.1](https://www.thewindowsclub.com/delete-wifi-network-profile-windows)
  * [How to Delete Wireless Network Profiles in Windows 10 / 8 / 7](https://www.top-password.com/blog/delete-wireless-network-profiles-in-windows/)
  * [Find the Wireless Security Information (e.g., SSID, Network key, etc.) for Windows](https://support.brother.com/g/b/faqend.aspx?c=us&lang=en&prod=rj4250wbeus&faqid=faqp00100049_000)
  * [WifiInfoView](https://www.nirsoft.net/utils/wifi_information_view.html)

* Cleaner
  * [Little Registry Cleaner](https://sourceforge.net/projects/littlecleaner/)
  * [BleachBit - Clean Your System and Free Disk Space](https://www.bleachbit.org/)

## Module05: Recovery and steganography
1. Data recovery
  * [Data recovery on Wikipedia](https://en.wikipedia.org/wiki/Data_recovery)
  * [File carving on Wikipedia](https://en.wikipedia.org/wiki/File_carving)
  * [Data Recovery on Ubuntu help](https://help.ubuntu.com/community/DataRecovery)
  * [Data Recovery on ArchLinux wiki](https://wiki.archlinux.org/index.php/File_recovery)
  * [bulk extractor on Github](https://github.com/simsong/bulk_extractor)
  * [bulk extractor on Digitalcorpora](http://downloads.digitalcorpora.org/downloads/bulk_extractor/)
  * [bulk_extractor 1.5 overview bySimson L. Garfinkel](http://downloads.digitalcorpora.org/downloads/bulk_extractor/2014-07-17_BE15.pdf)
  
2. Password recovery
  * [Password cracking on Wikipedia](https://en.wikipedia.org/wiki/Password_cracking)
  * [Cryptanalysis on Wikipedia](https://en.wikipedia.org/wiki/Cryptanalysis)
  * [Security Account Manager on Wikipedia](https://en.wikipedia.org/wiki/Security_Account_Manager)
  * [Proj 10: Reset Windows Password from Samclass](https://samsclass.info/123/proj14/123p10winpass.htm)
  * [Cain and Abel \(software\) on Wikipedia](https://en.wikipedia.org/wiki/Cain_and_Abel_\(software\))
  * [Hashcat on Wikipedia](https://en.wikipedia.org/wiki/Hashcat)
  * [Project 12: Cracking Windows Password Hashes with Hashcat on Samclass](https://samsclass.info/123/proj14/123p12winhash.htm)
  * [Ubuntu security](https://help.ubuntu.com/community/CategorySecurity)
3. Steganography
  * [Steganography on Wikipedia](https://en.wikipedia.org/wiki/Steganography)
  * [stego-toolkit collected by Dominic](https://github.com/DominicBreuker/stego-toolkit)



## Module06: Operating systems
### Windows
Concepts
0. Windows operating systems
  * [Microsoft Windows](https://en.wikipedia.org/wiki/Microsoft\_Windows)

1. Event logs
  * [List of Microsoft Windows components](https://en.wikipedia.org/wiki/List_of_Microsoft_Windows_components)
  * [Microsoft Management Console](https://en.wikipedia.org/wiki/Microsoft_Management_Console)
  * [Windows Event Log](https://docs.microsoft.com/en-us/windows/win32/eventlog/event-logging)
  * [Windows Event Viewer Log (EVT) format](https://github.com/libyal/libevt/blob/master/documentation/Windows%20Event%20Log%20\(EVT\)%20format.asciidoc)
  * [EVTX and Windows EventLogging](https://www.sans.org/reading-room/whitepapers/logging/evtx-windows-event-logging-32949)


2. Prefetched files
  * [Prefetching](https://en.wikipedia.org/wiki/Prefetching)
  * [Windows prefetcher](https://en.wikipedia.org/wiki/Prefetcher)
  * [prefetch folder](https://searchenterprisedesktop.techtarget.com/definition/prefetch-folder-PF)
  * [Prefetch Forensics](https://infosecuritygeek.com/prefetch-forensics/)
  * [Windows 10, 8 & 7: Enable or Disable Superfetch](https://www.technipages.com/windows-enable-disable-superfetch)

3. Shortcut files
  * [File Shortcut ](https://en.wikipedia.org/wiki/Shortcut_\(computing\))
  * [Windows Shortcut File format specification on Github](https://github.com/libyal/liblnk/blob/master/documentation/Windows%20Shortcut%20File%20\(LNK\)%20format.asciidoc)
  * [Windows Shortcut File format specification on DFIR](https://www.dfir.training/windows/lnk/116-windows-shortcut-file-lnk-format/file)
  * [The meaning of linkfile in forensic examinations](http://computerforensics.parsonage.co.uk/downloads/TheMeaningofLIFE.pdf)

3. Jump lists
  * [Adding items to a Jump List dynamically](https://msdn.microsoft.com/en-us/ie/gg491724\(v=vs.94\))
  * [JumpList Class](https://docs.microsoft.com/en-us/dotnet/api/system.windows.shell.jumplist?view=netframework-4.8)
  * [Create, Edit, Clear or Disable Jump Lists in Windows](https://www.raymond.cc/blog/clear-and-disable-jump-lists-in-windows-7/)
  * [Windows 10 Jump List Forensics](https://www.blackbagtech.com/blog/windows-10-jump-list-forensics/)

4. Windows executables
  * [Portable Executable](https://en.wikipedia.org/wiki/Portable_Executable)
  * [PE Format](https://docs.microsoft.com/en-us/windows/win32/debug/pe-format)
  * [Common Object File Format](https://en.wikipedia.org/wiki/COFF)
  * [Comparison of executable file formats](https://en.wikipedia.org/wiki/Comparison_of_executable_file_formats)
  * [UPX](https://en.wikipedia.org/wiki/UPX)

5. System Restore Points
  * [System restore](https://en.wikipedia.org/wiki/System_Restore)
  * [Windows Preinstallation Environment](https://en.wikipedia.org/wiki/Windows_Preinstallation_Environment)
  * [Restore Point Forensics](https://www.stevebunting.org/udpd4n6/forensics/restorepoints.htm)
  * [Forensic Analysis of System Restore Points in Microsoft Windows XP](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.84.4474&rep=rep1&type=pdf)

6. File trash
  * [Trash (computing)](https://en.wikipedia.org/wiki/Trash\_\(computing\))
  * [File Explorer](https://en.wikipedia.org/wiki/File\_Explorer)
  * [System.Shell.RecycleBin object](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/sidebar/system-shell-recyclebin)
  * [Examining the Windows 10 Recycle Bin](https://www.blackbagtech.com/blog/examining-the-windows-10-recycle-bin/)
  * [Undelete and the Recycle Bin in Windows](https://www.ccleaner.com/docs/recuva/technical-information/undelete-and-the-recycle-bin-in-windows)
  * [Where is the Windows 10 recycle bin?](https://www.techspot.com/guides/1640-windows-recycle-bin/)
  * [Files Sent to The Recycle Bin: How to View, Restore or Delete Them Permanently](https://hetmanrecovery.com/recovery_news/where-to-store-how-to-view-and-find-deleted-files-in-the-recycle-bin.htm)
  * [Windows Forensics: analysis of Recycle bin artifacts](https://www.andreafortuna.org/2019/09/26/windows-forensics-analysis-of-recycle-bin-artifacts/)

7. Printer track
  * [Print Spooler](https://docs.microsoft.com/en-us/windows/win32/printdocs/print-spooler)
  * [Clear Print Queue In Windows 10, 8, 7](https://www.techsupportall.com/solved-how-to-clean-printer-spool-queue-clean-print-spool-fixit/)
  * [Documents and Printing](https://docs.microsoft.com/en-us/windows/win32/printdocs/documents-and-printing)
  * [Printer driver design guide](https://docs.microsoft.com/en-us/windows-hardware/drivers/print/)
  * [How to Fix a Print Spooler](https://www.wikihow.com/Fix-a-Print-Spooler)

Tools
* [Evtx Explorer/EvtxECmd](https://ericzimmerman.github.io/#!index.md)
* [Windows Event Log Viewer](https://tzworks.net/prototype_page.php?proto_id=4)
* [MyEventViewer ](https://www.nirsoft.net/utils/my_event_viewer.html)
* [WinPrefetchView](https://www.nirsoft.net/utils/win_prefetch_view.html)
* [ShortcutsMan](https://www.nirsoft.net/utils/shman.html)
* [JumpListsView](https://www.nirsoft.net/utils/jump_lists_view.html)
* [JumpLister](https://github.com/woanware/JumpLister)
* [Rifiuti2 - Windows Recycle Bin Analysis Tool](https://abelcheung.github.io/rifiuti2/)
* [SPL - Windows Spool File Format](https://www.undocprint.org/formats/winspool/spl)
* [Five PE Analysis Tools Worth Looking At](https://blog.malwarebytes.com/threat-analysis/2014/05/five-pe-analysis-tools-worth-looking-at/)
* [PE Tools](https://petoolse.github.io/petools/)
* [pev the PE file analysis toolkit](http://pev.sourceforge.net/)
* [PEframe](https://github.com/guelfoweb/peframe)
* [DLL Export Viewer](https://www.nirsoft.net/utils/dll_export_viewer.html)
* [UPX - the Ultimate Packer for eXecutables](https://upx.github.io/)
* [ClamAV](https://www.clamav.net/)
* [yara](https://virustotal.github.io/yara/)



### MacOS


### Linux
Concepts

* _Boot_
* [Computer booting](https://en.wikipedia.org/wiki/Booting)
* [Linux startup process](https://en.wikipedia.org/wiki/Linux\_startup\_process)
* [Unified Extensible Firmware Interface](https://en.wikipedia.org/wiki/Unified\_Extensible\_Firmware\_Interface) 
* _Daemon_
* [Daemon](https://en.wikipedia.org/wiki/Daemon\_\(computing\))
* [List of Unix daemons](https://en.wikipedia.org/wiki/List\_of\_Unix\_daemons)
* [Systemd](https://en.wikipedia.org/wiki/Systemd)
* _File system layout_
* [ Filesystem Hierarchy Standard (FHS)](https://en.wikipedia.org/wiki/Filesystem\_Hierarchy\_Standard)
* [FHS specification](https://refspecs.linuxfoundation.org/fhs.shtml)
* [File system permissions](https://en.wikipedia.org/wiki/File\_system\_permissions)
* [File attribute](https://en.wikipedia.org/wiki/File\_attribute)
* [Hidden file and hidden directory](https://en.wikipedia.org/wiki/Hidden\_file\_and\_hidden\_directory)
* _Users_
* [Computer users](https://en.wikipedia.org/wiki/User\_\(computing\))
* [User identifier](https://en.wikipedia.org/wiki/User\_identifier)
* [Group identifier](https://en.wikipedia.org/wiki/Group\_identifier)
* [passwd](https://en.wikipedia.org/wiki/Passwd)
* [Understanding /etc/passwd File Format](https://www.cyberciti.biz/faq/understanding-etcpasswd-file-format/)
* [Understanding /etc/group File](https://www.cyberciti.biz/faq/understanding-etcgroup-file/)
* [Understanding /etc/shadow file](https://www.cyberciti.biz/faq/understanding-etcshadow-file/)
* [Home directory](https://en.wikipedia.org/wiki/Home\_directory)
* [Shell history](https://en.wikipedia.org/wiki/History\_\(command\))
* [Secure Shell](https://en.wikipedia.org/wiki/Secure\_Shell)
* [GNOME](https://en.wikipedia.org/wiki/GNOME)
* [About GNOME .gconf, .gnome2 etc. directories in $HOME](https://unix.stackexchange.com/questions/21086/about-gnome-gconf-gnome2-etc-directories-in-home)
* _Logs_
* [Linux Log Files](https://help.ubuntu.com/community/LinuxLogFiles)
* [Syslog](https://en.wikipedia.org/wiki/Syslog)
* _Tasks_
* [Cron How to](https://help.ubuntu.com/community/CronHowto)


Cases
* [How To Set up SSH Keys on a Linux / Unix System](https://www.cyberciti.biz/faq/how-to-set-up-ssh-keys-on-linux-unix/)
* [How to Schedule Job on Linux using Cron, Anacron and at Commands ](https://linoxide.com/linux-how-to/schedule-job-linux-commands/)

Tools
* [Text Processing](https://learnbyexample.gitbooks.io/linux-command-line/content/Text\_Processing.html)

Images
* [Linux LEO](https://linuxleo.com/)
* [Digital Corpora disk images](https://digitalcorpora.org/corpora/disk-images)

References
* [Linux man pages online](http://man7.org/linux/man-pages/)
* [Linux Forensics for non Linux folks](http://www.deer-run.com/~hal/LinuxForensicsForNon-LinuxFolks.pdf)
* [Forensic Artifacts in Modern Linux Systems](https://www.digitalforensics.ch/nikkel18.pdf)
* [Dead Linux Machines Do Tell Tales](https://www.sans.org/reading-room/whitepapers/forensics/dead-linux-machines-tales-34227)

### Android
* [Android forensics by Calpoly](https://cci.calpoly.edu/2019-digital-forensics-downloads)

### iOS


## Module07: Network
### Network traffic
Concepts
* [Open Systems Interconnection model (OSI model)](https://en.wikipedia.org/wiki/OSI\_model)
* [Internet protocol suite](https://en.wikipedia.org/wiki/Internet\_protocol\_suite)
* [Protocol Reference](https://wiki.wireshark.org/ProtocolReference)

Cases
* [Ubuntu Server Guide: Networking](https://help.ubuntu.com/lts/serverguide/networking.html)
* [Enable tcpdump for non-root users on Debian/Ubuntu](https://gist.github.com/zapstar/3d2ff4f345b43ce7918889053503ef84)
* [An introduction to using tcpdump at the Linux command line](https://opensource.com/article/18/10/introduction-tcpdump)
* [Tcpdump Examples](https://hackertarget.com/tcpdump-examples/)
* [How to install Wireshark on Ubuntu 18.04 / Ubuntu 16.04 Desktop](https://computingforgeeks.com/how-to-install-wireshark-on-ubuntu-18-04-ubuntu-16-04-desktop/)
* [Wireshark wikiuniversity](https://en.wikiversity.org/wiki/Wireshark)


Tools

* [59 Linux Networking commands and scripts](https://haydenjames.io/linux-networking-commands-scripts/)
* [Wireshark](https://www.wireshark.org/)
* [tcpdump & libpcap](https://www.tcpdump.org/)
* [Comparison of network monitoring systems](https://en.wikipedia.org/wiki/Comparison\_of\_network\_monitoring\_systems)
* [OpenNMS wikipedia](https://en.wikipedia.org/wiki/OpenNMS)

### Network devices: 
1. network adapters, switches, routers
2. clients, servers, cloud, iot


### Network applications: browsers, websites, emails, online storage, message apps 

## Module08: Live systems
### Memory


### Malware


## Module09: DFIR certifications
* [List of computer security certifications](https://en.wikipedia.org/wiki/List\_of\_computer\_security\_certifications)
  * [Michael Tu, Ph.D. Associate Professor, CISSP, CEH, ACE](https://centers.pnw.edu/cybersecurity/michael-tu/)
  * [Certified Information Systems Security Professional (CISSP) ](https://en.wikipedia.org/wiki/Certified\_Information\_Systems\_Security\_Professional)
  * [Certified Ethical Hacker (CEH)](https://en.wikipedia.org/wiki/Certified\_Ethical\_Hacker)
  * [Certified Penetration Testing Engineer](https://en.wikipedia.org/wiki/Certified\_Penetration\_Testing\_Engineer)

## Module10: Anti-forensics

### concepts
* [Anti-forensics with a small army of exploits](https://cryptome.org/0003/anti-forensics.pdf)

### Tools
* [Metasploit Anti-Forensics Project](https://resources.bishopfox.com/resources/tools/other-free-tools/mafia/)
* [Metasploit Unleashed – Free Ethical Hacking Course](https://www.offensive-security.com/metasploit-unleashed/)