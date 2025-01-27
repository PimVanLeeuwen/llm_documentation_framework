#### launch() [2/2]


 static bool Thread::launch ( Priority priority, std::function< void()> functionToRun ) static 
 

Invokes a lambda or function on its own thread with a custom priority.This will spin up a Thread object which calls the function and then exits. Bear in mind that starting and stopping a thread can be a fairly heavyweight operation, so you might prefer to use a ThreadPool if you're kicking off a lot of short background tasks.Also note that using an anonymous thread makes it very difficult to interrupt the function when you need to stop it, e.g. when your app quits. So it's up to you to deal with situations where the function may fail to stop in time.Parameters

 priority The priority the thread is started with. 
 
 functionToRun The lambda to be called from the new Thread. 



Returnstrue if the thread started successfully, or false if it failed.