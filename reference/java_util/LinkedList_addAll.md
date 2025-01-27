#### addAll

```
public boolean addAll(int index,
                      Collection<? extends E> c)
```
Inserts all of the elements in the specified collection into this
list, starting at the specified position. Shifts the element
currently at that position (if any) and any subsequent elements to
the right (increases their indices). The new elements will appear
in the list in the order that they are returned by the
specified collection's iterator.
Specified by:
`addAll` in interface `List<E>`
Overrides:
`addAll` in class `AbstractSequentialList<E>`
Parameters:
`index` - index at which to insert the first element
from the specified collection
`c` - collection containing elements to be added to this list
Returns:
`true` if this list changed as a result of the call
Throws:
`IndexOutOfBoundsException` - if the index is out of range
(index < 0 || index > size())
`NullPointerException` - if the specified collection is null

