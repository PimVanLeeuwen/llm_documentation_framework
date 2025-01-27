#### join()


 void AudioWorkgroup::join ( WorkgroupToken & token ) const 
 

This method attempts to join the calling thread to this workgroup.If the join operation is successful, the token will be engaged, i.e. its getTokenProvider() function will return nonnull.If the token is already engaged and represents a join to another workgroup, the thread will leave that workgroup before joining the workgroup represented by this object. If the 'token' is already engaged and is passed to the same workgroup, the method will not perform any action.It's important to note that the lifetime of the token should not exceed the lifetime of the associated thread and must be destroyed on the same thread.