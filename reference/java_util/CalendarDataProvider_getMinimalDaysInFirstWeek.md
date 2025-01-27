#### getMinimalDaysInFirstWeek

```
public abstract int getMinimalDaysInFirstWeek(Locale locale)
```
Returns the minimal number of days required in the first week of a
year. This information is required by `Calendar` to determine the
first week of a year. Refer to the description of  how `Calendar` determines
the first week.
Parameters:
`locale` - the desired locale
Returns:
the minimal number of days of the first week,
or 0 if the value isn't available for the `locale`
Throws:
`NullPointerException` - if `locale` is `null`.
See Also:
`Calendar.getMinimalDaysInFirstWeek()`




