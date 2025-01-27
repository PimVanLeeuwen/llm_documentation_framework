#### spliterator

```
public Spliterator<E> spliterator()
```
Creates a late-binding
and fail-fast `Spliterator` over the elements in this set.The `Spliterator` reports `Spliterator.SIZED`,
`Spliterator.DISTINCT`, and `ORDERED`. Implementations
should document the reporting of additional characteristic values.
Specified by:
`spliterator` in interface `Iterable<E>`
Specified by:
`spliterator` in interface `Collection<E>`
Specified by:
`spliterator` in interface `Set<E>`
Overrides:
`spliterator` in class `HashSet<E>`
Implementation Note:
The implementation creates a
late-binding spliterator
from the set's `Iterator`. The spliterator inherits the
fail-fast properties of the set's iterator.
The created `Spliterator` additionally reports
`Spliterator.SUBSIZED`.
Returns:
a `Spliterator` over the elements in this set
Since:
1.8




