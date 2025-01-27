#### subList

```
public List<E> subList(int fromIndex,
                       int toIndex)
```
Returns a view of the portion of this list between the specified
fromIndex, inclusive, and toIndex, exclusive. (If
fromIndex and toIndex are equal, the returned list is
empty.) The returned list is backed by this list, so non-structural
changes in the returned list are reflected in this list, and vice-versa.
The returned list supports all of the optional list operations supported
by this list.This method eliminates the need for explicit range operations (of
the sort that commonly exist for arrays). Any operation that expects
a list can be used as a range operation by passing a subList view
instead of a whole list. For example, the following idiom
removes a range of elements from a list:
```

      list.subList(from, to).clear();
 
```
Similar idioms may be constructed for indexOf and
lastIndexOf, and all of the algorithms in the
Collections class can be applied to a subList.The semantics of the list returned by this method become undefined if
the backing list (i.e., this list) is structurally modified in
any way other than via the returned list. (Structural modifications are
those that change the size of this list, or otherwise perturb it in such
a fashion that iterations in progress may yield incorrect results.)This implementation returns a list that subclasses
`AbstractList`. The subclass stores, in private fields, the
offset of the subList within the backing list, the size of the subList
(which can change over its lifetime), and the expected
`modCount` value of the backing list. There are two variants
of the subclass, one of which implements `RandomAccess`.
If this list implements `RandomAccess` the returned list will
be an instance of the subclass that implements `RandomAccess`.The subclass's `set(int, E)`, `get(int)`,
`add(int, E)`, `remove(int)`, `addAll(int,
Collection)` and `removeRange(int, int)` methods all
delegate to the corresponding methods on the backing abstract list,
after bounds-checking the index and adjusting for the offset. The
`addAll(Collection c)` method merely returns `addAll(size,
c)`.The `listIterator(int)` method returns a "wrapper object"
over a list iterator on the backing list, which is created with the
corresponding method on the backing list. The `iterator` method
merely returns `listIterator()`, and the `size` method
merely returns the subclass's `size` field.All methods first check to see if the actual `modCount` of
the backing list is equal to its expected value, and throw a
`ConcurrentModificationException` if it is not.
Specified by:
`subList` in interface `List<E>`
Parameters:
`fromIndex` - low endpoint (inclusive) of the subList
`toIndex` - high endpoint (exclusive) of the subList
Returns:
a view of the specified range within this list
Throws:
`IndexOutOfBoundsException` - if an endpoint index value is out of range
`(fromIndex < 0 || toIndex > size)`
`IllegalArgumentException` - if the endpoint indices are out of order
`(fromIndex > toIndex)`

