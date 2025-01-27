#### toSeconds

```
public long toSeconds(long duration)
```
Equivalent to
`SECONDS.convert(duration, this)`.
Parameters:
`duration` - the duration
Returns:
the converted duration,
or `Long.MIN_VALUE` if conversion would negatively
overflow, or `Long.MAX_VALUE` if it would positively overflow.

