#### run()


 virtual void Thread::run ( ) pure virtual 
 

Must be implemented to perform the thread's actual code.Remember that the thread must regularly check the threadShouldExit() method whilst running, and if this returns true it should return from the run() method as soon as possible to avoid being forcibly killed.See alsothreadShouldExit, startThread