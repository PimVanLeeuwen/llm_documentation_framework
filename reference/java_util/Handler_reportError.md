#### reportError

```
protected void reportError(String msg,
                           Exception ex,
                           int code)
```
Protected convenience method to report an error to this Handler's
ErrorManager. Note that this method retrieves and uses the ErrorManager
without doing a security check. It can therefore be used in
environments where the caller may be non-privileged.
Parameters:
`msg` - a descriptive string (may be null)
`ex` - an exception (may be null)
`code` - an error code defined in ErrorManager

