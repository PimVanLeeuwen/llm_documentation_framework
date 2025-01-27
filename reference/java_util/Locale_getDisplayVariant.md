#### getDisplayVariant

```
public String getDisplayVariant(Locale inLocale)
```
Returns a name for the locale's variant code that is appropriate for display to the
user. If possible, the name will be localized for inLocale. If the locale
doesn't specify a variant code, this function returns the empty string.
Parameters:
`inLocale` - The locale for which to retrieve the display variant code.
Returns:
The name of the display variant code appropriate to the given locale.
Throws:
`NullPointerException` - if `inLocale` is `null`

