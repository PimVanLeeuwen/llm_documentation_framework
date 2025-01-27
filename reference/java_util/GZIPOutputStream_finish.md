#### finish

```
public void finish()
            throws IOException
```
Finishes writing compressed data to the output stream without closing
the underlying stream. Use this method when applying multiple filters
in succession to the same output stream.
Overrides:
`finish` in class `DeflaterOutputStream`
Throws:
`IOException` - if an I/O error has occurred




