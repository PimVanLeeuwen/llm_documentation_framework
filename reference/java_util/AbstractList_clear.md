#### clear

```
public void clear()
```
Removes all of the elements from this list (optional operation).
The list will be empty after this call returns.This implementation calls `removeRange(0, size())`.Note that this implementation throws an
`UnsupportedOperationException` unless `remove(int
index)` or `removeRange(int fromIndex, int toIndex)` is
overridden.
Specified by:
`clear` in interface `Collection<E>`
Specified by:
`clear` in interface `List<E>`
Overrides:
`clear` in class `AbstractCollection<E>`
Throws:
`UnsupportedOperationException` - if the `clear` operation
is not supported by this list

