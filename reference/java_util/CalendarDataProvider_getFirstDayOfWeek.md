#### getFirstDayOfWeek

```
public abstract int getFirstDayOfWeek(Locale locale)
```
Returns the first day of a week in the given `locale`. This
information is required by `Calendar` to support operations on the
week-related calendar fields.
Parameters:
`locale` - the desired locale
Returns:
the first day of a week; one of `Calendar.SUNDAY` ..
`Calendar.SATURDAY`,
or 0 if the value isn't available for the `locale`
Throws:
`NullPointerException` - if `locale` is `null`.
See Also:
`Calendar.getFirstDayOfWeek()`,
First Week

