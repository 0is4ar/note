# Code style

## indent 
2 spaces per indentation level

Never use tabs

## line length
Try to limit most lines to a maximum of 79 characters

after '\', 4 spaces for next line

```python
class Rectangle(Blob):
  def __init__(self, width, height,
    color='black', emphasis=None, highlight=0):
    if width == 0 and height == 0 and \
        color == 'red' and emphasis == 'strong' or \
        highlight > 100:
      raise ValueError("sorry, you lose")
    if width == 0 and height == 0 and (color == 'red' or
        emphasis is None):
      raise ValueError("I don't think so -- values are %s, %s" %
          (width, height))
    Blob.__init__(self, width, height,
        color, emphasis, highlight)
    ```

## blank line

5 blank lines for top-level function and class
2 lines method in a class

- avoid if being so far from else

## import 

