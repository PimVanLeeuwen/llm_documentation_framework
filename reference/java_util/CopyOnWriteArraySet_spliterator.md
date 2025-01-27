#### spliterator

```
public Spliterator<E> spliterator()
```
Returns a `Spliterator` over the elements in this set in the order
in which these elements were added.The `Spliterator` reports `Spliterator.IMMUTABLE`,
`Spliterator.DISTINCT`, `Spliterator.SIZED`, and
`Spliterator.SUBSIZED`.The spliterator provides a snapshot of the state of the set
when the spliterator was constructed. No synchronization is needed while
operating on the spliterator.
Specified by:
`spliterator` in interface `Iterable<E>`
Specified by:
`spliterator` in interface `Collection<E>`
Specified by:
`spliterator` in interface `Set<E>`
Returns:
a `Spliterator` over the elements in this set
Since:
1.8




