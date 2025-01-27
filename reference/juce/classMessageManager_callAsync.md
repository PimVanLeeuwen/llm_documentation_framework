#### callAsync()


 static bool MessageManager::callAsync ( std::function< void()> functionToCall ) static 
 

Asynchronously invokes a function or C++11 lambda on the message thread.Returnstrue if the message was successfully posted to the message queue, or false otherwise.