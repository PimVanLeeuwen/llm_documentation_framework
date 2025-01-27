#### spliterator

```
public Spliterator<E> spliterator()
```
Returns a `Spliterator` over the elements in this deque.The returned spliterator is
weakly consistent.The `Spliterator` reports `Spliterator.CONCURRENT`,
`Spliterator.ORDERED`, and `Spliterator.NONNULL`.
Specified by:
`spliterator` in interface `Iterable<E>`
Specified by:
`spliterator` in interface `Collection<E>`
Implementation Note:
The `Spliterator` implements `trySplit` to permit limited
parallelism.
Returns:
a `Spliterator` over the elements in this deque
Since:
1.8




