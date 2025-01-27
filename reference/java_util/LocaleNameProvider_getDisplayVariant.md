#### getDisplayVariant

```
public abstract String getDisplayVariant(String variant,
                                         Locale locale)
```
Returns a localized name for the given variant code and the given locale that
is appropriate for display to the user.
If the name returned cannot be localized according to `locale`,
this method returns null.
Parameters:
`variant` - the variant string
`locale` - the desired locale
Returns:
the name of the given variant string for the specified locale, or null if it's not
available.
Throws:
`NullPointerException` - if `variant` or `locale` is null
`IllegalArgumentException` - if `locale` isn't
one of the locales returned from
`getAvailableLocales()`.
See Also:
`Locale.getDisplayVariant(java.util.Locale)`




