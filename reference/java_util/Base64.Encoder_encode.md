#### encode

```
public ByteBuffer encode(ByteBuffer buffer)
```
Encodes all remaining bytes from the specified byte buffer into
a newly-allocated ByteBuffer using the `Base64` encoding
scheme.
Upon return, the source buffer's position will be updated to
its limit; its limit will not have been changed. The returned
output buffer's position will be zero and its limit will be the
number of resulting encoded bytes.
Parameters:
`buffer` - the source ByteBuffer to encode
Returns:
A newly-allocated byte buffer containing the encoded bytes.

