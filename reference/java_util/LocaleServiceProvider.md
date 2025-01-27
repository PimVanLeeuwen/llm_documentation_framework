```
public abstract class LocaleServiceProvider
extends Object
```
This is the super class of all the locale sensitive service provider
interfaces (SPIs).Locale sensitive service provider interfaces are interfaces that
correspond to locale sensitive classes in the `java.text`
and `java.util` packages. The interfaces enable the
construction of locale sensitive objects and the retrieval of
localized names for these packages. Locale sensitive factory methods
and methods for name retrieval in the `java.text` and
`java.util` packages use implementations of the provider
interfaces to offer support for locales beyond the set of locales
supported by the Java runtime environment itself.