# its452
course materials and references for its452

## proj2: Network traffic analysis

**1. Task**

This project is revised from [Rhino Hunt](https://www.cfreds.nist.gov/dfrws/Rhino_Hunt.html) used in the [DFRWS 2005 Rodeo Challenge](https://www.cfreds.nist.gov/dfrws/). You may refer to this [Rhino Hunt demo](https://makemyday.io/post/rhino-hunt-part-1/) to complete it.

**2. Report**

Write a report about the process you complete the tasks in the description, key screen snapshots are needed as evidences. It is suggested to organized the contents following the steps described in [A brief digital forensics cycle by Linux and Disk Forensics](../proj1/refs/Acompleteforensicprocesspdf):
* (2%)Identification: identify the infected system.
  * What is the system with problem?
* (2%)Image Acquisition: acquiring the disk image/partition of the infected system
  * Verify the integrity of the given small image file and three network traces.
* (18%)Data Recovery and analysis: try to recover all deleted or corrupted data from the disk image, then analyze the data for collecting evidences
* (40%)Network traffic analysis: analyze the network traces for collecting evidences
* (10%)Reporting: write a report about the evidences collected, tools used, techniques exploited, timeline of the evidences and reconstruct the crime scene if possible.

**(28%)3. Review questions**

The 7 questions (each 4%) listed in the challenge above.

1. Who gave the accused a telnet/ftp account?
2. What’s the username/password for the account?
3. What relevant file transfers appear in the network traces?
4. What happened to the hard drive in the computer?  Where is it now?
5. What happened to the USB key?
6. What is recoverable from the dd image of the USB key?
7. Is there any evidence that connects the USB key and the network traces?  If so, what?

**4. Demo video**


**5. References:**
* [Password cracking](https://en.wikipedia.org/wiki/Password_cracking)
  * [fcrackzip](http://manpages.ubuntu.com/manpages/bionic/man1/fcrackzip.1.html)
  * [cRARk](http://www.crark.net/)
  * [the hydra](https://github.com/vanhauser-thc/thc-hydra)
  * [Leaked passwords](https://wiki.skullsecurity.org/index.php?title=Passwords)
    * [List of the most common passwords](https://en.wikipedia.org/wiki/List_of_the_most_common_passwords)
* [Exporting Objects from HTTP Traffic](https://unit42.paloaltonetworks.com/using-wireshark-exporting-objects-from-a-pcap/)
  * [how to extract ftp files from wireshark packet?](https://shankaraman.wordpress.com/tag/how-to-extract-ftp-files-from-wireshark-packet/)
  * [Four ways to extract files from pcaps](https://www.rubyguides.com/2012/01/four-ways-to-extract-files-from-pcaps/)
  * [Exporting Data from Wireshark](https://www.wireshark.org/docs/wsug_html_chunked/ChIOExportSection.html)
* [List of steganography software](http://www.jjtc.com/Steganography/tools.html)
  * [Stegdetect on Github](https://github.com/abeluck/stegdetect)
    * [stegdetect](http://ftp.mirrorservice.org/sites/ftp.wiretapped.net/pub/security/steganography/stegdetect/)
  * [jphs: jphide & seek steganography tools ](https://github.com/h3xx/jphs)
    * [JPHS Win](http://linux01.gwdg.de/~alatham/stego.html)
  * [Steghide](http://steghide.sourceforge.net/)
  * [SteGUI](http://stegui.sourceforge.net/)
  * [Ubuntu outguess](http://manpages.ubuntu.com/manpages/disco/man1/outguess.1.html)
    * [Archived outguess](http://web.archive.org/web/20150415220609/http://www.outguess.org/download.php)
    * [outguess on Github](https://github.com/resurrecting-open-source-projects/outguess)
  * [3 Steps to Hide Data in an Image Using Steganography](https://www.alpinesecurity.com/blog/3-steps-to-hide-data-in-an-image-using-steganography)
* [windows equivalent for dd](https://superuser.com/questions/839502/windows-equivalent-for-dd)
  * [Win32 Disk Imager](https://sourceforge.net/projects/win32diskimager/)
  * [RawWrite for Windows](http://www.chrysocome.net/rawwrite)
  * [Rawrite32](https://www.netbsd.org/~martin/rawrite32/)