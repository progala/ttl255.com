from jinja2 import Template

template = """interface {{ interface.name }}
 description {{ interface.description }}
 ip address {{ interface.ip_address }}
 speed {{ interface.speed }}
 duplex {{ interface.duplex }}
 mtu {{ interface.mtu }}"""

data = {
    "interface": {
        "name": "GigabitEthernet1/1",
        "ip_address": "10.0.0.1/31",
        "description": "Uplink to core",
        "speed": "1000",
        "duplex": "full",
        "mtu": "9124"
    }
}

j2_template = Template(template)

print(j2_template.render(data))
