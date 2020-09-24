# its452
course materials and references for its452

## lab03: File system overview and FAT

**1. Objectives**

1. Get familiar with FAT12/FAT16/FAT32/exFAT filesystems
2. Manually analyze a FAT12 image

**2. Tasks**
1. (5%) Create an image of size 2MB.
2. (5%) Mount the image on an loop device.
3. (5%) Format the loop device with FAT12.
4. (5%) Mount the loop device to an empty folder(mounting point) and create several folders and files inside
5. (5%) Unmount the loop device from the mounting point.
6. (25%) Open the loop device in wxHexEditor, then investigate it following [An overview of FAT12](./refs/AnoverviewofFAT12.pdf)
7. (50%) Following [MANUAL ANALYSIS OF THE FAT12 FILE SYSTEM](./refs/fat12manualanalysis.pdf), manually analyze the [image](./refs/fat12.img)
8. FYI: [images.7z](.refs/../refs/images.7z) contains a demo image generated from task 1-5 and the image for task 7.

**3. Tools**

* [dd](https://en.wikipedia.org/wiki/Dd_(Unix))
* _file split and concatenation_
  * [split](https://en.wikipedia.org/wiki/Split_(Unix))
  * [cat](https://en.wikipedia.org/wiki/Cat_(Unix))
* [wxHexEditor](https://www.wxhexeditor.org/)
  * [wxhexeditor](../../lectures/module02/wxhexeditor.md)
* [Loop device](https://en.wikipedia.org/wiki/Loop_device)
  * [losetup](https://man7.org/linux/man-pages/man8/losetup.8.html)
  * [How to use loop devices](https://blog.sleeplessbeastie.eu/2017/07/03/how-to-use-loop-devices/)
* [sleuthkit](https://www.sleuthkit.org/sleuthkit/)
  * [wiki](http://wiki.sleuthkit.org)
  * [doc](http://wiki.sleuthkit.org/index.php?title=Help_Documents)
  * [TSK Tool Overview](http://wiki.sleuthkit.org/index.php?title=TSK_Tool_Overview)
  * [Implementation doc](http://wiki.sleuthkit.org/index.php?title=Design_Documents)
  * [source code](https://github.com/sleuthkit/sleuthkit)

**4. Demo videos**

* _2020 Fall_
  * [Lab03 File System Overview And FAT Part 1(lecture)](https://youtu.be/7PdyOSGOnBw)
  * [Lab03 File System Overview And FAT Part 2(lab)](https://youtu.be/jM_mNZ35ABo)

**5.References:**
* [NTFS vs FAT vs exFAT](https://www.ntfs.com/ntfs_vs_fat.htm)
* [An overview of FAT12](./refs/AnoverviewofFAT12.pdf)
* [MANUAL ANALYSIS OF THE FAT12 FILE SYSTEM](./refs/fat12manualanalysis.pdf)
* [Microsoft FAT Specification, August 30 2005](./refs/MicrosoftFATSpecification2005.pdf)
* [Microsoft Extensible Firmware Initiative FAT32 File System Specification](./refs/msfat32filesystemspecification2000.pdf)
* [How to Use Fdisk to Manage Partitions on Linux?](https://www.howtogeek.com/106873/how-to-use-fdisk-to-manage-partitions-on-linux/)
* [how to change partition type id without formatting](https://unix.stackexchange.com/questions/508890/how-to-change-partition-type-id-without-formatting).
* [mount single partition from image of entire disk device](https://askubuntu.com/questions/69363/mount-single-partition-from-image-of-entire-disk-device)
* [creating partitioned virtual disk images](https://adayinthelifeof.nl/2011/10/11/creating-partitioned-virtual-disk-images/)
* [VBox: How to use a raw disk image file in VirtualBox](https://lira.epac.to/MyPublicWiki/VBox:%20How%20to%20use%20a%20raw%20disk%20image%20file%20in%20VirtualBox.html)


