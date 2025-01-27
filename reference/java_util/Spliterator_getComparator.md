#### getComparator

```
default Comparator<? super T> getComparator()
```
If this Spliterator's source is `SORTED` by a `Comparator`,
returns that `Comparator`. If the source is `SORTED` in
natural order, returns `null`. Otherwise,
if the source is not `SORTED`, throws `IllegalStateException`.
Implementation Requirements:
The default implementation always throws `IllegalStateException`.
Returns:
a Comparator, or `null` if the elements are sorted in the
natural order.
Throws:
`IllegalStateException` - if the spliterator does not report
a characteristic of `SORTED`.




