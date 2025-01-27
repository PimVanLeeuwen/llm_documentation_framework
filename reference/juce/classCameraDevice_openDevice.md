#### openDevice()


 static CameraDevice \* CameraDevice::openDevice ( int deviceIndex, int minWidth = 128, int minHeight = 64, int maxWidth = 1024, int maxHeight = 768, bool highQuality = true ) static 
 

Synchronously opens a camera device.This function should not be used on iOS or Android, use openDeviceAsync() instead.The index parameter indicates which of the items returned by getAvailableDevices() to open.The size constraints allow the method to choose between different resolutions if the camera supports this. If the resolution can't be specified (e.g. on the Mac) then these will be ignored.On Mac, if highQuality is false, then the camera will be opened in preview mode which will allow the OS to drop frames if the computer cannot keep up in processing the frames.