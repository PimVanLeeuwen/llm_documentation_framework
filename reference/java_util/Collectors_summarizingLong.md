#### summarizingLong

```
public static <T> Collector<T,?,LongSummaryStatistics> summarizingLong(ToLongFunction<? super T> mapper)
```
Returns a `Collector` which applies an `long`-producing
mapping function to each input element, and returns summary statistics
for the resulting values.
Type Parameters:
`T` - the type of the input elements
Parameters:
`mapper` - the mapping function to apply to each element
Returns:
a `Collector` implementing the summary-statistics reduction
See Also:
`summarizingDouble(ToDoubleFunction)`,
`summarizingInt(ToIntFunction)`

