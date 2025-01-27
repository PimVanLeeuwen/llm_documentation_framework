#### remove

```
public E remove(int index)
```
Removes the element at the specified position in this Vector.
Shifts any subsequent elements to the left (subtracts one from their
indices). Returns the element that was removed from the Vector.
Specified by:
`remove` in interface `List<E>`
Overrides:
`remove` in class `AbstractList<E>`
Parameters:
`index` - the index of the element to be removed
Returns:
element that was removed
Throws:
`ArrayIndexOutOfBoundsException` - if the index is out of range
(`index < 0 || index >= size()`)
Since:
1.2

