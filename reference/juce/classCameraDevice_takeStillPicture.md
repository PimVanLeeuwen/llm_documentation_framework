#### takeStillPicture()


 void CameraDevice::takeStillPicture ( std::function< void(const Image &)> pictureTakenCallback ) 
 

Triggers a still picture capture.Upon completion, pictureTakenCallback will be invoked on a message thread.On Android, before calling takeStillPicture(), you need to create a preview with createViewerComponent() and you need to make it visible on screen.Android does not support simultaneous video recording and still picture capture.