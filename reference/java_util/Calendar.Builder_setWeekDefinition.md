#### setWeekDefinition

```
public Calendar.Builder setWeekDefinition(int firstDayOfWeek,
                                          int minimalDaysInFirstWeek)
```
Sets the week definition parameters to the values given by
`firstDayOfWeek` and `minimalDaysInFirstWeek` that are
used to determine the first
week of a year. The parameters given by this method have
precedence over the default values given by the
locale.
Parameters:
`firstDayOfWeek` - the first day of a week; one of
`Calendar.SUNDAY` to `Calendar.SATURDAY`
`minimalDaysInFirstWeek` - the minimal number of days in the first
week (1..7)
Returns:
this `Calendar.Builder`
Throws:
`IllegalArgumentException` - if `firstDayOfWeek` or
`minimalDaysInFirstWeek` is invalid
See Also:
`Calendar.getFirstDayOfWeek()`,
`Calendar.getMinimalDaysInFirstWeek()`

