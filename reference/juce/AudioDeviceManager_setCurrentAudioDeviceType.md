#### setCurrentAudioDeviceType()


 void AudioDeviceManager::setCurrentAudioDeviceType ( const String & type, 
 
 bool treatAsChosenDevice ) 

Changes the class of audio device being used.This switches between, e.g. ASIO and DirectSound. On the Mac you probably won't ever call this because there's only one type: CoreAudio.For a list of types, see getAvailableDeviceTypes().