```
public class LinkedBlockingQueue<E>
extends AbstractQueue<E>
implements BlockingQueue<E>, Serializable
```
An optionally-bounded blocking queue based on
linked nodes.
This queue orders elements FIFO (first-in-first-out).
The head of the queue is that element that has been on the
queue the longest time.
The tail of the queue is that element that has been on the
queue the shortest time. New elements
are inserted at the tail of the queue, and the queue retrieval
operations obtain elements at the head of the queue.
Linked queues typically have higher throughput than array-based queues but
less predictable performance in most concurrent applications.The optional capacity bound constructor argument serves as a
way to prevent excessive queue expansion. The capacity, if unspecified,
is equal to `Integer.MAX_VALUE`. Linked nodes are
dynamically created upon each insertion unless this would bring the
queue above capacity.This class and its iterator implement all of the
optional methods of the `Collection` and `Iterator` interfaces.This class is a member of the
Java Collections Framework.
Since:
1.5
See Also:
Serialized Form
