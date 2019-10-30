# College Merch

I recently read a post on reddit where a high school student received over 300 t-shirts by individually emailing over 1,000 colleges. Having taken him over 3 weeks to send all of the emails, I figured there was a better way to approach this.   
**I wrote a script that emails 1,718 colleges asking for merchandise, like t-shirts or pennants, to help promote their school.**

## How to Use

There are two versions of the script depending on the resources you have available on hand: **Server** and **Serverless**

### Server

This version of the script is the recommended use case due to its ability to 'set and forget', but **requires a dedicated linux machine that will always be on** (or on for at least 4 days continuous). This script will send an email every 210 seconds; this is done in order to bypass Gmail's 500 emails per 24 hours rate limit. This method **requires basic knowledge with the linux terminal** to setup. Visit the Server folder for more information.

### Serverless

This version of the script is the most versatile of the two. This script can be run on any platform, but requires manual input. This script is to be manually run once per day, to avoid hitting Gmail's 500 emails per 24 hour rate limit. Every day you run the script, you must modify the script to use a different college list (each college list has approximately 450 college emails). This script will need to be run 4 times with **at least a 24 hour gap between each run**. Visit the Serverless folder for more information.
