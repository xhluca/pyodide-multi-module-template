import base64
import os
import sys
import zipfile

import js

def buff_to_str(buff):
    return js.String.fromCharCode.apply(None, js.Uint8Array.new(buff))


async def load_file(path) -> 'BytesIO':
    r = await js.fetch(path)
    buffer = await r.arrayBuffer()
    encoded = js.btoa(buff_to_str(buffer))
    decoded = base64.b64decode(encoded)

    return decoded

decoded = await load_file('/static/py.zip')

with open('py.zip', 'wb') as f:
    f.write(decoded)

with zipfile.ZipFile('py.zip', 'r') as zip_ref:
    zip_ref.extractall()

print(os.listdir())
# => ['tmp', 'home', 'dev', 'proc', 'lib', 'py.zip', 'my_project', 'main.py']

sys.path.insert(0, '.')
import my_project

print(my_project, my_project.foo)
print(my_project.foo())
print(my_project.my_module.bar())