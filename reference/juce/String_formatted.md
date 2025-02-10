#### formatted()


template<typename... Args> 

 static String String::formatted ( const String & formatStr, Args... args ) static 
 

Creates a String from a printfstyle parameter list.I don't like this method. I don't use it myself, and I recommend avoiding it and using the operator<< methods or pretty much anything else instead. It's only provided here because of the popular unrest that was stirredup when I tried to remove it...If you're really determined to use it, at least make sure that you never, ever, pass any String objects to it as parameters. And bear in mind that internally, depending on the platform, it may be using wchar\_t or char character types, so that even string literals can't be safely used as parameters if you're writing portable code.