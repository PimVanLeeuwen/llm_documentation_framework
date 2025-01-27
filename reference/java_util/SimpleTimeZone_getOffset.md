#### getOffset

```
public int getOffset(int era,
                     int year,
                     int month,
                     int day,
                     int dayOfWeek,
                     int millis)
```
Returns the difference in milliseconds between local time and
UTC, taking into account both the raw offset and the effect of
daylight saving, for the specified date and time. This method
assumes that the start and end month are distinct. It also
uses a default `GregorianCalendar` object as its
underlying calendar, such as for determining leap years. Do
not use the result of this method with a calendar other than a
default `GregorianCalendar`.Note: In general, clients should use
`Calendar.get(ZONE_OFFSET) + Calendar.get(DST_OFFSET)`
instead of calling this method.
Specified by:
`getOffset` in class `TimeZone`
Parameters:
`era` - The era of the given date.
`year` - The year in the given date.
`month` - The month in the given date. Month is 0-based. e.g.,
0 for January.
`day` - The day-in-month of the given date.
`dayOfWeek` - The day-of-week of the given date.
`millis` - The milliseconds in day in standard local time.
Returns:
The milliseconds to add to UTC to get local time.
Throws:
`IllegalArgumentException` - the `era`,
`month`, `day`, `dayOfWeek`,
or `millis` parameters are out of range
See Also:
`Calendar.ZONE_OFFSET`,
`Calendar.DST_OFFSET`

