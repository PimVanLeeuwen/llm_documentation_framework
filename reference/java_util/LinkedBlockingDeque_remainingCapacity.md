#### remainingCapacity

```
public int remainingCapacity()
```
Returns the number of additional elements that this deque can ideally
(in the absence of memory or resource constraints) accept without
blocking. This is always equal to the initial capacity of this deque
less the current `size` of this deque.Note that you cannot always tell if an attempt to insert
an element will succeed by inspecting `remainingCapacity`
because it may be the case that another thread is about to
insert or remove an element.
Specified by:
`remainingCapacity` in interface `BlockingQueue<E>`
Returns:
the remaining capacity

