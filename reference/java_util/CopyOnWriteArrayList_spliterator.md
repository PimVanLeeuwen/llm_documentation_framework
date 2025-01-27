#### spliterator

```
public Spliterator<E> spliterator()
```
Returns a `Spliterator` over the elements in this list.The `Spliterator` reports `Spliterator.IMMUTABLE`,
`Spliterator.ORDERED`, `Spliterator.SIZED`, and
`Spliterator.SUBSIZED`.The spliterator provides a snapshot of the state of the list
when the spliterator was constructed. No synchronization is needed while
operating on the spliterator.
Specified by:
`spliterator` in interface `Iterable<E>`
Specified by:
`spliterator` in interface `Collection<E>`
Specified by:
`spliterator` in interface `List<E>`
Returns:
a `Spliterator` over the elements in this list
Since:
1.8

