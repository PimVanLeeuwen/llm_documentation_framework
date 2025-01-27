#### size

```
public int size()
```
Returns the number of key-value mappings in this map. If this map
contains more than `Integer.MAX_VALUE` elements, it
returns `Integer.MAX_VALUE`.Beware that, unlike in most collections, this method is
NOT a constant-time operation. Because of the
asynchronous nature of these maps, determining the current
number of elements requires traversing them all to count them.
Additionally, it is possible for the size to change during
execution of this method, in which case the returned result
will be inaccurate. Thus, this method is typically not very
useful in concurrent applications.
Specified by:
`size` in interface `Map<K,V>`
Overrides:
`size` in class `AbstractMap<K,V>`
Returns:
the number of elements in this map

