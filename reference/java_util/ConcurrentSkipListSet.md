```
public class ConcurrentSkipListSet<E>
extends AbstractSet<E>
implements NavigableSet<E>, Cloneable, Serializable
```
A scalable concurrent `NavigableSet` implementation based on
a `ConcurrentSkipListMap`. The elements of the set are kept
sorted according to their natural ordering,
or by a `Comparator` provided at set creation time, depending
on which constructor is used.This implementation provides expected average log(n) time
cost for the `contains`, `add`, and `remove`
operations and their variants. Insertion, removal, and access
operations safely execute concurrently by multiple threads.Iterators and spliterators are
weakly consistent.Ascending ordered views and their iterators are faster than
descending ones.Beware that, unlike in most collections, the `size`
method is not a constant-time operation. Because of the
asynchronous nature of these sets, determining the current number
of elements requires a traversal of the elements, and so may report
inaccurate results if this collection is modified during traversal.
Additionally, the bulk operations `addAll`,
`removeAll`, `retainAll`, `containsAll`,
`equals`, and `toArray` are not guaranteed
to be performed atomically. For example, an iterator operating
concurrently with an `addAll` operation might view only some
of the added elements.This class and its iterators implement all of the
optional methods of the `Set` and `Iterator`
interfaces. Like most other concurrent collection implementations,
this class does not permit the use of `null` elements,
because `null` arguments and return values cannot be reliably
distinguished from the absence of elements.This class is a member of the
Java Collections Framework.
Since:
1.6
See Also:
Serialized Form
