```
public class Adler32
extends Object
implements Checksum
```
A class that can be used to compute the Adler-32 checksum of a data
stream. An Adler-32 checksum is almost as reliable as a CRC-32 but
can be computed much faster.Passing a `null` argument to a method in this class will cause
a `NullPointerException` to be thrown.
See Also:
`Checksum`
