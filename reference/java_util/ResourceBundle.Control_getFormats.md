#### getFormats

```
public List<String> getFormats(String baseName)
```
Returns a `List` of `String`s containing
formats to be used to load resource bundles for the given
`baseName`. The `ResourceBundle.getBundle`
factory method tries to load resource bundles with formats in the
order specified by the list. The list returned by this method
must have at least one `String`. The predefined
formats are `"java.class"` for class-based resource
bundles and `"java.properties"` for properties-based ones. Strings starting
with `"java."` are reserved for future extensions and
must not be used by application-defined formats.It is not a requirement to return an immutable (unmodifiable)
`List`. However, the returned `List` must
not be mutated after it has been returned by
`getFormats`.The default implementation returns `FORMAT_DEFAULT` so
that the `ResourceBundle.getBundle` factory method
looks up first class-based resource bundles, then
properties-based ones.
Parameters:
`baseName` - the base name of the resource bundle, a fully qualified class
name
Returns:
a `List` of `String`s containing
formats for loading resource bundles.
Throws:
`NullPointerException` - if `baseName` is null
See Also:
`FORMAT_DEFAULT`,
`FORMAT_CLASS`,
`FORMAT_PROPERTIES`

