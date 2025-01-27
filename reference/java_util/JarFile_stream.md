#### stream

```
public Stream<JarEntry> stream()
```
Description copied from class: `ZipFile`
Return an ordered `Stream` over the ZIP file entries.
Entries appear in the `Stream` in the order they appear in
the central directory of the ZIP file.
Overrides:
`stream` in class `ZipFile`
Returns:
an ordered `Stream` of entries in this ZIP file

