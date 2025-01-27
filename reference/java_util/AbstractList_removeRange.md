#### removeRange

```
protected void removeRange(int fromIndex,
                           int toIndex)
```
Removes from this list all of the elements whose index is between
`fromIndex`, inclusive, and `toIndex`, exclusive.
Shifts any succeeding elements to the left (reduces their index).
This call shortens the list by `(toIndex - fromIndex)` elements.
(If `toIndex==fromIndex`, this operation has no effect.)This method is called by the `clear` operation on this list
and its subLists. Overriding this method to take advantage of
the internals of the list implementation can substantially
improve the performance of the `clear` operation on this list
and its subLists.This implementation gets a list iterator positioned before
`fromIndex`, and repeatedly calls `ListIterator.next`
followed by `ListIterator.remove` until the entire range has
been removed. Note: if `ListIterator.remove` requires linear
time, this implementation requires quadratic time.
Parameters:
`fromIndex` - index of first element to be removed
`toIndex` - index after last element to be removed




