#### spliterator

```
default Spliterator<E> spliterator()
```
Creates a `Spliterator` over the elements in this set.The `Spliterator` reports `Spliterator.DISTINCT`.
Implementations should document the reporting of additional
characteristic values.
Specified by:
`spliterator` in interface `Collection<E>`
Specified by:
`spliterator` in interface `Iterable<E>`
Implementation Requirements:
The default implementation creates a
late-binding spliterator
from the set's `Iterator`. The spliterator inherits the
fail-fast properties of the set's iterator.The created `Spliterator` additionally reports
`Spliterator.SIZED`.
Implementation Note:
The created `Spliterator` additionally reports
`Spliterator.SUBSIZED`.
Returns:
a `Spliterator` over the elements in this set
Since:
1.8




