```
public class ErrorManager
extends Object
```
ErrorManager objects can be attached to Handlers to process
any error that occurs on a Handler during Logging.When processing logging output, if a Handler encounters problems
then rather than throwing an Exception back to the issuer of
the logging call (who is unlikely to be interested) the Handler
should call its associated ErrorManager.
