#### getDisplayLanguage

```
public abstract String getDisplayLanguage(String languageCode,
                                          Locale locale)
```
Returns a localized name for the given 
IETF BCP47 language code and the given locale that is appropriate for
display to the user.
For example, if `languageCode` is "fr" and `locale`
is en\_US, getDisplayLanguage() will return "French"; if `languageCode`
is "en" and `locale` is fr\_FR, getDisplayLanguage() will return "anglais".
If the name returned cannot be localized according to `locale`,
(say, the provider does not have a Japanese name for Croatian),
this method returns null.
Parameters:
`languageCode` - the language code string in the form of two to eight
lower-case letters between 'a' (U+0061) and 'z' (U+007A)
`locale` - the desired locale
Returns:
the name of the given language code for the specified locale, or null if it's not
available.
Throws:
`NullPointerException` - if `languageCode` or `locale` is null
`IllegalArgumentException` - if `languageCode` is not in the form of
two or three lower-case letters, or `locale` isn't
one of the locales returned from
`getAvailableLocales()`.
See Also:
`Locale.getDisplayLanguage(java.util.Locale)`

