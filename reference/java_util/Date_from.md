#### from

```
public static Date from(Instant instant)
```
Obtains an instance of `Date` from an `Instant` object.`Instant` uses a precision of nanoseconds, whereas `Date`
uses a precision of milliseconds. The conversion will trancate any
excess precision information as though the amount in nanoseconds was
subject to integer division by one million.`Instant` can store points on the time-line further in the future
and further in the past than `Date`. In this scenario, this method
will throw an exception.
Parameters:
`instant` - the instant to convert
Returns:
a `Date` representing the same point on the time-line as
the provided instant
Throws:
`NullPointerException` - if `instant` is null.
`IllegalArgumentException` - if the instant is too large to
represent as a `Date`
Since:
1.8

