#### spliterator

```
public Spliterator<E> spliterator()
```
Returns a `Spliterator` over the elements in this queue.The returned spliterator is
weakly consistent.The `Spliterator` reports `Spliterator.SIZED` and
`Spliterator.NONNULL`.
Specified by:
`spliterator` in interface `Iterable<E>`
Specified by:
`spliterator` in interface `Collection<E>`
Implementation Note:
The `Spliterator` additionally reports `Spliterator.SUBSIZED`.
Returns:
a `Spliterator` over the elements in this queue
Since:
1.8




