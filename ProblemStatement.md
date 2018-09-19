# Problems

#Question 
I.
1. Use the requests module to download a file from the internet and determine the type of file
(html/pdf/doc/video) downloaded. Assume user provided input URL

2. Suppose if a link is taking more than 1 min to download, it has to be skipped. How would this be
achieved.
3.  How would you determine the size of the file downloaded? Are there multiple ways? what are those?
Is it possible to determine size without actually downloading? If yes, How? Is it always possible?
What are the preconditions in which this will work?
Write the sample solution code for all of above scenarios. Feel free to write functions or files to
capture scenarios.

II.     Question 

Any website requiring login should have a strong password requirements. Following is the criteria for strength:
- At least 1 small case letter
- At least 1 upper case letter
- At least 1 number
- One character from @#$&.
- 6 ≤ length ≤ 12

Accept comma separated passwords as user input and print only strong passwords.

--------------------------------------------------------------------------------------------------------------------------
Answers
--------------------------------------------------------------------------------------------------------------------------

Using the details from the header we can determine the type of file that needs to be downloaded using requests module.

Example header:

```json
{'Date': 'Tue, 18 Sep 2018 03:00:49 GMT', 'Server': 'Apache', 'Last-Modified': 'Fri, 17 Jun 2016 17:43:54 GMT', 'Accept-Ranges': 'bytes', 'Content-Length': '1055736', 'Keep-Alive': 'timeout=5, max=100', 'Connection': 'Keep-Alive', 'Content-Type': 'video
```

2. Skipping or breaking if the download takes 1 minute can be estimated and can be skipped.

3.
The header of a url has a standard type of structure, some have a content-length and some have transfer-encoding .
Content-length : determines the byte length of the request/response body.
Transfer-encoding : data is transmitted in a chunked manner


When content-length is in the header then the time can be estimated,but then also for estimating the time for chunk by chunk the time increases once the downloading starts,so that will be an approximately determined value for the time estimation.





