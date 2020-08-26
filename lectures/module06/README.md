# its452
course materials and references for its452

## Module06: Operating systems
* [Operating system](https://en.wikipedia.org/wiki/Operating\_system)
* [List of operating systems](https://en.wikipedia.org/wiki/List\_of\_operating\_system)
* [Real-time operating system](https://en.wikipedia.org/wiki/Real-time\_operating\_system)
* [Comparison of real-time operating systems](https://en.wikipedia.org/wiki/Comparison\_of\_real-time\_operating\_systems)

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

### Mobile operating system
  * _overview_
    * [Introduction to Mobile Forensics](https://eforensicsmag.com/introduction-to-mobile-forensics/)
    * [INTRODUCTION TO MOBILE FORENSICS ppt](https://www.bucks.edu/media/bcccmedialibrary/con-ed/itacademy/IntroToMobileForensics.pdf)
    * [Android forensics by Calpoly](https://cci.calpoly.edu/2019-digital-forensics-downloads)
    * [Open Source Mobile Device Forensics](https://www.nist.gov/sites/default/files/documents/forensics/6-Mahalik_OSMF.pdf)
  * _concepts_
    * [Mobile device forensics](https://en.wikipedia.org/wiki/Mobile\_device\_forensics)
    * [Mobile phone](https://en.wikipedia.org/wiki/Mobile\_phone)
    * [Smartphone](https://en.wikipedia.org/wiki/Smartphone)
    * [Comparison of smartphones](https://en.wikipedia.org/wiki/Comparison\_of\_smartphones)
    * [Mobile operating system](https://en.wikipedia.org/wiki/Mobile\_operating\_system)
    * [Wikipedia: Cellular network](https://en.wikipedia.org/wiki/Cellular\_network)
    * [Wikipedia: SIM Card](https://en.wikipedia.org/wiki/SIM\_card)
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
  * [Embedded system](https://en.wikipedia.org/wiki/Embedded\_system)
* _tools_
* _cases_
