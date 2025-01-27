#### size

```
public int size()
```
Returns the number of elements in this set. If this set
contains more than `Integer.MAX_VALUE` elements, it
returns `Integer.MAX_VALUE`.Beware that, unlike in most collections, this method is
NOT a constant-time operation. Because of the
asynchronous nature of these sets, determining the current
number of elements requires traversing them all to count them.
Additionally, it is possible for the size to change during
execution of this method, in which case the returned result
will be inaccurate. Thus, this method is typically not very
useful in concurrent applications.
Specified by:
`size` in interface `Collection<E>`
Specified by:
`size` in interface `Set<E>`
Specified by:
`size` in class `AbstractCollection<E>`
Returns:
the number of elements in this set

