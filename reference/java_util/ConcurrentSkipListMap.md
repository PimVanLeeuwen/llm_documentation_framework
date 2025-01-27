```
public class ConcurrentSkipListMap<K,V>
extends AbstractMap<K,V>
implements ConcurrentNavigableMap<K,V>, Cloneable, Serializable
```
A scalable concurrent `ConcurrentNavigableMap` implementation.
The map is sorted according to the natural
ordering of its keys, or by a `Comparator` provided at map
creation time, depending on which constructor is used.This class implements a concurrent variant of SkipLists
providing expected average log(n) time cost for the
`containsKey`, `get`, `put` and
`remove` operations and their variants. Insertion, removal,
update, and access operations safely execute concurrently by
multiple threads.Iterators and spliterators are
weakly consistent.Ascending key ordered views and their iterators are faster than
descending ones.All `Map.Entry` pairs returned by methods in this class
and its views represent snapshots of mappings at the time they were
produced. They do not support the `Entry.setValue`
method. (Note however that it is possible to change mappings in the
associated map using `put`, `putIfAbsent`, or
`replace`, depending on exactly which effect you need.)Beware that, unlike in most collections, the `size`
method is not a constant-time operation. Because of the
asynchronous nature of these maps, determining the current number
of elements requires a traversal of the elements, and so may report
inaccurate results if this collection is modified during traversal.
Additionally, the bulk operations `putAll`, `equals`,
`toArray`, `containsValue`, and `clear` are
not guaranteed to be performed atomically. For example, an
iterator operating concurrently with a `putAll` operation
might view only some of the added elements.This class and its views and iterators implement all of the
optional methods of the `Map` and `Iterator`
interfaces. Like most other concurrent collections, this class does
not permit the use of `null` keys or values because some
null return values cannot be reliably distinguished from the absence of
elements.This class is a member of the
Java Collections Framework.
Since:
1.6
See Also:
Serialized Form
