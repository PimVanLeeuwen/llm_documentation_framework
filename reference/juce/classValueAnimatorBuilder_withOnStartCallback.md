#### withOnStartCallback()


 ValueAnimatorBuilder ValueAnimatorBuilder::withOnStartCallback ( std::function< void()> onStartCallback ) const nodiscard 
 

Use this function to specify an optional on start callback.Alternatively you can use the withOnStartReturningValueChangedCallback function that allows you to return the ValueChangedCallback from inside your on start callback.You can only use either withOnStartCallback() or withOnStartReturningValueChangedCallback().References NullCheckedInvocation::invoke().