#### getWeekYear

```
public int getWeekYear()
```
Returns the week year represented by this `Calendar`. The
week year is in sync with the week cycle. The first day of the first week is the first
day of the week year.The default implementation of this method throws an
`UnsupportedOperationException`.
Returns:
the week year of this `Calendar`
Throws:
`UnsupportedOperationException` - if any week year numbering isn't supported
in this `Calendar`.
Since:
1.7
See Also:
`isWeekDateSupported()`,
`getFirstDayOfWeek()`,
`getMinimalDaysInFirstWeek()`

