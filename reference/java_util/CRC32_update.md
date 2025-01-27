#### update

```
public void update(ByteBuffer buffer)
```
Updates the checksum with the bytes from the specified buffer.
The checksum is updated using
buffer.`remaining()`
bytes starting at
buffer.`position()`
Upon return, the buffer's position will
be updated to its limit; its limit will not have been changed.
Parameters:
`buffer` - the ByteBuffer to update the checksum with
Since:
1.8

