#### wrap

```
public OutputStream wrap(OutputStream os)
```
Wraps an output stream for encoding byte data using the `Base64`
encoding scheme.It is recommended to promptly close the returned output stream after
use, during which it will flush all possible leftover bytes to the underlying
output stream. Closing the returned output stream will close the underlying
output stream.
Parameters:
`os` - the output stream.
Returns:
the output stream for encoding the byte data into the
specified Base64 encoded format

