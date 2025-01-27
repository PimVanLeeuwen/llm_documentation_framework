#### getLastAccessTime

```
public FileTime getLastAccessTime()
```
Returns the last access time of the entry.The last access time is from the extended timestamp fields
of entry's `optional extra data` when read from a ZIP file
or ZIP file formatted stream.
Returns:
The last access time of the entry, null if not specified
Since:
1.8
See Also:
`setLastAccessTime(FileTime)`

