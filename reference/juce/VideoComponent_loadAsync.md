#### loadAsync()


 void VideoComponent::loadAsync ( const URL & url, 
 
 std::function< void(const URL &, Result)> loadFinishedCallback ) 

Tries to load a video from a URL asynchronously.When finished, invokes the callback supplied to the function on the message thread.This is the preferred way of loading content, since it works not only on macOS and Windows, but also on iOS and Android. On Windows, it will internally call load().See alsoload