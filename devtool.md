# Nice to know commands



Get all events for rule.id
```
GET wazuh-alerts-*/_search
{
  "query": {
    "match": {
      "rule.id": "222341"
    }
  }
}

```