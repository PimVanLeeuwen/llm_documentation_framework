#### spliterator

```
public Spliterator<E> spliterator()
```
Creates a late-binding
and fail-fast `Spliterator` over the elements in this
list.The `Spliterator` reports `Spliterator.SIZED` and
`Spliterator.ORDERED`. Overriding implementations should document
the reporting of additional characteristic values.
Specified by:
`spliterator` in interface `Iterable<E>`
Specified by:
`spliterator` in interface `Collection<E>`
Specified by:
`spliterator` in interface `List<E>`
Implementation Note:
The `Spliterator` additionally reports `Spliterator.SUBSIZED`
and implements `trySplit` to permit limited parallelism..
Returns:
a `Spliterator` over the elements in this list
Since:
1.8




