```
public class LinkedTransferQueue<E>
extends AbstractQueue<E>
implements TransferQueue<E>, Serializable
```
An unbounded `TransferQueue` based on linked nodes.
This queue orders elements FIFO (first-in-first-out) with respect
to any given producer. The head of the queue is that
element that has been on the queue the longest time for some
producer. The tail of the queue is that element that has
been on the queue the shortest time for some producer.Beware that, unlike in most collections, the `size` method
is NOT a constant-time operation. Because of the
asynchronous nature of these queues, determining the current number
of elements requires a traversal of the elements, and so may report
inaccurate results if this collection is modified during traversal.
Additionally, the bulk operations `addAll`,
`removeAll`, `retainAll`, `containsAll`,
`equals`, and `toArray` are not guaranteed
to be performed atomically. For example, an iterator operating
concurrently with an `addAll` operation might view only some
of the added elements.This class and its iterator implement all of the
optional methods of the `Collection` and `Iterator` interfaces.Memory consistency effects: As with other concurrent
collections, actions in a thread prior to placing an object into a
`LinkedTransferQueue`
happen-before
actions subsequent to the access or removal of that element from
the `LinkedTransferQueue` in another thread.This class is a member of the
Java Collections Framework.
Since:
1.7
See Also:
Serialized Form
