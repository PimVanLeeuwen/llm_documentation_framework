#### initialiseJUCE()


 static void Thread::initialiseJUCE ( void \* jniEnv, void \* jContext ) static 
 

Initialises the JUCE subsystem for projects not created by the Projucer.On Android, JUCE needs to be initialised once before it is used. The Projucer will automatically generate the necessary java code to do this. However, if you are using JUCE without the Projucer or are creating a library made with JUCE intended for use in nonJUCE apks, then you must call this method manually once on apk startup.You can call this method from C++ or directly from java by calling the following java method:com.rmsl.juce.Java.initialiseJUCE (myContext);
Note that the above java method is only available in Android Studio projects created by the Projucer. If you need to call this from another type of project then you need to add the following java file to your project:package com.rmsl.juce;
 
public class Java
{
 static { System.loadLibrary ("juce\_jni"); }
 public native static void initialiseJUCE (Context context);
}
Parameters

 jniEnv this is a pointer to JNI's JNIEnv variable. Any callback from Java into C++ will have this passed in as it's first parameter. 
 
 jContext this is a jobject referring to your app/service/receiver/ provider's Context. JUCE needs this for many of it's internal functions.