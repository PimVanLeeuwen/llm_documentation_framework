#### spliterator

```
public Spliterator<E> spliterator()
```
Returns a `Spliterator` over the elements in this set.The `Spliterator` reports `Spliterator.CONCURRENT`,
`Spliterator.NONNULL`, `Spliterator.DISTINCT`,
`Spliterator.SORTED` and `Spliterator.ORDERED`, with an
encounter order that is ascending order. Overriding implementations
should document the reporting of additional characteristic values.The spliterator's comparator (see
`Spliterator.getComparator()`) is `null` if
the set's comparator (see `comparator()`) is `null`.
Otherwise, the spliterator's comparator is the same as or imposes the
same total ordering as the set's comparator.
Specified by:
`spliterator` in interface `Iterable<E>`
Specified by:
`spliterator` in interface `Collection<E>`
Specified by:
`spliterator` in interface `Set<E>`
Specified by:
`spliterator` in interface `SortedSet<E>`
Returns:
a `Spliterator` over the elements in this set
Since:
1.8




