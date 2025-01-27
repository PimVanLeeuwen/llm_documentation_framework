#### getActualMaximum

```
public int getActualMaximum(int field)
```
Returns the maximum value that this calendar field could have,
taking into consideration the given time value and the current
values of the
`getFirstDayOfWeek`,
`getMinimalDaysInFirstWeek`,
`getGregorianChange` and
`getTimeZone` methods.
For example, if the date of this instance is February 1, 2004,
the actual maximum value of the `DAY_OF_MONTH` field
is 29 because 2004 is a leap year, and if the date of this
instance is February 1, 2005, it's 28.This method calculates the maximum value of `WEEK_OF_YEAR` based on the `YEAR` (calendar year) value, not the week year. Call `getWeeksInWeekYear()` to get the maximum value of `WEEK_OF_YEAR` in the week year of this `GregorianCalendar`.
Overrides:
`getActualMaximum` in class `Calendar`
Parameters:
`field` - the calendar field
Returns:
the maximum of the given field for the time value of
this `GregorianCalendar`
Since:
1.2
See Also:
`getMinimum(int)`,
`getMaximum(int)`,
`getGreatestMinimum(int)`,
`getLeastMaximum(int)`,
`getActualMinimum(int)`

