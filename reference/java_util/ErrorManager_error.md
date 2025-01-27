#### error

```
public void error(String msg,
                  Exception ex,
                  int code)
```
The error method is called when a Handler failure occurs.This method may be overridden in subclasses. The default
behavior in this base class is that the first call is
reported to System.err, and subsequent calls are ignored.
Parameters:
`msg` - a descriptive string (may be null)
`ex` - an exception (may be null)
`code` - an error code defined in ErrorManager




