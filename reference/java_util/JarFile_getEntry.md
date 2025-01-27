#### getEntry

```
public ZipEntry getEntry(String name)
```
Returns the `ZipEntry` for the given entry name or
`null` if not found.
Overrides:
`getEntry` in class `ZipFile`
Parameters:
`name` - the jar file entry name
Returns:
the `ZipEntry` for the given entry name or
`null` if not found
Throws:
`IllegalStateException` - may be thrown if the jar file has been closed
See Also:
`ZipEntry`

