# its452
course materials and references for its452

## Module06: Operating systems
* [Operating system](https://en.wikipedia.org/wiki/Operating_system)
  * [List of operating systems](https://en.wikipedia.org/wiki/List_of_operating_system)
  * [Comparison of operating systems](https://en.wikipedia.org/wiki/Comparison_of_operating_systems)

### Windows
**Concepts**

* Windows operating systems
  * [Microsoft Windows](https://en.wikipedia.org/wiki/Microsoft_Windows)
* Event logs
  * [List of Microsoft Windows components](https://en.wikipedia.org/wiki/List_of_Microsoft_Windows_components)
    * [Microsoft Management Console](https://en.wikipedia.org/wiki/Microsoft_Management_Console)
  * [Windows Event Log](https://docs.microsoft.com/en-us/windows/win32/eventlog/event-logging)
    * [Windows Event Viewer Log (EVT) format](https://github.com/libyal/libevt/blob/master/documentation/Windows%20Event%20Log%20\(EVT\)%20format.asciidoc)
    * [EVTX and Windows EventLogging](https://www.sans.org/reading-room/whitepapers/logging/evtx-windows-event-logging-32949)
* Prefetched files
  * [Prefetching](https://en.wikipedia.org/wiki/Prefetching)
    * [Windows prefetcher](https://en.wikipedia.org/wiki/Prefetcher)
    * [prefetch folder](https://searchenterprisedesktop.techtarget.com/definition/prefetch-folder-PF)
    * [Prefetch Forensics](https://infosecuritygeek.com/prefetch-forensics/)
    * [Windows 10, 8 & 7: Enable or Disable Superfetch](https://www.technipages.com/windows-enable-disable-superfetch)
* Shortcut files
  * [File Shortcut ](https://en.wikipedia.org/wiki/Shortcut_\(computing\))
    * [NTFS links](https://en.wikipedia.org/wiki/NTFS_links)
      * [NTFS reparse point](https://en.wikipedia.org/wiki/NTFS_reparse_point)
      * [NTFS volume mount point](https://en.wikipedia.org/wiki/NTFS_volume_mount_point)
    * [Windows Shortcut File format specification on Github](https://github.com/libyal/liblnk/blob/master/documentation/Windows%20Shortcut%20File%20\(LNK\)%20format.asciidoc)
    * [Windows Shortcut File format specification on DFIR](https://www.dfir.training/windows/lnk/116-windows-shortcut-file-lnk-format/file)
    * [The meaning of linkfile in forensic examinations](http://computerforensics.parsonage.co.uk/downloads/TheMeaningofLIFE.pdf)
* [Jump lists](https://forensicswiki.xyz/wiki/index.php?title=Jump_Lists)
  * [List of Jump List IDs](https://forensicswiki.xyz/wiki/index.php?title=List_of_Jump_List_IDs)
  * [Adding items to a Jump List dynamically](https://msdn.microsoft.com/en-us/ie/gg491724\(v=vs.94\))
    * [JumpList Class](https://docs.microsoft.com/en-us/dotnet/api/system.windows.shell.jumplist?view=netframework-4.8)
    * [Create, Edit, Clear or Disable Jump Lists in Windows](https://www.raymond.cc/blog/clear-and-disable-jump-lists-in-windows-7/)
  * [Windows 10 Jump List Forensics](https://www.blackbagtech.com/blog/windows-10-jump-list-forensics/)
* [Program installation](https://en.wikipedia.org/wiki/Installation_(computer_programs))
  * [List of installation software](https://en.wikipedia.org/wiki/List_of_installation_software)
    * [Windows Installer](https://en.wikipedia.org/wiki/Windows_Installer)
    * [App Installer](https://en.wikipedia.org/wiki/App_Installer)
    * [Pre-installed software](https://en.wikipedia.org/wiki/Pre-installed_software)
    * [Package manager](https://en.wikipedia.org/wiki/Package_manager)
      * [List of software package management systems](https://en.wikipedia.org/wiki/List_of_software_package_management_systems)
      * [Package format](https://en.wikipedia.org/wiki/Package_format)
  * [Uninstaller](https://en.wikipedia.org/wiki/Uninstaller)
  * Windows executables
    * [Portable Executable](https://en.wikipedia.org/wiki/Portable_Executable)
      * [PE Format](https://docs.microsoft.com/en-us/windows/win32/debug/pe-format)
    * [Comparison of executable file formats](https://en.wikipedia.org/wiki/Comparison_of_executable_file_formats)
      * [Common Object File Format](https://en.wikipedia.org/wiki/COFF)
    * [UPX](https://en.wikipedia.org/wiki/UPX)
      * [Executable compression](https://en.wikipedia.org/wiki/Executable_compression)
* System Restore Points
  * [System restore](https://en.wikipedia.org/wiki/System_Restore)
    * [Restore Point Forensics](https://www.stevebunting.org/udpd4n6/forensics/restorepoints.htm)
    * [Forensic Analysis of System Restore Points in Microsoft Windows XP](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.84.4474&rep=rep1&type=pdf)
  * [Windows Preinstallation Environment](https://en.wikipedia.org/wiki/Windows_Preinstallation_Environment)
* File trash
  * [Trash (computing)](https://en.wikipedia.org/wiki/Trash_\(computing\))
    * [System.Shell.RecycleBin object](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/sidebar/system-shell-recyclebin)
    * [Examining the Windows 10 Recycle Bin](https://www.blackbagtech.com/blog/examining-the-windows-10-recycle-bin/)
    * [Undelete and the Recycle Bin in Windows](https://www.ccleaner.com/docs/recuva/technical-information/undelete-and-the-recycle-bin-in-windows)
    * [Where is the Windows 10 recycle bin?](https://www.techspot.com/guides/1640-windows-recycle-bin/)
    * [Files Sent to The Recycle Bin: How to View, Restore or Delete Them Permanently](https://hetmanrecovery.com/recovery_news/where-to-store-how-to-view-and-find-deleted-files-in-the-recycle-bin.htm)
    * [Windows Forensics: analysis of Recycle bin artifacts](https://www.andreafortuna.org/2019/09/26/windows-forensics-analysis-of-recycle-bin-artifacts/)
  * [File Explorer](https://en.wikipedia.org/wiki/File_Explorer)
* Printer track
  * [Print Spooler](https://docs.microsoft.com/en-us/windows/win32/printdocs/print-spooler)
    * [Clear Print Queue In Windows 10, 8, 7](https://www.techsupportall.com/solved-how-to-clean-printer-spool-queue-clean-print-spool-fixit/)
    * [How to Fix a Print Spooler](https://www.wikihow.com/Fix-a-Print-Spooler)
  * [Documents and Printing](https://docs.microsoft.com/en-us/windows/win32/printdocs/documents-and-printing)
    * [Printer driver design guide](https://docs.microsoft.com/en-us/windows-hardware/drivers/print/)

**Tools**
  * _suite_
    * [HxD - Freeware Hex Editor and Disk Editor](https://mh-nexus.de/)
    * [Sleuthkit & Autopsy](https://www.sleuthkit.org/)
    * [Zimmerman tools](https://ericzimmerman.github.io/)
  * _event_
    * [Evtx Explorer/EvtxECmd](https://ericzimmerman.github.io/#!index.md)
    * [Windows Event Log Viewer](https://tzworks.net/prototype_page.php?proto_id=4)
    * [MyEventViewer ](https://www.nirsoft.net/utils/my_event_viewer.html)
  * _prefetch_
    * [WinPrefetchView](https://www.nirsoft.net/utils/win_prefetch_view.html)
  * _shortcut_
    * [ShortcutsMan](https://www.nirsoft.net/utils/shman.html)
  * _jumplist_
    * [JumpListsView](https://www.nirsoft.net/utils/jump_lists_view.html)
    * [JumpLister](https://github.com/woanware/JumpLister)
    * [Jump List Parser](https://tzworks.net/download_links.php)
  * _recycle bin_
    * [Rifiuti2 - Windows Recycle Bin Analysis Tool](https://abelcheung.github.io/rifiuti2/)
  * _printing_
    * [SPL - Windows Spool File Format](https://www.undocprint.org/formats/winspool/spl)
  * _PE_
    * [Five PE Analysis Tools Worth Looking At](https://blog.malwarebytes.com/threat-analysis/2014/05/five-pe-analysis-tools-worth-looking-at/)
    * [PE Tools](https://petoolse.github.io/petools/)
    * [pev the PE file analysis toolkit](http://pev.sourceforge.net/)
    * [PEframe](https://github.com/guelfoweb/peframe)
    * [DLL Export Viewer](https://www.nirsoft.net/utils/dll_export_viewer.html)
  * _archivers_
    * [7z](https://www.7-zip.org/download.html)
    * [UPX - the Ultimate Packer for eXecutables](https://upx.github.io/)
  * _network and PnP devices_
    * [UsbHistorian](https://4discovery.com/our-tools/usb-historian/)
    * [USBDview](http://www.nirsoft.net/utils/usb_devices_view.html)
    * [USBView](https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/usbview?redirectedfrom=MSDN)
  * _password cracker_
    * [ophcrack](https://ophcrack.sourceforge.io/)
  * _timestamp_
    * [Dcode](https://www.digital-detective.net/digital-forensic-software/free-tools/)
  * _antivirus_
    * [ClamAV](https://www.clamav.net/)
    * [yara](https://virustotal.github.io/yara/)
  * _app logs_
    * [SkypeLogView](http://www.nirsoft.net/utils/skype_log_view.html)



### MacOS


### Linux
**Overview**
  * [Linux Forensics for non Linux folks](http://www.deer-run.com/~hal/LinuxForensicsForNon-LinuxFolks.pdf)
  * [Forensic Artifacts in Modern Linux Systems](https://www.digitalforensics.ch/nikkel18.pdf)
  * [Dead Linux Machines Do Tell Tales](https://www.sans.org/reading-room/whitepapers/forensics/dead-linux-machines-tales-34227)
**Concepts**
* _Boot_
  * [Computer booting](https://en.wikipedia.org/wiki/Booting)
    * [Linux startup process](https://en.wikipedia.org/wiki/Linux_startup_process)
  * [Unified Extensible Firmware Interface](https://en.wikipedia.org/wiki/Unified_Extensible_Firmware_Interface) 
* _Daemon_
  * [Daemon](https://en.wikipedia.org/wiki/Daemon_\(computing\))
    * [List of Unix daemons](https://en.wikipedia.org/wiki/List_of_Unix_daemons)
    * [Systemd](https://en.wikipedia.org/wiki/Systemd)
* _File system layout_
  * [Filesystem Hierarchy Standard (FHS)](https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard)
    * [FHS specification](https://refspecs.linuxfoundation.org/fhs.shtml)
  * [File system permissions](https://en.wikipedia.org/wiki/File_system_permissions)
    * [File attribute](https://en.wikipedia.org/wiki/File_attribute)
  * [Hidden file and hidden directory](https://en.wikipedia.org/wiki/Hidden_file_and_hidden_directory)
* _Users_
  * [Computer users](https://en.wikipedia.org/wiki/User_\(computing\))
    * [User identifier](https://en.wikipedia.org/wiki/User_identifier)
    * [Group identifier](https://en.wikipedia.org/wiki/Group_identifier)
  * [passwd](https://en.wikipedia.org/wiki/Passwd)
    * [Understanding /etc/passwd File Format](https://www.cyberciti.biz/faq/understanding-etcpasswd-file-format/)
    * [Understanding /etc/group File](https://www.cyberciti.biz/faq/understanding-etcgroup-file/)
    * [Understanding /etc/shadow file](https://www.cyberciti.biz/faq/understanding-etcshadow-file/)
  * [Home directory](https://en.wikipedia.org/wiki/Home_directory)
  * [Shell history](https://en.wikipedia.org/wiki/History_\(command\))
    * [Secure Shell](https://en.wikipedia.org/wiki/Secure_Shell)
    * [How To Set up SSH Keys on a Linux / Unix System](https://www.cyberciti.biz/faq/how-to-set-up-ssh-keys-on-linux-unix/)
  * [GNOME](https://en.wikipedia.org/wiki/GNOME)
    * [About GNOME .gconf, .gnome2 etc. directories in $HOME](https://unix.stackexchange.com/questions/21086/about-gnome-gconf-gnome2-etc-directories-in-home)
* _Logs_
  * [Linux Log Files](https://help.ubuntu.com/community/LinuxLogFiles)
    * [Syslog](https://en.wikipedia.org/wiki/Syslog)
* _Tasks_
  * [Cron How to](https://help.ubuntu.com/community/CronHowto)
  * [How to Schedule Job on Linux using Cron, Anacron and at Commands ](https://linoxide.com/linux-how-to/schedule-job-linux-commands/)
**Tools**
  * [Text Processing](https://learnbyexample.gitbooks.io/linux-command-line/content/Text_Processing.html)
**Images**
  * [Linux LEO](https://linuxleo.com/)
  * [Digital Corpora disk images](https://digitalcorpora.org/corpora/disk-images)
**References**
  * [Linux man pages online](http://man7.org/linux/man-pages/)

### Mobile operating system
  * _overview_
    * [Introduction to Mobile Forensics](https://eforensicsmag.com/introduction-to-mobile-forensics/)
    * [INTRODUCTION TO MOBILE FORENSICS ppt](https://www.bucks.edu/media/bcccmedialibrary/con-ed/itacademy/IntroToMobileForensics.pdf)
    * [Android forensics by Calpoly](https://cci.calpoly.edu/2019-digital-forensics-downloads)
    * [Open Source Mobile Device Forensics](https://www.nist.gov/sites/default/files/documents/forensics/6-Mahalik_OSMF.pdf)
  * _concepts_
    * [Mobile device forensics](https://en.wikipedia.org/wiki/Mobile_device_forensics)
    * [Mobile phone](https://en.wikipedia.org/wiki/Mobile_phone)
    * [Smartphone](https://en.wikipedia.org/wiki/Smartphone)
    * [Comparison of smartphones](https://en.wikipedia.org/wiki/Comparison_of_smartphones)
    * [Mobile operating system](https://en.wikipedia.org/wiki/Mobile_operating_system)
      * [Comparison of mobile operating systems](https://en.wikipedia.org/wiki/Comparison_of_mobile_operating_systems)
    * [Wikipedia: Cellular network](https://en.wikipedia.org/wiki/Cellular_network)
    * [Wikipedia: SIM Card](https://en.wikipedia.org/wiki/SIM_card)
  * _tools_
    * [Cellebrite – UFED](https://www.cfreds.nist.gov/mobile/cellebrite/index.htm)
    * [libimobiledevice - iOS communicator](http://www.libimobiledevice.org/)
    * [Santoku](https://santoku-linux.com/)
    * [Android developers](https://developer.android.com/)
    * [3uTools](https://www.3u.com/firmwares)
    * [P2K Commander](http://www.e398mod.com/index.php?option=com_content&view=article&id=60/28)

  * _hardware_
    * [Faraday bag](https://faradaybag.com/)
    
  * _cases_
    * [SANS: Mobile Device Forensics](https://www.sans.org/reading-room/whitepapers/forensics/mobile-device-forensics-32888)
    * [Flash, Mod and Backup Your Android from Computer using UniFlash](https://www.guidingtech.com/14470/flash-mod-backup-android-computer-uniflash/)
    * [How to flash the firmware of iPhone](https://www.gearbest.com/blog/how-to/how-to-flash-the-firmware-of-iphone-3070)
    * [iMazing: Reinstall or restore iOS on a malfunctioning iPhone or iPad](https://imazing.com/guides/how-to-reinstall-or-restore-ios-on-a-malfunctioning-iphone-or-ipad)
    * [How to Flash a New ROM to Your Android Phone](https://www.xda-developers.com/how-to-install-custom-rom-android/)
    * [Manually flash Android Things](https://developer.android.com/things/hardware/fastboot)
    * [4 Ways to Flash Dead Android Phone Safely](https://drfone.wondershare.com/android-issue/flash-dead-android-phone.html)

### Embedded systems
* _overview_
* _concepts_
  * [Embedded system](https://en.wikipedia.org/wiki/Embedded_system)
  * [Real-time operating system](https://en.wikipedia.org/wiki/Real-time_operating_system)
    * [Comparison of real-time operating systems](https://en.wikipedia.org/wiki/Comparison_of_real-time_operating_systems)
* _tools_
* _cases_

### Virtualization
* [Virtualization](https://en.wikipedia.org/wiki/Virtualization)
  * [Hypervisor](https://en.wikipedia.org/wiki/Hypervisor)
  * [Comparison of platform virtualization software](https://en.wikipedia.org/wiki/Comparison_of_platform_virtualization_software)

