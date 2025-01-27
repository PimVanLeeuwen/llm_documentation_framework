#### spliterator

```
default Spliterator<E> spliterator()
```
Creates a `Spliterator` over the elements in this sorted set.The `Spliterator` reports `Spliterator.DISTINCT`,
`Spliterator.SORTED` and `Spliterator.ORDERED`.
Implementations should document the reporting of additional
characteristic values.The spliterator's comparator (see
`Spliterator.getComparator()`) must be `null` if
the sorted set's comparator (see `comparator()`) is `null`.
Otherwise, the spliterator's comparator must be the same as or impose the
same total ordering as the sorted set's comparator.
Specified by:
`spliterator` in interface `Collection<E>`
Specified by:
`spliterator` in interface `Iterable<E>`
Specified by:
`spliterator` in interface `Set<E>`
Implementation Requirements:
The default implementation creates a
late-binding spliterator
from the sorted set's `Iterator`. The spliterator inherits the
fail-fast properties of the set's iterator. The
spliterator's comparator is the same as the sorted set's comparator.The created `Spliterator` additionally reports
`Spliterator.SIZED`.
Implementation Note:
The created `Spliterator` additionally reports
`Spliterator.SUBSIZED`.
Returns:
a `Spliterator` over the elements in this sorted set
Since:
1.8




