#### getSymbol

```
public abstract String getSymbol(String currencyCode,
                                 Locale locale)
```
Gets the symbol of the given currency code for the specified locale.
For example, for "USD" (US Dollar), the symbol is "$" if the specified
locale is the US, while for other locales it may be "US$". If no
symbol can be determined, null should be returned.
Parameters:
`currencyCode` - the ISO 4217 currency code, which
consists of three upper-case letters between 'A' (U+0041) and
'Z' (U+005A)
`locale` - the desired locale
Returns:
the symbol of the given currency code for the specified locale, or null if
the symbol is not available for the locale
Throws:
`NullPointerException` - if `currencyCode` or
`locale` is null
`IllegalArgumentException` - if `currencyCode` is not in
the form of three upper-case letters, or `locale` isn't
one of the locales returned from
`getAvailableLocales()`.
See Also:
`Currency.getSymbol(java.util.Locale)`

