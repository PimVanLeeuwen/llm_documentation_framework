#### newBundle

```
public ResourceBundle newBundle(String baseName,
                                Locale locale,
                                String format,
                                ClassLoader loader,
                                boolean reload)
                         throws IllegalAccessException,
                                InstantiationException,
                                IOException
```
Instantiates a resource bundle for the given bundle name of the
given format and locale, using the given class loader if
necessary. This method returns `null` if there is no
resource bundle available for the given parameters. If a resource
bundle can't be instantiated due to an unexpected error, the
error must be reported by throwing an `Error` or
`Exception` rather than simply returning
`null`.If the `reload` flag is `true`, it
indicates that this method is being called because the previously
loaded resource bundle has expired.The default implementation instantiates a
`ResourceBundle` as follows.The bundle name is obtained by calling `toBundleName(baseName,
locale)`.If `format` is `"java.class"`, the
`Class` specified by the bundle name is loaded by calling
`ClassLoader.loadClass(String)`. Then, a
`ResourceBundle` is instantiated by calling `Class.newInstance()`. Note that the `reload` flag is
ignored for loading class-based resource bundles in this default
implementation.If `format` is `"java.properties"`,
`toResourceName(bundlename,
"properties")` is called to get the resource name.
If `reload` is `true`, `load.getResource` is called
to get a `URL` for creating a `URLConnection`. This `URLConnection` is used to
disable the
caches of the underlying resource loading layers,
and to get an
`InputStream`.
Otherwise, `loader.getResourceAsStream` is called to get an `InputStream`. Then, a `PropertyResourceBundle` is constructed with the
`InputStream`.If `format` is neither `"java.class"`
nor `"java.properties"`, an
`IllegalArgumentException` is thrown.
Parameters:
`baseName` - the base bundle name of the resource bundle, a fully
qualified class name
`locale` - the locale for which the resource bundle should be
instantiated
`format` - the resource bundle format to be loaded
`loader` - the `ClassLoader` to use to load the bundle
`reload` - the flag to indicate bundle reloading; `true`
if reloading an expired resource bundle,
`false` otherwise
Returns:
the resource bundle instance,
or `null` if none could be found.
Throws:
`NullPointerException` - if `bundleName`, `locale`,
`format`, or `loader` is
`null`, or if `null` is returned by
`toBundleName`
`IllegalArgumentException` - if `format` is unknown, or if the resource
found for the given parameters contains malformed data.
`ClassCastException` - if the loaded class cannot be cast to `ResourceBundle`
`IllegalAccessException` - if the class or its nullary constructor is not
accessible.
`InstantiationException` - if the instantiation of a class fails for some other
reason.
`ExceptionInInitializerError` - if the initialization provoked by this method fails.
`SecurityException` - If a security manager is present and creation of new
instances is denied. See `Class.newInstance()`
for details.
`IOException` - if an error occurred when reading resources using
any I/O operations

