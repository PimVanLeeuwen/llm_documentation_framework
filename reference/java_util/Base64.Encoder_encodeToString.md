#### encodeToString

```
public String encodeToString(byte[] src)
```
Encodes the specified byte array into a String using the `Base64`
encoding scheme.This method first encodes all input bytes into a base64 encoded
byte array and then constructs a new String by using the encoded byte
array and the `ISO-8859-1` charset.In other words, an invocation of this method has exactly the same
effect as invoking
`new String(encode(src), StandardCharsets.ISO_8859_1)`.
Parameters:
`src` - the byte array to encode
Returns:
A String containing the resulting Base64 encoded characters

