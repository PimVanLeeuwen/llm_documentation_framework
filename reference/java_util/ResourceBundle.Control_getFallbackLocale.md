#### getFallbackLocale

```
public Locale getFallbackLocale(String baseName,
                                Locale locale)
```
Returns a `Locale` to be used as a fallback locale for
further resource bundle searches by the
`ResourceBundle.getBundle` factory method. This method
is called from the factory method every time when no resulting
resource bundle has been found for `baseName` and
`locale`, where locale is either the parameter for
`ResourceBundle.getBundle` or the previous fallback
locale returned by this method.The method returns `null` if no further fallback
search is desired.The default implementation returns the default `Locale` if the given
`locale` isn't the default one. Otherwise,
`null` is returned.
Parameters:
`baseName` - the base name of the resource bundle, a fully
qualified class name for which
`ResourceBundle.getBundle` has been
unable to find any resource bundles (except for the
base bundle)
`locale` - the `Locale` for which
`ResourceBundle.getBundle` has been
unable to find any resource bundles (except for the
base bundle)
Returns:
a `Locale` for the fallback search,
or `null` if no further fallback search
is desired.
Throws:
`NullPointerException` - if `baseName` or `locale`
is `null`

