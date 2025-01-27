#### removeIf

```
default boolean removeIf(Predicate<? super E> filter)
```
Removes all of the elements of this collection that satisfy the given
predicate. Errors or runtime exceptions thrown during iteration or by
the predicate are relayed to the caller.
Implementation Requirements:
The default implementation traverses all elements of the collection using
its `iterator()`. Each matching element is removed using
`Iterator.remove()`. If the collection's iterator does not
support removal then an `UnsupportedOperationException` will be
thrown on the first matching element.
Parameters:
`filter` - a predicate which returns `true` for elements to be
removed
Returns:
`true` if any elements were removed
Throws:
`NullPointerException` - if the specified filter is null
`UnsupportedOperationException` - if elements cannot be removed
from this collection. Implementations may throw this exception if a
matching element cannot be removed or if, in general, removal is not
supported.
Since:
1.8

