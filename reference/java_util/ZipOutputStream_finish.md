#### finish

```
public void finish()
            throws IOException
```
Finishes writing the contents of the ZIP output stream without closing
the underlying stream. Use this method when applying multiple filters
in succession to the same output stream.
Overrides:
`finish` in class `DeflaterOutputStream`
Throws:
`ZipException` - if a ZIP file error has occurred
`IOException` - if an I/O exception has occurred

