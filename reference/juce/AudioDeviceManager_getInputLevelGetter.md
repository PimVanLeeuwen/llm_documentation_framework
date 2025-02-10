#### getInputLevelGetter()


 LevelMeter::Ptr AudioDeviceManager::getInputLevelGetter ( ) noexcept 
 

Returns a referencecounted object that can be used to get the current input level.You need to store this object locally to ensure that the reference count is incremented and decremented properly. The current input level value can be read using getCurrentLevel().