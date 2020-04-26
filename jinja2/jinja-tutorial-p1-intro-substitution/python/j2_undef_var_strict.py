from jinja2 import Template, StrictUndefined

template = "Device {{ name }} is a {{ type }} located in the {{ site }} datacenter."

data = {
    "name": "waw-rtr-core-01",
    "site": "warsaw-01",
}

j2_template = Template(template, undefined=StrictUndefined)

print(j2_template.render(data))
