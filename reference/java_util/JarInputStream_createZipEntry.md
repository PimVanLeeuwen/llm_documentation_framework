#### createZipEntry

```
protected ZipEntry createZipEntry(String name)
```
Creates a new `JarEntry` (`ZipEntry`) for the
specified JAR file entry name. The manifest attributes of
the specified JAR file entry name will be copied to the new
`JarEntry`.
Overrides:
`createZipEntry` in class `ZipInputStream`
Parameters:
`name` - the name of the JAR/ZIP file entry
Returns:
the `JarEntry` object just created




