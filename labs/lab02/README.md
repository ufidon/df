# its452
course materials and references for its452

## lab02: Disk partition

**1. Objectives**

* Practice on two popular drive partition schemes: [MBR](https://en.wikipedia.org/wiki/Master_boot_record) and [GPT](https://en.wikipedia.org/wiki/GUID_Partition_Table)
* Be able to describe MBR and GPT
* Analyze MBR and GPT manually

**2. Tasks**

1. (10%) Use dd command to create two disk images each of size 500M and filled with zero
2. (10%) Use losetup to mount these two disk images to two loop devices
3. (40%) Use GParted to partition the first image into 4 partitions. *Use MBR as the partition scheme*
   1. (20%) Unmount the image, explore the partitions with sleuthkit image file tools and volume system tools
   2. (20%) Mount the image with losetup, explore the partitions with wxHexEditor
4. (40%) Use fdisk to partition the second image into 5 partitions. *Use GPT as the partition scheme*
   1. (20%) Unmount the image, explore the partitions with sleuthkit image file tools and volume system tools
   2. (20%) Mount the image with losetup, explore the partitions with wxHexEditor

**3. Tools**

* [dd](https://en.wikipedia.org/wiki/Dd_(Unix))
* _file split and concatenation_
  * [split](https://en.wikipedia.org/wiki/Split_(Unix))
  * [cat](https://en.wikipedia.org/wiki/Cat_(Unix))
* [wxHexEditor](https://www.wxhexeditor.org/)
  * [wxhexeditor](../../lectures/module02/wxhexeditor.md)
* [fdisk](https://tldp.org/HOWTO/Partition/fdisk_partitioning.html)
* [GParted](https://en.wikipedia.org/wiki/GParted)
  * [GNOME Partition Editor](https://gparted.org/)
* [Loop device](https://en.wikipedia.org/wiki/Loop_device)
  * [losetup](https://man7.org/linux/man-pages/man8/losetup.8.html)
  * [How to use loop devices](https://blog.sleeplessbeastie.eu/2017/07/03/how-to-use-loop-devices/)
* [sleuthkit](https://www.sleuthkit.org/sleuthkit/)
  * [wiki](http://wiki.sleuthkit.org)
  * [doc](http://wiki.sleuthkit.org/index.php?title=Help_Documents)
  * [TSK Tool Overview](http://wiki.sleuthkit.org/index.php?title=TSK_Tool_Overview)
  * [Implementation doc](http://wiki.sleuthkit.org/index.php?title=Design_Documents)
  * [source code](https://github.com/sleuthkit/sleuthkit)


**References:**
* [Disk partition](https://en.wikipedia.org/wiki/Disk_partitioning)
  * [Partition Table](https://wiki.osdev.org/Partition_Table)
* [MBR](https://en.wikipedia.org/wiki/Master_boot_record)
  * [Master Boot Record (MBR)](https://wiki.osdev.org/MBR_(x86))
* [GPT](https://en.wikipedia.org/wiki/GUID_Partition_Table)
  * [GUID Partition Table](https://wiki.osdev.org/GPT)
* [Apple partition map](https://en.wikipedia.org/wiki/Apple_Partition_Map)
