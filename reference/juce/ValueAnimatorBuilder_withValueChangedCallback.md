#### withValueChangedCallback()


 ValueAnimatorBuilder ValueAnimatorBuilder::withValueChangedCallback ( ValueChangedCallback valueChangedCallback ) const nodiscard 
 

Use this function to specify an optional on change callback.Alternatively you can use the withOnStartReturningValueChangedCallback function that allows you to return the ValueChangedCallback from inside your on start callback.You can only use either withValueChangedCallback or withOnStartReturningValueChangedCallback.See alsoOnStartReturningValueChangedCallback References NullCheckedInvocation::invoke(), and x.