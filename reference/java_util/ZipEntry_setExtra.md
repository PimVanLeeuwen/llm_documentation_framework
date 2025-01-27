#### setExtra

```
public void setExtra(byte[] extra)
```
Sets the optional extra field data for the entry.Invoking this method may change this entry's last modification
time, last access time and creation time, if the `extra` field
data includes the extensible timestamp fields, such as `NTFS tag
0x0001` or `Info-ZIP Extended Timestamp`, as specified in
Info-ZIP
Application Note 970311.
Parameters:
`extra` - The extra field data bytes
Throws:
`IllegalArgumentException` - if the length of the specified
extra field data is greater than 0xFFFF bytes
See Also:
`getExtra()`

