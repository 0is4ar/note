# 迭代器与生成器

\[TOC\]

## 手动遍历

### 示例

> 一个文件句柄 open\('a.txt','r'\)就是一个可迭代对象

```python
def manual_iter(): 
    with open('/etc/passwd') as f: 
        try: 
            while True: 
                line = next(f) 
                print(line, end='') 
        except StopIteration: 
            pass
```

### iter后面的magic method

```text
items = [1, 2, 3]
it = iter(items) #invokes items.__iter__()
next(it) #invokes it.__next__()
```

### **iter**

```text
class Node: 
    def __init__(self, value): 
        self._value = value 
        self._children = []

    def add_child(self, node):  
        self._children.append(node) 

    def __iter__(self): 
        return iter(self._children)

root = Node(0)
child1 = Node(1)
child2 = Node(2)
则 next(root)可到child1
```

