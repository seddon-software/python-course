# import sys
# import codecs
# from bs4 import os, BeautifulSoup, Tag
# 
# # must be able to locate chromedriver on the PATH
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# os.environ["PATH"] = "." + os.pathsep + os.environ["PATH"]
# 
# # load Chrome
# driver = webdriver.Chrome(executable_path="chromedriver-75")
# 
# driver.get(event)
# 
# # the pages do not load immediately so add implicit delays on all pages 
# driver.implicitly_wait(10) # seconds
# 
# 
# For complete examples and data files, please go to https://github.com/aspose-email/aspose-email-python-dotnet

reader = MboxrdStorageReader(dataDir + "ExampleMbox.mbox", False)


eml = reader.read_next_message()

# Read all messages in a loop
while (eml is not None):

    # Manipulate message - show contents
    print("Subject: " + eml.subject)
    #Save this message in EML or MSG format
    eml.save(eml.subject + "_out.eml", aspose.email.SaveOptions.default_eml)
    eml.save(eml.subject + "_out.msg", aspose.email.SaveOptions.default_msg_unicode)

    # Get the next message
    eml = reader.read_next_message();

# Close the streams
reader.dispose();