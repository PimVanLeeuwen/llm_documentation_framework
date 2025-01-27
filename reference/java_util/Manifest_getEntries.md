#### getEntries

```
public Map<String,Attributes> getEntries()
```
Returns a Map of the entries contained in this Manifest. Each entry
is represented by a String name (key) and associated Attributes (value).
The Map permits the `null` key, but no entry with a null key is
created by `read(java.io.InputStream)`, nor is such an entry written by using `write(java.io.OutputStream)`.
Returns:
a Map of the entries contained in this Manifest

