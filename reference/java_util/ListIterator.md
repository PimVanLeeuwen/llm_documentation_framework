```
public interface ListIterator<E>
extends Iterator<E>
```
An iterator for lists that allows the programmer
to traverse the list in either direction, modify
the list during iteration, and obtain the iterator's
current position in the list. A `ListIterator`
has no current element; its cursor position always
lies between the element that would be returned by a call
to `previous()` and the element that would be
returned by a call to `next()`.
An iterator for a list of length `n` has `n+1` possible
cursor positions, as illustrated by the carets (`^`) below:
```

                      Element(0)   Element(1)   Element(2)   ... Element(n-1)
 cursor positions:  ^            ^            ^            ^                  ^
 
```
Note that the `remove()` and `set(Object)` methods are
not defined in terms of the cursor position; they are defined to
operate on the last element returned by a call to `next()` or
`previous()`.This interface is a member of the
Java Collections Framework.
Since:
1.2
See Also:
`Collection`,
`List`,
`Iterator`,
`Enumeration`,
`List.listIterator()`
