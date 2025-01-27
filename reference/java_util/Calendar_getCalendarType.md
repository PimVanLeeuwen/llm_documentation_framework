#### getCalendarType

```
public String getCalendarType()
```
Returns the calendar type of this `Calendar`. Calendar types are
defined by the Unicode Locale Data Markup Language (LDML)
specification.The default implementation of this method returns the class name of
this `Calendar` instance. Any subclasses that implement
LDML-defined calendar systems should override this method to return
appropriate calendar types.
Returns:
the LDML-defined calendar type or the class name of this
`Calendar` instance
Since:
1.8
See Also:
Locale extensions,
`Locale.Builder.setLocale(Locale)`,
`Locale.Builder.setUnicodeLocaleKeyword(String, String)`

