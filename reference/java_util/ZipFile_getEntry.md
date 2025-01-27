#### getEntry

```
public ZipEntry getEntry(String name)
```
Returns the zip file entry for the specified name, or null
if not found.
Parameters:
`name` - the name of the entry
Returns:
the zip file entry, or null if not found
Throws:
`IllegalStateException` - if the zip file has been closed

