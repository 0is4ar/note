# super

`super(Dog,self).greet()` 在python3中 == `super().greet()`

`super(cls, inst)` 获得的是 cls 在 inst 的 MRO 列表中的下一个类。

```python
>>> C.mro()   # or C.__mro__ or C().__class__.mro()
[__main__.C, __main__.A, __main__.B, __main__.Base, object]
```

这就是一个类的mro列表，它是通过一个C3线性算法实现的，不深究

