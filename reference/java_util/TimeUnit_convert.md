#### convert

```
public long convert(long sourceDuration,
                    TimeUnit sourceUnit)
```
Converts the given time duration in the given unit to this unit.
Conversions from finer to coarser granularities truncate, so
lose precision. For example, converting `999` milliseconds
to seconds results in `0`. Conversions from coarser to
finer granularities with arguments that would numerically
overflow saturate to `Long.MIN_VALUE` if negative or
`Long.MAX_VALUE` if positive.For example, to convert 10 minutes to milliseconds, use:
`TimeUnit.MILLISECONDS.convert(10L, TimeUnit.MINUTES)`
Parameters:
`sourceDuration` - the time duration in the given `sourceUnit`
`sourceUnit` - the unit of the `sourceDuration` argument
Returns:
the converted duration in this unit,
or `Long.MIN_VALUE` if conversion would negatively
overflow, or `Long.MAX_VALUE` if it would positively overflow.

