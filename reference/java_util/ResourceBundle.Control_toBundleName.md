#### toBundleName

```
public String toBundleName(String baseName,
                           Locale locale)
```
Converts the given `baseName` and `locale`
to the bundle name. This method is called from the default
implementation of the `newBundle` and `needsReload`
methods.This implementation returns the following value:
```

     baseName + "_" + language + "_" + script + "_" + country + "_" + variant
 
```
where `language`, `script`, `country`,
and `variant` are the language, script, country, and variant
values of `locale`, respectively. Final component values that
are empty Strings are omitted along with the preceding '\_'. When the
script is empty, the script value is omitted along with the preceding '\_'.
If all of the values are empty strings, then `baseName`
is returned.For example, if `baseName` is
`"baseName"` and `locale` is
`Locale("ja", "", "XX")`, then
`"baseName_ja_ _XX"` is returned. If the given
locale is `Locale("en")`, then
`"baseName_en"` is returned.Overriding this method allows applications to use different
conventions in the organization and packaging of localized
resources.
Parameters:
`baseName` - the base name of the resource bundle, a fully
qualified class name
`locale` - the locale for which a resource bundle should be
loaded
Returns:
the bundle name for the resource bundle
Throws:
`NullPointerException` - if `baseName` or `locale`
is `null`

