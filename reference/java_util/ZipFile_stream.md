#### stream

```
public Stream<? extends ZipEntry> stream()
```
Return an ordered `Stream` over the ZIP file entries.
Entries appear in the `Stream` in the order they appear in
the central directory of the ZIP file.
Returns:
an ordered `Stream` of entries in this ZIP file
Throws:
`IllegalStateException` - if the zip file has been closed
Since:
1.8

