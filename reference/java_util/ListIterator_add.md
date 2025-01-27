#### add

```
void add(E e)
```
Inserts the specified element into the list (optional operation).
The element is inserted immediately before the element that
would be returned by `next()`, if any, and after the element
that would be returned by `previous()`, if any. (If the
list contains no elements, the new element becomes the sole element
on the list.) The new element is inserted before the implicit
cursor: a subsequent call to `next` would be unaffected, and a
subsequent call to `previous` would return the new element.
(This call increases by one the value that would be returned by a
call to `nextIndex` or `previousIndex`.)
Parameters:
`e` - the element to insert
Throws:
`UnsupportedOperationException` - if the `add` method is
not supported by this list iterator
`ClassCastException` - if the class of the specified element
prevents it from being added to this list
`IllegalArgumentException` - if some aspect of this element
prevents it from being added to this list




