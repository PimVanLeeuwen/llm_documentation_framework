#### operator=()


 ErasedScopeGuard & ErasedScopeGuard::operator= ( ErasedScopeGuard && other ) noexcept 
 

Calls the stored callback, if any, then assumes responsibility for calling other's callback.After this call, other will be reset to its default state.