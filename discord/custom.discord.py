 #!/usr/bin/env python3
import sys
import json
import requests

DASHBOARD_HOST = "10.13.0.127"

alert_file = open(sys.argv[1])
hook_url = sys.argv[3]
alert_json = json.loads(alert_file.read())
alert_file.close()

rule_desc = alert_json.get('rule', {}).get('description', 'No description')
rule_level = alert_json.get('rule', {}).get('level', 0)
rule_id = alert_json.get('rule', {}).get('id', 'N/A')
agent_name = alert_json.get('agent', {}).get('name', 'Unknown')
user = alert_json.get('data', {}).get('dstuser', alert_json.get('data', {}).get('srcuser', 'N/A'))
full_log = alert_json.get('full_log', 'No log available')
alert_id = alert_json.get('id', 'N/A')


event_link = (
    f"https://{DASHBOARD_HOST}/app/data-explorer/discover#?_a=(discover:(columns:!(_source),isDirty:!f,sort:!()),"
    f"metadata:(indexPattern:'wazuh-alerts-*',view:discover))&_g=(filters:!(),refreshInterval:(pause:!t,value:0),"
    f"time:(from:now-7d,to:now%2B1h))&_q=(filters:!(),query:(language:kuery,query:'id:\"{alert_id}\"'))"
)

color = 15158332 if rule_level >= 10 else (15105570 if rule_level >= 7 else 3447003)

payload = {
    "content": f"🔗 **View in Dashboard:** <{event_link}>",
    "embeds": [{
        "title": f"🚨 Wazuh Alert - Level {rule_level}",
        "description": f"**{rule_desc}**",
        "color": color,
        "fields": [
            {"name": "🆔 Rule ID", "value": f"`{rule_id}`", "inline": True},
            {"name": "👤 User", "value": f"`{user}`", "inline": True},
            {"name": "🖥️ Agent", "value": f"`{agent_name}`", "inline": True},
            {"name": "📜 Full Log", "value": f"```{full_log[:1000]}```", "inline": False}
        ],
        "footer": {"text": f"Event ID: {alert_id}"}
    }]
}
