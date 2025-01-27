#### getDisplayName

```
public String getDisplayName(Locale inLocale)
```
Returns a name for the locale that is appropriate for display
to the user. This will be the values returned by
getDisplayLanguage(), getDisplayScript(),getDisplayCountry(),
and getDisplayVariant() assembled into a single string.
The non-empty values are used in order,
with the second and subsequent names in parentheses. For example:language (script, country, variant)
language (country)
language (variant)
script (country)
countrydepending on which fields are specified in the locale. If the
language, script, country, and variant fields are all empty,
this function returns the empty string.
Parameters:
`inLocale` - The locale for which to retrieve the display name.
Returns:
The name of the locale appropriate to display.
Throws:
`NullPointerException` - if `inLocale` is `null`

