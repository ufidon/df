# its452
course materials and references for its452

## Module07: Network
### Network traffic
**Concepts**
  * [Open Systems Interconnection model (OSI model)](https://en.wikipedia.org/wiki/OSI_model)
    * [Internet protocol suite](https://en.wikipedia.org/wiki/Internet_protocol_suite)
      * [Transmission Control Protocol](https://en.wikipedia.org/wiki/Transmission_Control_Protocol)
        * [Lists of network protocols](https://en.wikipedia.org/wiki/Lists_of_network_protocols)
        * [List of IP protocol numbers](https://en.wikipedia.org/wiki/List_of_IP_protocol_numbers)
        * [List of TCP and UDP port numbers](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers)
    * [Protocol Reference](https://wiki.wireshark.org/ProtocolReference)
  * [Log file](https://en.wikipedia.org/wiki/Log_file)
    * [Log analysis](https://en.wikipedia.org/wiki/Log_analysis)
    * [Making better use of your Linux logs](https://www.networkworld.com/article/3313425/making-better-use-of-your-linux-logs.html)
      * [Linux Logs Explained](https://www.plesk.com/blog/featured/linux-logs-explained/)
      * [Linux Log Files Location And How Do I View Logs Files on Linux?](https://www.cyberciti.biz/faq/linux-log-files-location-and-how-do-i-view-logs-files/)
  * [Shared resource](https://en.wikipedia.org/wiki/Shared_resource)
    * [File sharing](https://en.wikipedia.org/wiki/File_sharing)
      * [Comparison of file-sharing applications](https://en.wikipedia.org/wiki/Comparison_of_file-sharing_applications)
    * [Clustered file system](https://en.wikipedia.org/wiki/Clustered_file_system)
      * [Comparison of distributed file systems](https://en.wikipedia.org/wiki/Comparison_of_distributed_file_systems)
        * [Network File System (NFS)](https://en.wikipedia.org/wiki/Network_File_System)
    * [File transfer](https://en.wikipedia.org/wiki/File_transfer)
      * [Comparison of file transfer protocols](https://en.wikipedia.org/wiki/Comparison_of_file_transfer_protocols)
    * [File synchronization](https://en.wikipedia.org/wiki/File_synchronization)
      * [Comparison of file synchronization software](https://en.wikipedia.org/wiki/Comparison_of_file_synchronization_software)
  * [Network packet](https://en.wikipedia.org/wiki/Network_packet)
    * [Protocol data unit](https://en.wikipedia.org/wiki/Protocol_data_unit)
      * [Ethernet frame](https://en.wikipedia.org/wiki/Ethernet_frame)
      * [IP fragmentation](https://en.wikipedia.org/wiki/IP_fragmentation)
  * [Packet capture appliance](https://en.wikipedia.org/wiki/Packet_capture_appliance)
    * [Network tap](https://en.wikipedia.org/wiki/Network_tap)
      * [TUN/TAP](https://en.wikipedia.org/wiki/TUN/TAP)
      * [Make a Passive Network Tap](https://www.instructables.com/Make-a-Passive-Network-Tap/)
      * [Promiscuous mode](https://en.wikipedia.org/wiki/Promiscuous_mode)
      * [Monitor mode](https://en.wikipedia.org/wiki/Monitor_mode)
    * [Pcap](https://en.wikipedia.org/wiki/Pcap)
    * [Packet analyzer](https://en.wikipedia.org/wiki/Packet_analyzer)
      * [Comparison of packet analyzers](https://en.wikipedia.org/wiki/Comparison_of_packet_analyzers)
        * [Wireshark](https://en.wikipedia.org/wiki/Wireshark)
        * [Tcpdump](https://en.wikipedia.org/wiki/Tcpdump)
    * [Berkeley Packet Filter](https://en.wikipedia.org/wiki/Berkeley_Packet_Filter)
      * [BPF](https://www.kernel.org/doc/html/latest/bpf/index.html)
      * [Wireshark CaptureFilters](https://gitlab.com/wireshark/wireshark/-/wikis/CaptureFilters)
      * [Wireshark DisplayFilters](https://gitlab.com/wireshark/wireshark/-/wikis/DisplayFilters)
  * [Transport Layer Security (TLS)](https://en.wikipedia.org/wiki/Transport_Layer_Security)
    * [Datagram Transport Layer Security (DTLS)](https://en.wikipedia.org/wiki/Datagram_Transport_Layer_Security)
    * [TLS by Wireshark](https://gitlab.com/wireshark/wireshark/-/wikis/TLS)
  * [Network monitoring](https://en.wikipedia.org/wiki/Network_monitoring)
    * [Comparison of network monitoring systems](https://en.wikipedia.org/wiki/Comparison_of_network_monitoring_systems)
      * [DShield](https://en.wikipedia.org/wiki/DShield)
      * [ShieldsUP](https://en.wikipedia.org/wiki/ShieldsUP)

**Cases**
  * [Ubuntu Server Guide: Networking](https://help.ubuntu.com/lts/serverguide/networking.html)
    * [59 Linux Networking commands and scripts](https://haydenjames.io/linux-networking-commands-scripts/)
  * [Enable tcpdump for non-root users on Debian/Ubuntu](https://gist.github.com/zapstar/3d2ff4f345b43ce7918889053503ef84)
    * [An introduction to using tcpdump at the Linux command line](https://opensource.com/article/18/10/introduction-tcpdump)
    * [Tcpdump Examples](https://hackertarget.com/tcpdump-examples/)
  * [windump](https://www.winpcap.org/windump/)
    * [winpcap](https://www.winpcap.org)
  * [How to install Wireshark on Ubuntu 18.04 / Ubuntu 16.04 Desktop](https://computingforgeeks.com/how-to-install-wireshark-on-ubuntu-18-04-ubuntu-16-04-desktop/)
    * [Wireshark wikiuniversity](https://en.wikiversity.org/wiki/Wireshark)
  * [How to Decrypt SSL with Wireshark – HTTPS Decryption Guide](https://www.comparitech.com/net-admin/decrypt-ssl-with-wireshark/)
    * [Wireshark Tutorial: Decrypting HTTPS Traffic](https://unit42.paloaltonetworks.com/wireshark-tutorial-decrypting-https-traffic/)
    * [Wireshark and SSL/TLS Master Secrets](https://docs.mitmproxy.org/stable/howto-wireshark-tls/)
      * [mitmproxy is a free and open source interactive HTTPS proxy](https://mitmproxy.org/)
        * [code](https://github.com/mitmproxy/mitmproxy)

### Network applications: browsers, websites, emails, online storage, message apps 
* **Browsers**
  * _overview_
    * [AN OVERVIEW OF WEB BROWSER FORENSICS](https://www.digitalforensics.com/blog/an-overview-of-web-browser-forensics/)
  *  _concepts_
    * [Web browser](https://en.wikipedia.org/wiki/Web_browser) 
    * [List of web browsers](https://en.wikipedia.org/wiki/List_of_web_browsers)
    * [Comparison of web browsers](https://en.wikipedia.org/wiki/Comparison_of_web_browsers)
    * [Browser extension](https://en.wikipedia.org/wiki/Browser_extension)
    * [Bookmark (digital)](https://en.wikipedia.org/wiki/Bookmark_\(digital\))
    * [HTTP cookie](https://en.wikipedia.org/wiki/HTTP_cookie)
    * [Web storage](https://en.wikipedia.org/wiki/Web_storage)
    * [Web browsing history](https://en.wikipedia.org/wiki/Web_browsing_history)
    * [Wikipedia:Database download](https://en.wikipedia.org/wiki/Wikipedia:Database_download)
    * [Firefox](https://en.wikipedia.org/wiki/Firefox)
    * [Google Chrome](https://en.wikipedia.org/wiki/Google_Chrome)
    * [Microsoft Edge](https://en.wikipedia.org/wiki/Microsoft_Edge)
    * [Internet Explorer](https://en.wikipedia.org/wiki/Internet_Explorer)
    * [SQLite](https://en.wikipedia.org/wiki/SQLite)
  * _tools_
    * [Web Artifact Analysis in Autopsy](https://www.sleuthkit.org/autopsy/web_artifacts.php)
    * [pasco](http://manpages.ubuntu.com/manpages/bionic/en/man1/pasco.1.html)
    * [msiecfinfo](http://manpages.ubuntu.com/manpages/bionic/man1/msiecfinfo.1.html)
    * [msiecfexport](http://manpages.ubuntu.com/manpages/bionic/en/man1/msiecfexport.1.html)
    * [Win32::UrlCache](https://metacpan.org/pod/Win32::UrlCache)
    * [SQLiteStudio](https://sqlitestudio.pl/index.rvt)
    * [DB Browser for SQLite](https://sqlitebrowser.org/)
    * [GNUstep](https://en.wikipedia.org/wiki/GNUstep)
  * _cases_
    * [Change the Default Location for Saving Internet Explorer Favorites](https://www.howtogeek.com/115412/change-the-default-location-for-saving-internet-explorer-favorites/)
  
  
* **eMails**
  * _overview_
    * [Email Forensics](https://fenix.tecnico.ulisboa.pt/downloadFile/1970943312267438/csf-13.pdf)
  * _concepts_
    * [Email on Wikipedia](https://en.wikipedia.org/wiki/Email)
    * [Comparison of email clients](https://en.wikipedia.org/wiki/Comparison_of_email_clients)
    * [Personal Storage Table](https://en.wikipedia.org/wiki/Personal_Storage_Table)
    * [Outlook Personal Folders (.pst) File Format](https://docs.microsoft.com/en-us/openspecs/office_file_formats/ms-pst/141923d5-15ab-4ef1-a524-6dce75aae546)
    * [Mbox](https://en.wikipedia.org/wiki/Mbox)
    * [Maildir](https://en.wikipedia.org/wiki/Maildir)
  * _tools_
    * [pst2gmail](https://github.com/yiqideren/pst2gmail)
    * [libpff](https://github.com/libyal/libpff)
    * [pffinfo](http://manpages.ubuntu.com/manpages/bionic/man1/pffinfo.1.html)
    * [pffexport](http://manpages.ubuntu.com/manpages/bionic/man1/pffexport.1.html)
    * [grepmail](http://manpages.ubuntu.com/manpages/bionic/man1/grepmail.1p.html)
    * [mairix ](http://manpages.ubuntu.com/manpages/bionic/en/man1/mairix.1.html)

* **Online (Cloud) storage**
  * _overview_
    * [CLOUD STORAGE FORENSICS - ppt](https://digital-forensics.sans.org/summit-archives/Prague_Summit/Cloud_Storage_Forensics_Mattia_Eppifani.pdf)
    * [Cloud Storage Forensics - book](https://www.sciencedirect.com/book/9780124199705/cloud-storage-forensics/)
  * _concepts_
    * [Cloud storage](https://en.wikipedia.org/wiki/Cloud_storage)
    * [Comparison of online backup services](https://en.wikipedia.org/wiki/Comparison_of_online_backup_services)
    * [File sharing](https://en.wikipedia.org/wiki/File_sharing)
    * [Comparison of file-sharing applications](https://en.wikipedia.org/wiki/Comparison_of_file-sharing_applications)
    * [File hosting service](https://en.wikipedia.org/wiki/File_hosting_service)
  * _tools_
  * _cases_


* **Message Apps**
  * _overview_
  * _concepts_
    * [Messaging apps](https://en.wikipedia.org/wiki/Messaging_apps)
    * [Instant messaging](https://en.wikipedia.org/wiki/Instant_messaging)
    * [Comparison of instant messaging clients](https://en.wikipedia.org/wiki/Comparison_of_instant_messaging_clients)
  * _tools_
  * _cases_

### Network devices: 
* network adapters, switches, routers
* clients, servers, cloud, iot