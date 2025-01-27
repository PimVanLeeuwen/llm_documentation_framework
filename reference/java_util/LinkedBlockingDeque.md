```
public class LinkedBlockingDeque<E>
extends AbstractQueue<E>
implements BlockingDeque<E>, Serializable
```
An optionally-bounded blocking deque based on
linked nodes.The optional capacity bound constructor argument serves as a
way to prevent excessive expansion. The capacity, if unspecified,
is equal to `Integer.MAX_VALUE`. Linked nodes are
dynamically created upon each insertion unless this would bring the
deque above capacity.Most operations run in constant time (ignoring time spent
blocking). Exceptions include `remove`,
`removeFirstOccurrence`, `removeLastOccurrence`, `contains`, `iterator.remove()`, and the bulk
operations, all of which run in linear time.This class and its iterator implement all of the
optional methods of the `Collection` and `Iterator` interfaces.This class is a member of the
Java Collections Framework.
Since:
1.6
See Also:
Serialized Form
