# hash_filter_test.py
import jinja2
from hash_filter import j2_hash_filter

env = jinja2.Environment()
env.filters["hash"] = j2_hash_filter

tmpl_string = """MD5 hash of '$3cr3tP44$$': {{ '$3cr3tP44$$' | hash('md5') }}"""

tmpl = env.from_string(tmpl_string)

print(tmpl.render())