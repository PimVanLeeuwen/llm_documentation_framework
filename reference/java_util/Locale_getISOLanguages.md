#### getISOLanguages

```
public static String[] getISOLanguages()
```
Returns a list of all 2-letter language codes defined in ISO 639.
Can be used to create Locales.Note:ISO 639 is not a stable standard— some languages' codes have changed.
The list this function returns includes both the new and the old codes for the
languages whose codes have changed.The `Locale` class also supports language codes up to
8 characters in length. Therefore, the list returned by this method does
not contain ALL valid codes that can be used to create Locales.
Returns:
Am array of ISO 639 two-letter language codes.

