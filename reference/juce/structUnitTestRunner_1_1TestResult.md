Contains the results of a test.One of these objects is instantiated each time UnitTest::beginTest() is called, and it contains details of the number of subsequent UnitTest::expect() calls that are made.

Constructor & Destructor Documentation


◆ TestResult() [1/2]


 UnitTestRunner::TestResult::TestResult ( ) default 
 



◆ TestResult() [2/2]


 UnitTestRunner::TestResult::TestResult ( const String & name, const String & subCategory ) explicit 
 


Member Data Documentation


◆ unitTestName


 String UnitTestRunner::TestResult::unitTestName 
 

The main name of this test (i.e.the name of the UnitTest object being run).

◆ subcategoryName


 String UnitTestRunner::TestResult::subcategoryName 
 

The name of the current subcategory (i.e.the name that was set when UnitTest::beginTest() was called).

◆ passes


 int UnitTestRunner::TestResult::passes = 0 
 

The number of UnitTest::expect() calls that succeeded.

◆ failures


 int UnitTestRunner::TestResult::failures = 0 
 

The number of UnitTest::expect() calls that failed.

◆ messages


 StringArray UnitTestRunner::TestResult::messages 
 

A list of messages describing the failed tests.

◆ startTime


 Time UnitTestRunner::TestResult::startTime = Time::getCurrentTime() 
 

The time at which this test was started.

◆ endTime


 Time UnitTestRunner::TestResult::endTime 
 

The time at which this test ended.

The documentation for this struct was generated from the following file:juce\_UnitTest.h
### Purchase

Get JUCE
### Discover

What's New in JUCEFeatures
### Learn

DocumentaionTutorialsMade with JUCEResources
### Support

JUCE ForumNewsletterArchive
### About

Contact UsJUCE LegalJUCE Licensing FAQ
### Events

Audio Developer Conference
Visit our FacebookVisit our TwitterVisit our LinkedInVisit our YouTube channel© Raw Material Software Limited
linkedin




facebook


pinterest


youtube


rss


twitter


instagram




facebookblank


rssblank


linkedinblank


pinterest


youtube


twitter


instagram