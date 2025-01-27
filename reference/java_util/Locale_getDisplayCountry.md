#### getDisplayCountry

```
public String getDisplayCountry(Locale inLocale)
```
Returns a name for the locale's country that is appropriate for display to the
user.
If possible, the name returned will be localized according to inLocale.
For example, if the locale is fr\_FR and inLocale
is en\_US, getDisplayCountry() will return "France"; if the locale is en\_US and
inLocale is fr\_FR, getDisplayCountry() will return "Etats-Unis".
If the name returned cannot be localized according to inLocale.
(say, we don't have a Japanese name for Croatia),
this function falls back on the English name, and finally
on the ISO code as a last-resort value. If the locale doesn't specify a country,
this function returns the empty string.
Parameters:
`inLocale` - The locale for which to retrieve the display country.
Returns:
The name of the country appropriate to the given locale.
Throws:
`NullPointerException` - if `inLocale` is `null`

