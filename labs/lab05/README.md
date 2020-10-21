# its452
course materials and references for its452

## lab05: Windows registry

**1. Objectives**

1. Get familiar with Windows registry
2. Analyze the Windows registry in the [laptop image](https://drive.google.com/file/d/1ayGZIIm91I2GS_8rNUGxc7lIOkn2CbW0/view) provided by [California Cybersecurity Institute](https://cci.calpoly.edu/2019-digital-forensics-downloads) with  autopsy and/or [Zimmerman's Registy Explorer](https://ericzimmerman.github.io).

**2. Tasks**
* Complete all tasks listed in California Cybersecurity Institute (CCI)'s digital forensics training [Chapter 4: Understanding the Registry](https://cci.calpoly.edu/2019-digital-forensics-downloads)
  * Local live system(Use your Windows or Windows server VM):
    * (10%) Use RegEditor to explore registry Subtrees, Keys, Subkeys and Values
    * (10%) Find all hive files
    * (10%) Explore user profiles and find all SIDs (Security Identifiers)
  * [CCI Offline image](https://drive.google.com/file/d/1ayGZIIm91I2GS_8rNUGxc7lIOkn2CbW0/view):
    * (10%) Find all recent activities with Autopsy
    * (10%) Export hive files from Autopsy
    * (10%) Load offline hive files into Registry Explorer
    * (10%) Find the TimeZone information in the SYSTEM hive
    * (10%) Identify all computer users using Autopsy and Registry Explorer
    * (20%) Crack user Crag's login password with OpCrack

**3. Tools**
* [autopsy](http://sleuthkit.org/autopsy/docs/user-docs/)
  * [sleuthkit](http://wiki.sleuthkit.org/index.php?title=Help_Documents)
* [Zimmerman's Registy Explorer](https://ericzimmerman.github.io)
* [Dcode](https://www.digital-detective.net/dcode/)
* [epochconverter](https://www.epochconverter.com/)

**4. References**
* [Dr. Schwarz's ppt on registry analysis](http://www.cse.scu.edu/~tschwarz/COEN252_13/PPT/Windows%20Registry%20Analysis.pptx)
* [Understanding the Registry  by Calpoly](https://cci.calpoly.edu/2019-digital-forensics-downloads)
* [cfreds-2017-winreg](https://www.cfreds.nist.gov/winreg/cfreds-2017-winreg/cfreds-2017-winreg.html)
