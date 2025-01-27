#### launchWorkerProcess()


 bool ChildProcessCoordinator::launchWorkerProcess ( const File & executableToLaunch, 
 
 const String & commandLineUniqueID, 
 int timeoutMs = 0, 
 int streamFlags = ChildProcess::wantStdOutChildProcess::wantStdErr ) 

Attempts to launch and connect to a worker process.This will start the given executable, passing it a special commandline parameter based around the commandLineUniqueID string, which must be a short alphanumeric string (no spaces!) that identifies your app. The exe that gets launched must respond by calling ChildProcessWorker::initialiseFromCommandLine() in its startup code, and must use a matching ID to commandLineUniqueID.The timeoutMs parameter lets you specify how long the child process is allowed to go without sending a ping before it is considered to have died and handleConnectionLost() will be called. Passing <= 0 for this timeout makes it use a default value.If this all works, the method returns true, and you can begin sending and receiving messages with the worker process.If a child process is already running, this will call killWorkerProcess() and start a new one.