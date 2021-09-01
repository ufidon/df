# its452
course materials and references for its452

## proj1: Overview of a complete forensic process

**0. Warmup reading**
* [A brief digital forensics cycle by Linux and Disk Forensics](./refs/Acompleteforensicprocess.pdf)


**1. Task**

Complete the challenge posted on Honeynet: [scan 24](http://www.honeynet.onofri.org/scans/scan24/)


**2. Report**

Write a report about the process you complete the tasks in the description, key screen snapshots are needed as evidences. It is suggested to organized the contents following the steps described in [A brief digital forensics cycle by Linux and Disk Forensics](./refs/Acompleteforensicprocess.pdf):
* (5%)Identification: identify the infected system
* (5%)Image Acquisition: acquiring the disk image/partition of the infected system
* (20%)Data Recovery: try to recover all deleted or corrupted data from the disk image
* (30%)Analysis: analyze the disk image for collecting evidences
* (10%)Reporting: write a report about the evidences collected, tools used, techniques exploited, timeline of the evidences and reconstruct the crime scene if possible.

Quick way to recover corrupted files using foremost, inside the folder containing the image, open a terminal, run the following commands:

```bash
# 1. recover corrupted files
foremost -orecovers -i image

# 2. use a file manager such as caja or command tree to explore the recovered files
recovers/
├── audit.txt
├── jpg
│   └── 00000073.jpg
├── ole
│   └── 00000033.ole
└── zip
    └── 00000104.zip

# 3. use stirngs command to find the password for the zip file
strings image > allstrings.txt

# 4. use a text editor or less command check the content of allstrings.txt
# you should be able to notice a line "pw=goodtimes", so "goodtimes" is likely to be the password, try it
less allstrings.txt

```

**(30%)3. Review questions**

The 6 questions listed in the challenge above.


1. (5%) Who is Joe Jacob's supplier of marijuana and what is the address listed for the supplier?
2. (5%) What crucial data is available within the coverpage.jpg file and why is this data crucial?
3. (5%) What (if any) other high schools besides Smith Hill does Joe Jacobs frequent?
4. (5%) For each file, what processes were taken by the suspect to mask them from others?
5. (5%) What processes did you (the investigator) use to successfully examine the entire contents of each file?
6. (5%) What Microsoft program was used to create the Cover Page file. What is your proof (Proof is the key to getting this question right, not just making a guess).

**4. Demo video**
* [A complete digital forensics demo with Ubuntu forensics platform](https://youtu.be/koi7A6yW\_gI)

**5. References:**
* [The Honeynet Projects: scan 24](http://www.honeynet.onofri.org/scans/scan24/)
* [Reference demo](https://www.pcsympathy.com/2008/03/22/my-first-autopsy/)
* [A brief digital forensics cycle by Linux and Disk Forensics](https://resources.infosecinstitute.com/linux-and-disk-forensics/)

