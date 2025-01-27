#### removeRange

```
protected void removeRange(int fromIndex,
                           int toIndex)
```
Removes from this list all of the elements whose index is between
`fromIndex`, inclusive, and `toIndex`, exclusive.
Shifts any succeeding elements to the left (reduces their index).
This call shortens the list by `(toIndex - fromIndex)` elements.
(If `toIndex==fromIndex`, this operation has no effect.)
Overrides:
`removeRange` in class `AbstractList<E>`
Parameters:
`fromIndex` - index of first element to be removed
`toIndex` - index after last element to be removed
Throws:
`IndexOutOfBoundsException` - if `fromIndex` or
`toIndex` is out of range
(`fromIndex < 0 ||
fromIndex >= size() ||
toIndex > size() ||
toIndex < fromIndex`)

