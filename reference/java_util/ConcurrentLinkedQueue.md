```
public class ConcurrentLinkedQueue<E>
extends AbstractQueue<E>
implements Queue<E>, Serializable
```
An unbounded thread-safe queue based on linked nodes.
This queue orders elements FIFO (first-in-first-out).
The head of the queue is that element that has been on the
queue the longest time.
The tail of the queue is that element that has been on the
queue the shortest time. New elements
are inserted at the tail of the queue, and the queue retrieval
operations obtain elements at the head of the queue.
A `ConcurrentLinkedQueue` is an appropriate choice when
many threads will share access to a common collection.
Like most other concurrent collection implementations, this class
does not permit the use of `null` elements.This implementation employs an efficient non-blocking
algorithm based on one described in  Simple,
Fast, and Practical Non-Blocking and Blocking Concurrent Queue
Algorithms by Maged M. Michael and Michael L. Scott.Iterators are weakly consistent, returning elements
reflecting the state of the queue at some point at or since the
creation of the iterator. They do not throw `ConcurrentModificationException`, and may proceed concurrently
with other operations. Elements contained in the queue since the creation
of the iterator will be returned exactly once.Beware that, unlike in most collections, the `size` method
is NOT a constant-time operation. Because of the
asynchronous nature of these queues, determining the current number
of elements requires a traversal of the elements, and so may report
inaccurate results if this collection is modified during traversal.
Additionally, the bulk operations `addAll`,
`removeAll`, `retainAll`, `containsAll`,
`equals`, and `toArray` are not guaranteed
to be performed atomically. For example, an iterator operating
concurrently with an `addAll` operation might view only some
of the added elements.This class and its iterator implement all of the optional
methods of the `Queue` and `Iterator` interfaces.Memory consistency effects: As with other concurrent
collections, actions in a thread prior to placing an object into a
`ConcurrentLinkedQueue`
happen-before
actions subsequent to the access or removal of that element from
the `ConcurrentLinkedQueue` in another thread.This class is a member of the
Java Collections Framework.
Since:
1.5
See Also:
Serialized Form
