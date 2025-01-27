#### getDisplayName

```
public abstract String getDisplayName(String ID,
                                      boolean daylight,
                                      int style,
                                      Locale locale)
```
Returns a name for the given time zone ID that's suitable for
presentation to the user in the specified locale. The given time
zone ID is "GMT" or one of the names defined using "Zone" entries
in the "tz database", a public domain time zone database at
ftp://elsie.nci.nih.gov/pub/.
The data of this database is contained in a file whose name starts with
"tzdata", and the specification of the data format is part of the zic.8
man page, which is contained in a file whose name starts with "tzcode".If `daylight` is true, the method should return a name
appropriate for daylight saving time even if the specified time zone
has not observed daylight saving time in the past.
Parameters:
`ID` - a time zone ID string
`daylight` - if true, return the daylight saving name.
`style` - either `TimeZone.LONG` or
`TimeZone.SHORT`
`locale` - the desired locale
Returns:
the human-readable name of the given time zone in the
given locale, or null if it's not available.
Throws:
`IllegalArgumentException` - if `style` is invalid,
or `locale` isn't one of the locales returned from
`getAvailableLocales()`.
`NullPointerException` - if `ID` or `locale`
is null
See Also:
`TimeZone.getDisplayName(boolean, int, java.util.Locale)`

