#### getManifest

```
public Manifest getManifest()
                     throws IOException
```
Returns the jar file manifest, or `null` if none.
Returns:
the jar file manifest, or `null` if none
Throws:
`IllegalStateException` - may be thrown if the jar file has been closed
`IOException` - if an I/O error has occurred

