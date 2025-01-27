#### spliterator

```
default Spliterator<E> spliterator()
```
Creates a `Spliterator` over the elements in this collection.
Implementations should document characteristic values reported by the
spliterator. Such characteristic values are not required to be reported
if the spliterator reports `Spliterator.SIZED` and this collection
contains no elements.The default implementation should be overridden by subclasses that
can return a more efficient spliterator. In order to
preserve expected laziness behavior for the `stream()` and
`parallelStream()`} methods, spliterators should either have the
characteristic of `IMMUTABLE` or `CONCURRENT`, or be
late-binding.
If none of these is practical, the overriding class should describe the
spliterator's documented policy of binding and structural interference,
and should override the `stream()` and `parallelStream()`
methods to create streams using a `Supplier` of the spliterator,
as in:
```

     Stream<E> s = StreamSupport.stream(() -> spliterator(), spliteratorCharacteristics)
 
```
These requirements ensure that streams produced by the
`stream()` and `parallelStream()` methods will reflect the
contents of the collection as of initiation of the terminal stream
operation.
Specified by:
`spliterator` in interface `Iterable<E>`
Implementation Requirements:
The default implementation creates a
late-binding spliterator
from the collections's `Iterator`. The spliterator inherits the
fail-fast properties of the collection's iterator.The created `Spliterator` reports `Spliterator.SIZED`.
Implementation Note:
The created `Spliterator` additionally reports
`Spliterator.SUBSIZED`.If a spliterator covers no elements then the reporting of additional
characteristic values, beyond that of `SIZED` and `SUBSIZED`,
does not aid clients to control, specialize or simplify computation.
However, this does enable shared use of an immutable and empty
spliterator instance (see `Spliterators.emptySpliterator()`) for
empty collections, and enables clients to determine if such a spliterator
covers no elements.
Returns:
a `Spliterator` over the elements in this collection
Since:
1.8

