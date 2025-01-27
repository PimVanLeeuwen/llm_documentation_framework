#### withOnStartReturningValueChangedCallback()


 ValueAnimatorBuilder ValueAnimatorBuilder::withOnStartReturningValueChangedCallback ( OnStartReturningValueChangedCallback value ) const nodiscard 
 

Use this function to specify an optional on start callback.The return value of the provided function is a ValueChangedCallback. This allows you to construct a new ValueChangedCallback on every on start event, capturing state that is also constructed at the time of starting.If you don't need to return a new ValueChangedCallback on every animation start, you can use the simpler variants withOnStartCallback and withValueChangedCallback. However you cannot use those functions together with this one.See alsoOnStartReturningValueChangedCallback, withOnStartCallback, withValueChangedCallback