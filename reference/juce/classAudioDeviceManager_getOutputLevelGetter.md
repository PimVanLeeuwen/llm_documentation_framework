#### getOutputLevelGetter()


 LevelMeter::Ptr AudioDeviceManager::getOutputLevelGetter ( ) noexcept 
 

Returns a referencecounted object that can be used to get the current output level.You need to store this object locally to ensure that the reference count is incremented and decremented properly. The current output level value can be read using getCurrentLevel().