```
public interface BlockingDeque<E>
extends BlockingQueue<E>, Deque<E>
```
A `Deque` that additionally supports blocking operations that wait
for the deque to become non-empty when retrieving an element, and wait for
space to become available in the deque when storing an element.`BlockingDeque` methods come in four forms, with different ways
of handling operations that cannot be satisfied immediately, but may be
satisfied at some point in the future:
one throws an exception, the second returns a special value (either
`null` or `false`, depending on the operation), the third
blocks the current thread indefinitely until the operation can succeed,
and the fourth blocks for only a given maximum time limit before giving
up. These methods are summarized in the following table:

Summary of BlockingDeque methodsFirst Element (Head)Throws exceptionSpecial valueBlocksTimes outInsert`addFirst(e)``offerFirst(e)``putFirst(e)``offerFirst(e, time, unit)`Remove`removeFirst()``pollFirst()``takeFirst()``pollFirst(time, unit)`Examine`getFirst()``peekFirst()`not applicablenot applicableLast Element (Tail)Throws exceptionSpecial valueBlocksTimes outInsert`addLast(e)``offerLast(e)``putLast(e)``offerLast(e, time, unit)`Remove`removeLast()``pollLast()``takeLast()``pollLast(time, unit)`Examine`getLast()``peekLast()`not applicablenot applicable
Like any `BlockingQueue`, a `BlockingDeque` is thread safe,
does not permit null elements, and may (or may not) be
capacity-constrained.A `BlockingDeque` implementation may be used directly as a FIFO
`BlockingQueue`. The methods inherited from the
`BlockingQueue` interface are precisely equivalent to
`BlockingDeque` methods as indicated in the following table:

Comparison of BlockingQueue and BlockingDeque methods`BlockingQueue` MethodEquivalent `BlockingDeque` MethodInsert`add(e)``addLast(e)``offer(e)``offerLast(e)``put(e)``putLast(e)``offer(e, time, unit)``offerLast(e, time, unit)`Remove`remove()``removeFirst()``poll()``pollFirst()``take()``takeFirst()``poll(time, unit)``pollFirst(time, unit)`Examine`element()``getFirst()``peek()``peekFirst()`
Memory consistency effects: As with other concurrent
collections, actions in a thread prior to placing an object into a
`BlockingDeque`
happen-before
actions subsequent to the access or removal of that element from
the `BlockingDeque` in another thread.This interface is a member of the
Java Collections Framework.
Since:
1.6
