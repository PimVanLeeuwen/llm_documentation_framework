#### setWeekDate

```
public void setWeekDate(int weekYear,
                        int weekOfYear,
                        int dayOfWeek)
```
Sets the date of this `Calendar` with the the given date
specifiers - week year, week of year, and day of week.Unlike the `set` method, all of the calendar fields
and `time` values are calculated upon return.If `weekOfYear` is out of the valid week-of-year range
in `weekYear`, the `weekYear` and `weekOfYear` values are adjusted in lenient mode, or an `IllegalArgumentException` is thrown in non-lenient mode.The default implementation of this method throws an
`UnsupportedOperationException`.
Parameters:
`weekYear` - the week year
`weekOfYear` - the week number based on `weekYear`
`dayOfWeek` - the day of week value: one of the constants
for the `DAY_OF_WEEK` field: `SUNDAY`, ..., `SATURDAY`.
Throws:
`IllegalArgumentException` - if any of the given date specifiers is invalid
or any of the calendar fields are inconsistent
with the given date specifiers in non-lenient mode
`UnsupportedOperationException` - if any week year numbering isn't supported in this
`Calendar`.
Since:
1.7
See Also:
`isWeekDateSupported()`,
`getFirstDayOfWeek()`,
`getMinimalDaysInFirstWeek()`

