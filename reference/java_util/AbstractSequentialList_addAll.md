#### addAll

```
public boolean addAll(int index,
                      Collection<? extends E> c)
```
Inserts all of the elements in the specified collection into this
list at the specified position (optional operation). Shifts the
element currently at that position (if any) and any subsequent
elements to the right (increases their indices). The new elements
will appear in this list in the order that they are returned by the
specified collection's iterator. The behavior of this operation is
undefined if the specified collection is modified while the
operation is in progress. (Note that this will occur if the specified
collection is this list, and it's nonempty.)This implementation gets an iterator over the specified collection and
a list iterator over this list pointing to the indexed element (with
listIterator(index)). Then, it iterates over the specified
collection, inserting the elements obtained from the iterator into this
list, one at a time, using ListIterator.add followed by
ListIterator.next (to skip over the added element).Note that this implementation will throw an
UnsupportedOperationException if the list iterator returned by
the listIterator method does not implement the add
operation.
Specified by:
`addAll` in interface `List<E>`
Overrides:
`addAll` in class `AbstractList<E>`
Parameters:
`index` - index at which to insert the first element from the
specified collection
`c` - collection containing elements to be added to this list
Returns:
true if this list changed as a result of the call
Throws:
`UnsupportedOperationException` - if the addAll operation
is not supported by this list
`ClassCastException` - if the class of an element of the specified
collection prevents it from being added to this list
`NullPointerException` - if the specified collection contains one
or more null elements and this list does not permit null
elements, or if the specified collection is null
`IllegalArgumentException` - if some property of an element of the
specified collection prevents it from being added to this list
`IndexOutOfBoundsException` - if the index is out of range
(index < 0 || index > size())

