#### getDisplayLanguage

```
public String getDisplayLanguage(Locale inLocale)
```
Returns a name for the locale's language that is appropriate for display to the
user.
If possible, the name returned will be localized according to inLocale.
For example, if the locale is fr\_FR and inLocale
is en\_US, getDisplayLanguage() will return "French"; if the locale is en\_US and
inLocale is fr\_FR, getDisplayLanguage() will return "anglais".
If the name returned cannot be localized according to inLocale,
(say, we don't have a Japanese name for Croatian),
this function falls back on the English name, and finally
on the ISO code as a last-resort value. If the locale doesn't specify a language,
this function returns the empty string.
Parameters:
`inLocale` - The locale for which to retrieve the display language.
Returns:
The name of the display language appropriate to the given locale.
Throws:
`NullPointerException` - if `inLocale` is `null`

