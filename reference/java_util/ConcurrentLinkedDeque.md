```
public class ConcurrentLinkedDeque<E>
extends AbstractCollection<E>
implements Deque<E>, Serializable
```
An unbounded concurrent deque based on linked nodes.
Concurrent insertion, removal, and access operations execute safely
across multiple threads.
A `ConcurrentLinkedDeque` is an appropriate choice when
many threads will share access to a common collection.
Like most other concurrent collection implementations, this class
does not permit the use of `null` elements.Iterators and spliterators are
weakly consistent.Beware that, unlike in most collections, the `size` method
is NOT a constant-time operation. Because of the
asynchronous nature of these deques, determining the current number
of elements requires a traversal of the elements, and so may report
inaccurate results if this collection is modified during traversal.
Additionally, the bulk operations `addAll`,
`removeAll`, `retainAll`, `containsAll`,
`equals`, and `toArray` are not guaranteed
to be performed atomically. For example, an iterator operating
concurrently with an `addAll` operation might view only some
of the added elements.This class and its iterator implement all of the optional
methods of the `Deque` and `Iterator` interfaces.Memory consistency effects: As with other concurrent collections,
actions in a thread prior to placing an object into a
`ConcurrentLinkedDeque`
happen-before
actions subsequent to the access or removal of that element from
the `ConcurrentLinkedDeque` in another thread.This class is a member of the
Java Collections Framework.
Since:
1.7
See Also:
Serialized Form
