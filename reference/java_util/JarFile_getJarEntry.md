#### getJarEntry

```
public JarEntry getJarEntry(String name)
```
Returns the `JarEntry` for the given entry name or
`null` if not found.
Parameters:
`name` - the jar file entry name
Returns:
the `JarEntry` for the given entry name or
`null` if not found.
Throws:
`IllegalStateException` - may be thrown if the jar file has been closed
See Also:
`JarEntry`

