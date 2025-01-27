#### toResourceName

```
public final String toResourceName(String bundleName,
                                   String suffix)
```
Converts the given `bundleName` to the form required
by the `ClassLoader.getResource`
method by replacing all occurrences of `'.'` in
`bundleName` with `'/'` and appending a
`'.'` and the given file `suffix`. For
example, if `bundleName` is
`"foo.bar.MyResources_ja_JP"` and `suffix`
is `"properties"`, then
`"foo/bar/MyResources_ja_JP.properties"` is returned.
Parameters:
`bundleName` - the bundle name
`suffix` - the file type suffix
Returns:
the converted resource name
Throws:
`NullPointerException` - if `bundleName` or `suffix`
is `null`




