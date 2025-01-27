#### from

```
public static GregorianCalendar from(ZonedDateTime zdt)
```
Obtains an instance of `GregorianCalendar` with the default locale
from a `ZonedDateTime` object.Since `ZonedDateTime` does not support a Julian-Gregorian cutover
date and uses ISO calendar system, the return GregorianCalendar is a pure
Gregorian calendar and uses ISO 8601 standard for week definitions,
which has `MONDAY` as the `FirstDayOfWeek` and `4` as the value of the
`MinimalDaysInFirstWeek`.`ZoneDateTime` can store points on the time-line further in the
future and further in the past than `GregorianCalendar`. In this
scenario, this method will throw an `IllegalArgumentException`
exception.
Parameters:
`zdt` - the zoned date-time object to convert
Returns:
the gregorian calendar representing the same point on the
time-line as the zoned date-time provided
Throws:
`NullPointerException` - if `zdt` is null
`IllegalArgumentException` - if the zoned date-time is too
large to represent as a `GregorianCalendar`
Since:
1.8




