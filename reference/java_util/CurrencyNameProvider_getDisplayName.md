#### getDisplayName

```
public String getDisplayName(String currencyCode,
                             Locale locale)
```
Returns a name for the currency that is appropriate for display to the
user. The default implementation returns null.
Parameters:
`currencyCode` - the ISO 4217 currency code, which
consists of three upper-case letters between 'A' (U+0041) and
'Z' (U+005A)
`locale` - the desired locale
Returns:
the name for the currency that is appropriate for display to the
user, or null if the name is not available for the locale
Throws:
`IllegalArgumentException` - if `currencyCode` is not in
the form of three upper-case letters, or `locale` isn't
one of the locales returned from
`getAvailableLocales()`.
`NullPointerException` - if `currencyCode` or
`locale` is `null`
Since:
1.7




