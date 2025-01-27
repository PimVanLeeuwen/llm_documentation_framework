#### getAvailableLocales

```
public abstract Locale[] getAvailableLocales()
```
Returns an array of all locales for which this locale service provider
can provide localized objects or names. This information is used to
compose `getAvailableLocales()` values of the locale-dependent
services, such as `DateFormat.getAvailableLocales()`.The array returned by this method should not include two or more
`Locale` objects only differing in their extensions.
Returns:
An array of all locales for which this locale service provider
can provide localized objects or names.

