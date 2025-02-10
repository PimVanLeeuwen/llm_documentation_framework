#### startRecordingToFile()


 void CameraDevice::startRecordingToFile ( const File & file, 
 
 int quality = 2 ) 

Starts recording video to the specified file.You should use getFileExtension() to find out the correct extension to use for your filename.If the file exists, it will be deleted before the recording starts.This method may not start recording instantly, so if you need to know the exact time at which the file begins, you can call getTimeOfFirstRecordedFrame() after the recording has finished.The quality parameter can be 0, 1, or 2, to indicate low, medium, or high. It may or may not be used, depending on the driver.On Android, before calling startRecordingToFile(), you need to create a preview with createViewerComponent() and you need to make it visible on screen.The Android camera also requires exclusive access to the audio device, so make sure you close any open audio devices with AudioDeviceManager::closeAudioDevice() first.Android does not support simultaneous video recording and still picture capture.See alsoAudioDeviceManager::closeAudioDevice, AudioDeviceManager::restartLastAudioDevice