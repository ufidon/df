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
8. [MS Local File Systems](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/legacy/aa364407\(v%3Dvs.85\)
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
1. Event logs
  * [List of Microsoft Windows components](https://en.wikipedia.org/wiki/List_of_Microsoft_Windows_components)
  * [Microsoft Management Console](https://en.wikipedia.org/wiki/Microsoft_Management_Console)
  * [Windows Event Log](https://docs.microsoft.com/en-us/windows/win32/eventlog/event-logging)
  * [Windows Event Viewer Log (EVT) format](https://github.com/libyal/libevt/blob/master/documentation/Windows%20Event%20Log%20\(EVT\)%20format.asciidoc)
  * [EVTX and Windows EventLogging](https://www.sans.org/reading-room/whitepapers/logging/evtx-windows-event-logging-32949)
  * [Windows forensics by Calpoly](https://cci.calpoly.edu/2019-digital-forensics-downloads)

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
4. Windows executables
  * [Portable Executable](https://en.wikipedia.org/wiki/Portable_Executable)
  * [PE Format](https://docs.microsoft.com/en-us/windows/win32/debug/pe-format)
  * [Common Object File Format](https://en.wikipedia.org/wiki/COFF)
  * [Comparison of executable file formats](https://en.wikipedia.org/wiki/Comparison_of_executable_file_formats)
  * [UPX](https://en.wikipedia.org/wiki/UPX)

Tools
* [Evtx Explorer/EvtxECmd](https://ericzimmerman.github.io/#!index.md)
* [Windows Event Log Viewer](https://tzworks.net/prototype_page.php?proto_id=4)
* [MyEventViewer ](https://www.nirsoft.net/utils/my_event_viewer.html)
* [WinPrefetchView](https://www.nirsoft.net/utils/win_prefetch_view.html)
* [ShortcutsMan](https://www.nirsoft.net/utils/shman.html)
* [Five PE Analysis Tools Worth Looking At](https://blog.malwarebytes.com/threat-analysis/2014/05/five-pe-analysis-tools-worth-looking-at/)
* [PE Tools](https://petoolse.github.io/petools/)
* [pev the PE file analysis toolkit](http://pev.sourceforge.net/)
* [PEframe](https://github.com/guelfoweb/peframe)
* [DLL Export Viewer](https://www.nirsoft.net/utils/dll_export_viewer.html)
* [UPX - the Ultimate Packer for eXecutables](https://upx.github.io/)



### MacOS


### Linux

### Android
* [Android forensics by Calpoly](https://cci.calpoly.edu/2019-digital-forensics-downloads)

### iOS


## Module07: Network
### Network traffic


### Network devices: 
1. switches, routers, network adapters
2. clients, servers, cloud, iot


### Network applications: browsers, websites, emails, online storage, message apps 

## Module08: Live systems
### Memory


### Malware


## Module09: DFIR certifications