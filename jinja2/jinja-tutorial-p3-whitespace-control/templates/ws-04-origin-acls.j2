{% for acl, acl_lines in access_lists.items() %}(1)
ip access-list extended {{ acl }}
  {% for line in acl_lines %}(2)
    (3){% if line.action == "remark" %}
    remark {{ line.text }}
    (4){% elif line.action == "permit" %}
    permit {{ line.src }} {{ line.dst }}
    (5){% endif %}
  {% endfor %}(6)
{% endfor %}(7)

# All ACLs have been generated