#### add

```
public void add(int index,
                E element)
```
Inserts the specified element at the specified position in this list
(optional operation). Shifts the element currently at that position
(if any) and any subsequent elements to the right (adds one to their
indices).This implementation first gets a list iterator pointing to the
indexed element (with listIterator(index)). Then, it
inserts the specified element with ListIterator.add.Note that this implementation will throw an
UnsupportedOperationException if the list iterator does not
implement the add operation.
Specified by:
`add` in interface `List<E>`
Overrides:
`add` in class `AbstractList<E>`
Parameters:
`index` - index at which the specified element is to be inserted
`element` - element to be inserted
Throws:
`UnsupportedOperationException` - if the add operation
is not supported by this list
`ClassCastException` - if the class of the specified element
prevents it from being added to this list
`NullPointerException` - if the specified element is null and
this list does not permit null elements
`IllegalArgumentException` - if some property of the specified
element prevents it from being added to this list
`IndexOutOfBoundsException` - if the index is out of range
(index < 0 || index > size())

