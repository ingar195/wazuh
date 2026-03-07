# Alerts i use 

```xml
<integration>
    <name>custom-discord</name>
    <hook_url></hook_url>
    <alert_format>json</alert_format>
    <level>12</level>
   <!-- Wazuh API & System Critical Errors -->
    <rule_id>404,518,519,521,593</rule_id>
    <!--
      404 Wazuh API: Critical Error event, requires immediate attention.
      506 Wazuh agent stopped.
      513 Windows malware detected.
      518 Windows Adware/Spyware application found.
      519 System Audit: Vulnerable web application found.
      521 Possible kernel level rootkit.
      Removed 533 Listened ports status (netstat) changed (new port opened or closed).
      593 Microsoft Event log cleared.
    -->

    <!-- Syslog & User Privilege Changes -->
    <rule_id>2504,2961,5139,5305,5402,5404,5405,5406,5555</rule_id>
    <!--
      2504 syslog: Illegal root login.
      2961 User added to group sudo.
      5139 General device failure.
      5305 First time (su) is executed by user.
      5402 Successful sudo to ROOT executed.
      5405 Unauthorized user attempted to use sudo.
      5555 Password changed.
    -->

    <!-- SSH and Network Security -->
    <rule_id>5701,5710,5712,5902,5763,5551</rule_id>
    <!--
      5701 sshd: Possible attack on the ssh server (or version gathering).
      5710 sshd: Authentication failure.
      5712 sshd: Brute force trying to get access to the system. Non-existent user.
      5715 sshd: Authentication success.
      5902 New user added to the system.
      5763 sshd: brute force trying to get access to the system. Authentication failed.
      5551 PAM: Multiple failed logins in a small period of time.
    -->

    <!-- Malware, Virus & Shady Behavior -->
    <rule_id>7701,7702,18108,18110,18116,18119,18125,18138,22405,22406</rule_id>
    <!--
      7701 Microsoft Antimalware informational event.
      7702 Microsoft Antimalware warning event.
      18108 Windows: Failed attempt to perform a privileged operation.
      18110 Windows: User account enabled or created.
      18116 Windows: User account locked out (multiple login errors).
      18119 Windows: First time this user logged into this system.
      18125 Windows: Remote access login failure.
      18138 Windows: Logon Failure - Account locked out.
      22405 High vulnerability.
      22406 Critical vulnerability.
    -->

    <!-- Web Authentication & Firewall -->
    <rule_id>31316,40601,60204,60115,62122,67005,67006,67007</rule_id>
    <!--
      31316 Nginx: Multiple web authentication failures.
      40601 Network scan from the same source IP.
      60204 Multiple Windows logon failures.
      60115 User account locked out (multiple login errors).
      62122 Windows Defender: Antimalware platform detected suspicious activity.
      67005 Windows Firewall With Advanced Security: Windows Defender Firewall disabled.
      67006 Windows Firewall With Advanced Security: Rule has been added to the Windows Defender Firewall exception list.
      67007 Windows Firewall With Advanced Security: Rule has been modified in the Windows Defender Firewall exception list.
    -->

    <!-- Powershell & Command Execution -->
    <rule_id>92027</rule_id>
    <!--
      92027 Powershell process spawned Powershell instance.
      92029 Powershell executed script from suspicious location.
      92032 Suspicious Windows cmd shell execution.
    -->

    <!-- Additional Security Concerns -->
    <rule_id>17101,17102,61603</rule_id>
    <!--
      17101 Successful login during non-business hours.
      17102 Successful login during weekend.
      61603 Windows admin consent prompt.
    -->

    <!-- Security Windows Defender -->
    <rule_id>62152,62100,62101,62103,62104,62123</rule_id>
    <!-- 
    
      62152 Windows Defender: Disabled realtime protection 
      62154 Windows Defender: Changes to config (tamper, etc)
      62100 Windows Defender: Malware detected.
      62101 Windows Defender: Malware action taken (quarantined, removed, etc.).
      62103 Windows Defender: Signature update failed.
      62104 Windows Defender: Engine update failed.
      62123 Windows Defender: Antimalware stopped.
      62107 Windows Defender: Exclusion added.
      62108 Windows Defender: Real-time protection enabled.
      -->


    <!-- TeamViewer -->
    <rule_id>100202</rule_id>
    <!--
      100201 Successful Teamviewer login
      100202 Failed Teamviewer login
    -->
    
    <!-- Unifi -->
    <!-- THIS IS IN DEVELOPMENT-->
    <rule_id>100060</rule_id> 
    
 

  </integration>
```