#### isSupportedLocale

```
public boolean isSupportedLocale(Locale locale)
```
Returns `true` if the given `locale` is supported by
this locale service provider. The given `locale` may contain
extensions that should be
taken into account for the support determination.The default implementation returns `true` if the given `locale`
is equal to any of the available `Locale`s returned by
`getAvailableLocales()` with ignoring any extensions in both the
given `locale` and the available locales. Concrete locale service
provider implementations should override this method if those
implementations are `Locale` extensions-aware. For example,
`DecimalFormatSymbolsProvider` implementations will need to check
extensions in the given `locale` to see if any numbering system is
specified and can be supported. However, `CollatorProvider`
implementations may not be affected by any particular numbering systems,
and in that case, extensions for numbering systems should be ignored.
Parameters:
`locale` - a `Locale` to be tested
Returns:
`true` if the given `locale` is supported by this
provider; `false` otherwise.
Throws:
`NullPointerException` - if the given `locale` is `null`
Since:
1.8
See Also:
`Locale.hasExtensions()`,
`Locale.stripExtensions()`




