#### getGenericDisplayName

```
public String getGenericDisplayName(String ID,
                                    int style,
                                    Locale locale)
```
Returns a generic name for the given time zone `ID` that's suitable
for presentation to the user in the specified `locale`. Generic
time zone names are neutral from standard time and daylight saving
time. For example, "PT" is the short generic name of time zone ID `America/Los_Angeles`, while its short standard time and daylight saving
time names are "PST" and "PDT", respectively. Refer to
`getDisplayName`
for valid time zone IDs.The default implementation of this method returns `null`.
Parameters:
`ID` - a time zone ID string
`style` - either `TimeZone.LONG` or
`TimeZone.SHORT`
`locale` - the desired locale
Returns:
the human-readable generic name of the given time zone in the
given locale, or `null` if it's not available.
Throws:
`IllegalArgumentException` - if `style` is invalid,
or `locale` isn't one of the locales returned from
`getAvailableLocales()`.
`NullPointerException` - if `ID` or `locale`
is `null`
Since:
1.8




