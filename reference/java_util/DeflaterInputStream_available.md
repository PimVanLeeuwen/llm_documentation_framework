#### available

```
public int available()
              throws IOException
```
Returns 0 after EOF has been reached, otherwise always return 1.Programs should not count on this method to return the actual number
of bytes that could be read without blocking
Overrides:
`available` in class `FilterInputStream`
Returns:
zero after the end of the underlying input stream has been
reached, otherwise always returns 1
Throws:
`IOException` - if an I/O error occurs or if this stream is
already closed

