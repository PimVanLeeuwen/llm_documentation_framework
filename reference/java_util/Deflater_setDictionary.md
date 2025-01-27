#### setDictionary

```
public void setDictionary(byte[] b)
```
Sets preset dictionary for compression. A preset dictionary is used
when the history buffer can be predetermined. When the data is later
uncompressed with Inflater.inflate(), Inflater.getAdler() can be called
in order to get the Adler-32 value of the dictionary required for
decompression.
Parameters:
`b` - the dictionary data bytes
See Also:
`Inflater.inflate(byte[], int, int)`,
`Inflater.getAdler()`

