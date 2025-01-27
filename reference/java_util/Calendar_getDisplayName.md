#### getDisplayName

```
public String getDisplayName(int field,
                             int style,
                             Locale locale)
```
Returns the string representation of the calendar
`field` value in the given `style` and
`locale`. If no string representation is
applicable, `null` is returned. This method calls
`get(field)` to get the calendar
`field` value if the string representation is
applicable to the given calendar `field`.For example, if this `Calendar` is a
`GregorianCalendar` and its date is 2005-01-01, then
the string representation of the `MONTH` field would be
"January" in the long style in an English locale or "Jan" in
the short style. However, no string representation would be
available for the `DAY_OF_MONTH` field, and this method
would return `null`.The default implementation supports the calendar fields for
which a `DateFormatSymbols` has names in the given
`locale`.
Parameters:
`field` - the calendar field for which the string representation
is returned
`style` - the style applied to the string representation; one of `SHORT_FORMAT` (`SHORT`), `SHORT_STANDALONE`,
`LONG_FORMAT` (`LONG`), `LONG_STANDALONE`,
`NARROW_FORMAT`, or `NARROW_STANDALONE`.
`locale` - the locale for the string representation
(any calendar types specified by `locale` are ignored)
Returns:
the string representation of the given
`field` in the given `style`, or
`null` if no string representation is
applicable.
Throws:
`IllegalArgumentException` - if `field` or `style` is invalid,
or if this `Calendar` is non-lenient and any
of the calendar fields have invalid values
`NullPointerException` - if `locale` is null
Since:
1.6

