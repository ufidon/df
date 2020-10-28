# its452
course materials and references for its452

## lab06: Data Recovery and Steganography

**1. Task**

Complete the challenge posted on Honeynet: [scan 26](http://honeynet.onofri.org/scans/scan26/)

Read the [police report](http://honeynet.onofri.org/scans/scan26/scenario.html) before continuing.

**2. Report**

Write a report about the process you complete the tasks in the description, key screen snapshots are needed as evidences. It is suggested to organized the contents following the steps described in [this demo](http://www.sleuthkit.org/case/sotm_26/index.html):
* (5%)Identification: identify the infected system
  * Check the hashes of the archive and the image
* (5%)Image Acquisition: acquiring the disk image/partition of the infected system
  * identify image, partition and filesystem, normal access
* (40%)Data Recovery and analysis: try to recover all deleted or corrupted data from the disk image
  * image details
  * unallocated directory entries
  * file/data extraction
  * file/data carving
* (20%)Reporting: write a report about 
  * the evidences collected, 
  * tools used, 
  * techniques exploited, 
  * timeline of the evidences and 
  * reconstruct the crime scene if possible.


**(30%)3. Review questions**

The 6 questions listed in the challenge above.


1. (5%) Who is the probable supplier of drugs to Jimmy Jungle?
2. (5%) What is the mailing address of Jimmy Jungle's probable drug supplier?
3. (5%) What is the exact location in which Jimmy Jungle received the drugs?
4. (5%) Where is Jimmy Jungle currently hiding?
5. (5%) What kind of car is Jimmy Jungle driving?
6. (5%) Bonus Question: Explain the process that was performed so that there were no entries in the root directory and File Allocation Table (FAT), yet the contents of each file remained in the data area?"

**4. Demo video**
* [Data Recovery and Steganography](https://youtu.be/JNzTI1TKuEU)

**5. References:**
* [Honeynet Scan of the Month 26 with TSK](http://www.sleuthkit.org/case/sotm_26/index.html)
  * [Honeynet Scan of the Month](https://www.honeynet.org/challenges/scan-of-the-month-archive/)
* [Stegdetect on Github](https://github.com/abeluck/stegdetect)
  * [outguess](https://web.archive.org/web/20150419030527/http://www.outguess.org/)
* [invisiblesecrets trial](https://www.east-tec.com/invisiblesecrets/download/)
