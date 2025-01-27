#### setLocale

```
public Calendar.Builder setLocale(Locale locale)
```
Sets the locale parameter to the given `locale`. If no locale
is given to this `Calendar.Builder`, the default `Locale`
for `Locale.Category.FORMAT` will be used.If no calendar type is explicitly given by a call to the
`setCalendarType` method,
the `Locale` value is used to determine what type of
`Calendar` to be built.If no week definition parameters are explicitly given by a call to
the `setWeekDefinition` method, the
`Locale`'s default values are used.
Parameters:
`locale` - the `Locale`
Returns:
this `Calendar.Builder`
Throws:
`NullPointerException` - if `locale` is `null`
See Also:
`Calendar.getInstance(Locale)`

