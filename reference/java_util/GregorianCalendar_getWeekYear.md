#### getWeekYear

```
public int getWeekYear()
```
Returns the week year represented by this
`GregorianCalendar`. The dates in the weeks between 1 and the
maximum week number of the week year have the same week year value
that may be one year before or after the `YEAR`
(calendar year) value.This method calls `Calendar.complete()` before
calculating the week year.
Overrides:
`getWeekYear` in class `Calendar`
Returns:
the week year represented by this `GregorianCalendar`.
If the `ERA` value is `BC`, the year is
represented by 0 or a negative number: BC 1 is 0, BC 2
is -1, BC 3 is -2, and so on.
Throws:
`IllegalArgumentException` - if any of the calendar fields is invalid in non-lenient mode.
Since:
1.7
See Also:
`isWeekDateSupported()`,
`getWeeksInWeekYear()`,
`Calendar.getFirstDayOfWeek()`,
`Calendar.getMinimalDaysInFirstWeek()`

