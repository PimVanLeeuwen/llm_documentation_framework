#### complete

```
protected void complete()
```
Fills in any unset fields in the calendar fields. First, the `computeTime()` method is called if the time value (millisecond offset
from the Epoch) has not been calculated from
calendar field values. Then, the `computeFields()` method is
called to calculate all calendar field values.

