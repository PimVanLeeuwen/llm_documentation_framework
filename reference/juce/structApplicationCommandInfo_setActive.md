#### setActive()


 void ApplicationCommandInfo::setActive ( bool isActive ) noexcept 
 

An easy way to set or remove the isDisabled bit in the structure's flags field.If isActive is true, the flags member has the isDisabled bit cleared; if isActive is false, the bit is set.