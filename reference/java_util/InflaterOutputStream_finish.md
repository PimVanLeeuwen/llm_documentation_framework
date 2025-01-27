#### finish

```
public void finish()
            throws IOException
```
Finishes writing uncompressed data to the output stream without closing
the underlying stream. Use this method when applying multiple filters in
succession to the same output stream.
Throws:
`IOException` - if an I/O error occurs or this stream is already
closed

