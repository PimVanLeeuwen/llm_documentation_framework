#### flush

```
public void flush()
           throws IOException
```
Flushes the compressed output stream.
If `syncFlush` is `true` when this compressed output stream is
constructed, this method first flushes the underlying `compressor`
with the flush mode `Deflater.SYNC_FLUSH` to force
all pending data to be flushed out to the output stream and then
flushes the output stream. Otherwise this method only flushes the
output stream without flushing the `compressor`.
Specified by:
`flush` in interface `Flushable`
Overrides:
`flush` in class `FilterOutputStream`
Throws:
`IOException` - if an I/O error has occurred
Since:
1.7
See Also:
`FilterOutputStream.out`




