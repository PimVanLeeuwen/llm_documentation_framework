#### getWeeksInWeekYear

```
public int getWeeksInWeekYear()
```
Returns the number of weeks in the week year
represented by this `GregorianCalendar`.For example, if this `GregorianCalendar`'s date is
December 31, 2008 with the ISO
8601 compatible setting, this method will return 53 for the
period: December 29, 2008 to January 3, 2010 while `getActualMaximum(WEEK_OF_YEAR)` will return
52 for the period: December 31, 2007 to December 28, 2008.
Overrides:
`getWeeksInWeekYear` in class `Calendar`
Returns:
the number of weeks in the week year.
Since:
1.7
See Also:
`Calendar.WEEK_OF_YEAR`,
`getWeekYear()`,
`getActualMaximum(int)`

