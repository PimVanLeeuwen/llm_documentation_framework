#### remove

```
public E remove(int index)
```
Removes the element at the specified position in this list (optional
operation). Shifts any subsequent elements to the left (subtracts one
from their indices). Returns the element that was removed from the
list.This implementation always throws an
`UnsupportedOperationException`.
Specified by:
`remove` in interface `List<E>`
Parameters:
`index` - the index of the element to be removed
Returns:
the element previously at the specified position
Throws:
`UnsupportedOperationException` - if the remove operation
is not supported by this list
`IndexOutOfBoundsException` - if the index is out of range
(index < 0 || index >= size())

