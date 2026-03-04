# Wazuh Discord integrating



## Docker
1. Enter the wazuh.manager
2. cd /var/ossec/integrations
3. Add the 2 files from this folder
4. Update the IP to your 
5. Run the commands
``` bash
chmod 750 /var/ossec/integrations/custom-discord*
chown root:wazuh /var/ossec/integrations/custom-discord*
```
5. Add it to the config in the web ui within the then save and restart
```xml
<integration>
    <name>custom-discord</name>
    <hook_url>https://discordapp.com/api/webhooks/some-url</hook_url> <!-- Replace with your discord hook URL -->
    <alert_format>json</alert_format>
    <rule_id>404,518,519,521,593</rule_id>
    <level>12</level>
  </integration>
``