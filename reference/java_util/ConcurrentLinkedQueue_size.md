#### size

```
public int size()
```
Returns the number of elements in this queue. If this queue
contains more than `Integer.MAX_VALUE` elements, returns
`Integer.MAX_VALUE`.Beware that, unlike in most collections, this method is
NOT a constant-time operation. Because of the
asynchronous nature of these queues, determining the current
number of elements requires an O(n) traversal.
Additionally, if elements are added or removed during execution
of this method, the returned result may be inaccurate. Thus,
this method is typically not very useful in concurrent
applications.
Specified by:
`size` in interface `Collection<E>`
Specified by:
`size` in class `AbstractCollection<E>`
Returns:
the number of elements in this queue

