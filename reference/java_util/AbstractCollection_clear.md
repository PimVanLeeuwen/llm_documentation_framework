#### clear

```
public void clear()
```
Removes all of the elements from this collection (optional operation).
The collection will be empty after this method returns.This implementation iterates over this collection, removing each
element using the Iterator.remove operation. Most
implementations will probably choose to override this method for
efficiency.Note that this implementation will throw an
UnsupportedOperationException if the iterator returned by this
collection's iterator method does not implement the
remove method and this collection is non-empty.
Specified by:
`clear` in interface `Collection<E>`
Throws:
`UnsupportedOperationException` - if the clear operation
is not supported by this collection

