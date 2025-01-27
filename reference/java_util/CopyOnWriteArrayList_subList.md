#### subList

```
public List<E> subList(int fromIndex,
                       int toIndex)
```
Returns a view of the portion of this list between
`fromIndex`, inclusive, and `toIndex`, exclusive.
The returned list is backed by this list, so changes in the
returned list are reflected in this list.The semantics of the list returned by this method become
undefined if the backing list (i.e., this list) is modified in
any way other than via the returned list.
Specified by:
`subList` in interface `List<E>`
Parameters:
`fromIndex` - low endpoint (inclusive) of the subList
`toIndex` - high endpoint (exclusive) of the subList
Returns:
a view of the specified range within this list
Throws:
`IndexOutOfBoundsException` - for an illegal endpoint index value
(fromIndex < 0 || toIndex > size ||
fromIndex > toIndex)




