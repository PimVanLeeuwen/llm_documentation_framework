#### setSize

```
public void setSize(int newSize)
```
Sets the size of this vector. If the new size is greater than the
current size, new `null` items are added to the end of
the vector. If the new size is less than the current size, all
components at index `newSize` and greater are discarded.
Parameters:
`newSize` - the new size of this vector
Throws:
`ArrayIndexOutOfBoundsException` - if the new size is negative

