#### getMillisecondsSinceLastUpdate()


 int AnimatedAppComponent::getMillisecondsSinceLastUpdate ( ) const noexcept 
 

When called from update(), this returns the number of milliseconds since the last update call.This might be useful for accurately timing animations, etc.