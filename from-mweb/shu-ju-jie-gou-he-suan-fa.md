# 数据结构和算法

## 解压可迭代对象给多个变量

```text
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
```

```text
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
```

## 保留最后N个元素

```python
from collections import deque

def search(lines, pattern, history=5):
    previous_line=deque(maxlen=history)
    #deque初始化了一个长度为5队伍，append之后之前的就会出去
    for li in lines:
        if pattern in li:
            yield li, previous_lines
        previous_lines.append(li)

if __name__ == '__main__':
with open(r'somefile.txt') as f:
    for line, prevlines in search(f, 'python', 5):
        for pline in prevlines:
            print(pline, end='')
        print(line, end='')
        print('-'*20)
```

## 寻找最大最小的n个元素\(heapq\)

```python
import heapq
cheap = heapq.nsmallest(int n, iterable, key=lambda s:s['price'])
expensive = heapq.nlargest
```

如果n较小，使用这种方法，较多建议sorted

* 堆排序：

```python
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heapq.heapify(nums) #直接改变nums
heap.heappop(nums)
#pop出最小元素
```

### 优先级\(heapq\)

```python
def push(self, item, priority):
    heapq.heappush(self._queue, (-priority, self._index, item))
    self._index += 1

def pop(self):
return heapq.heappop(self._queue)[-1]
```

heapq.heappush写成那样的原因，是因为heap会进行大小比较:

* 两个tuple的比较\(a,b\),\(c,d\)会一次比较元素的大小\(int什么的\)，如果一样大则报错

所以有index这个参数，应为每次push的index不一样，确保不报错

## 字典映射多个值

```python
from collections import defaultdict 
d = defaultdict(list) 
d['a'].append(1) 
d['a'].append(2) 
d['b'].append(4)
```

这样d\['a'\]就是列表

## 字典排序

```python
from collections import OrderedDict 
def ordered_dict(): 
    d = OrderedDict() 
    d['foo'] = 1 
    d['bar'] = 
    2 d['spam'] = 3 
    d['grok'] = 4 
    # Outputs "foo 1", "bar 2", "spam 3", "grok 4" 
    for key in d: 
        print(key, d[key]
```

## 字典运算

需要zip\(dic.values\(\),dic.keys\(\)\)来翻转，才能作用与min,max,sorted 再sorted\(dic, key=lambda k: p

