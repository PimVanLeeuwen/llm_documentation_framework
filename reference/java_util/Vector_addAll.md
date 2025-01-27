#### addAll

```
public boolean addAll(int index,
                      Collection<? extends E> c)
```
Inserts all of the elements in the specified Collection into this
Vector at the specified position. Shifts the element currently at
that position (if any) and any subsequent elements to the right
(increases their indices). The new elements will appear in the Vector
in the order that they are returned by the specified Collection's
iterator.
Specified by:
`addAll` in interface `List<E>`
Overrides:
`addAll` in class `AbstractList<E>`
Parameters:
`index` - index at which to insert the first element from the
specified collection
`c` - elements to be inserted into this Vector
Returns:
`true` if this Vector changed as a result of the call
Throws:
`ArrayIndexOutOfBoundsException` - if the index is out of range
(`index < 0 || index > size()`)
`NullPointerException` - if the specified collection is null
Since:
1.2

