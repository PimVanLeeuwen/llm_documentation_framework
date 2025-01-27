#### getISOCountries

```
public static String[] getISOCountries()
```
Returns a list of all 2-letter country codes defined in ISO 3166.
Can be used to create Locales.Note: The `Locale` class also supports other codes for
country (region), such as 3-letter numeric UN M.49 area codes.
Therefore, the list returned by this method does not contain ALL valid
codes that can be used to create Locales.
Returns:
An array of ISO 3166 two-letter country codes.

