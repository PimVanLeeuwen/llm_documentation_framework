#### toString

```
public final String toString()
```
Returns a string representation of this `Locale`
object, consisting of language, country, variant, script,
and extensions as below:language + "\_" + country + "\_" + (variant + "\_#" | "#") + script + "-" + extensionsLanguage is always lower case, country is always upper case, script is always title
case, and extensions are always lower case. Extensions and private use subtags
will be in canonical order as explained in `toLanguageTag()`.When the locale has neither script nor extensions, the result is the same as in
Java 6 and prior.If both the language and country fields are missing, this function will return
the empty string, even if the variant, script, or extensions field is present (you
can't have a locale with just a variant, the variant must accompany a well-formed
language or country code).If script or extensions are present and variant is missing, no underscore is
added before the "#".This behavior is designed to support debugging and to be compatible with
previous uses of `toString` that expected language, country, and variant
fields only. To represent a Locale as a String for interchange purposes, use
`toLanguageTag()`.Examples:ende\_DE\_GBen\_US\_WINde\_\_POSIXzh\_CN\_#Hanszh\_TW\_#Hant-x-javath\_TH\_TH\_#u-nu-thai
Overrides:
`toString` in class `Object`
Returns:
A string representation of the Locale, for debugging.
See Also:
`getDisplayName()`,
`toLanguageTag()`

