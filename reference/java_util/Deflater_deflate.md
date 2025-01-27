#### deflate

```
public int deflate(byte[] b,
                   int off,
                   int len,
                   int flush)
```
Compresses the input data and fills the specified buffer with compressed
data. Returns actual number of bytes of data compressed.Compression flush mode is one of the following three modes:`NO_FLUSH`: allows the deflater to decide how much data
to accumulate, before producing output, in order to achieve the best
compression (should be used in normal use scenario). A return value
of 0 in this flush mode indicates that `needsInput()` should
be called in order to determine if more input data is required.`SYNC_FLUSH`: all pending output in the deflater is flushed,
to the specified output buffer, so that an inflater that works on
compressed data can get all input data available so far (In particular
the `needsInput()` returns `true` after this invocation
if enough output space is provided). Flushing with `SYNC_FLUSH`
may degrade compression for some compression algorithms and so it
should be used only when necessary.`FULL_FLUSH`: all pending output is flushed out as with
`SYNC_FLUSH`. The compression state is reset so that the inflater
that works on the compressed output data can restart from this point
if previous compressed data has been damaged or if random access is
desired. Using `FULL_FLUSH` too often can seriously degrade
compression.In the case of `FULL_FLUSH` or `SYNC_FLUSH`, if
the return value is `len`, the space available in output
buffer `b`, this method should be invoked again with the same
`flush` parameter and more output space.
Parameters:
`b` - the buffer for the compressed data
`off` - the start offset of the data
`len` - the maximum number of bytes of compressed data
`flush` - the compression flush mode
Returns:
the actual number of bytes of compressed data written to
the output buffer
Throws:
`IllegalArgumentException` - if the flush mode is invalid
Since:
1.7

