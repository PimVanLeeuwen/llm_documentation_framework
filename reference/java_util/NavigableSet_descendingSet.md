#### descendingSet

```
NavigableSet<E> descendingSet()
```
Returns a reverse order view of the elements contained in this set.
The descending set is backed by this set, so changes to the set are
reflected in the descending set, and vice-versa. If either set is
modified while an iteration over either set is in progress (except
through the iterator's own `remove` operation), the results of
the iteration are undefined.The returned set has an ordering equivalent to
`Collections.reverseOrder`(comparator()).
The expression `s.descendingSet().descendingSet()` returns a
view of `s` essentially equivalent to `s`.
Returns:
a reverse order view of this set

