#### removeIf

```
public boolean removeIf(Predicate<? super E> filter)
```
Description copied from interface: `Collection`
Removes all of the elements of this collection that satisfy the given
predicate. Errors or runtime exceptions thrown during iteration or by
the predicate are relayed to the caller.
Specified by:
`removeIf` in interface `Collection<E>`
Parameters:
`filter` - a predicate which returns `true` for elements to be
removed
Returns:
`true` if any elements were removed

