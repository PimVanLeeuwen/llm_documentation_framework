#### summarizingInt

```
public static <T> Collector<T,?,IntSummaryStatistics> summarizingInt(ToIntFunction<? super T> mapper)
```
Returns a `Collector` which applies an `int`-producing
mapping function to each input element, and returns summary statistics
for the resulting values.
Type Parameters:
`T` - the type of the input elements
Parameters:
`mapper` - a mapping function to apply to each element
Returns:
a `Collector` implementing the summary-statistics reduction
See Also:
`summarizingDouble(ToDoubleFunction)`,
`summarizingLong(ToLongFunction)`

