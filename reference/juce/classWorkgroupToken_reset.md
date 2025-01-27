#### reset()


 void WorkgroupToken::reset ( ) 
 

If this token was engaged by joining a workgroup, leaves that workgroup and disengages the token.After this call, getTokenProvider() will return nullptr.