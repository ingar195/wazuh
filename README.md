# Wazuh 




## How to setup Unifi syslog
<div>
    <img src="./pictures/unifi-settings.png" alt="picture" width="550"/>
</div>

* Enable the settings like shown in the picture above
* Add the following configuration under the existing `<remote>` tag in the `ossec.conf` file. Replace `allowed-ips` with the IP range of your UniFi devices:
```xml
  <remote>
    <connection>syslog</connection>
    <port>514</port>
    <protocol>udp</protocol>
    <allowed-ips>192.168.1.0/24</allowed-ips>
  </remote>
```
* Verify that you do not have any firewall rules blocking this port on the PC and the firewall
* Make sure port 514 is exposed in the docker file 
* Now you need to save and restart Wazuh and it should now send the syslog to Wazuh 


### Debugging
* To verify that you are receiving data you can set `<logall>` to yes</logall> in the global tag. <b>Remember to disable this after you are done</b>
```xml
  <global>
    <jsonout_output>yes</jsonout_output>
    <alerts_log>yes</alerts_log>
    <logall>yes</logall>
    <logall_json>no</logall_json>
    <email_notification>no</email_notification>
    <smtp_server>smtp.example.wazuh.com</smtp_server>
    <email_from>wazuh@example.wazuh.com</email_from>
    <email_to>recipient@example.wazuh.com</email_to>
    <email_maxperhour>12</email_maxperhour>
    <email_log_source>alerts.log</email_log_source>
    <agents_disconnection_time>10m</agents_disconnection_time>
    <agents_disconnection_alert_time>0</agents_disconnection_alert_time>
  </global>
```
* Now save and restart
* Then check the log `tail -f /var/ossec/logs/archives/archives.log`
    * You should see something like this (this is from a wifi ap)
    ```
        2024 Oct 18 19:36:28 WIFI_AP_NAME->192.168.x.xx Oct 18 21:36:28 WIFI_AP_NAME xxxxxxxxxxxxx,WIFI_AP_NAME-6.6.78+15404: mcad: mcad[9776]: wireless_agg_stats.log_sta_anomalies(): bssid=XX:XX:XX:XX:XX:XX radio=rai0 vap=rai1 sta=XX:XX:XX:XX:XX:XX satisfaction_now=72 anomalies=wifi_retries
        
        2024 Oct 18 19:36:29 WIFI_AP_NAME->192.168.x.xx Oct 18 21:36:29 WIFI_AP_NAME xxxxxxxxxxxxx,WIFI_AP_NAME-6.6.78+15404: stahtd: stahtd[3701]: [STA-TRACKER].stahtd_dump_event(): {"message_type":"STA_ASSOC_TRACKER","mac":"XX:XX:XX:XX:XX:XX","vap":"ra1","event_type":"soft failure","assoc_status":"0","ip_assign_type":"roamed","wpa_auth_delta":"72000","assoc_delta":"56000","auth_delta":"0","event_id":"247","auth_ts":"2054102.769340","sta_dc_reason":"sta left","disassoc_reason":"8"}
    ```
* If you are not seeing this, double check all the steps from [How to setup Unifi syslog](#how-to-setup-unifi-syslog)
