![image](https://github.com/1nv1sibl3/OS-CTF/assets/120787381/cb58fdfa-99dd-41e1-bf85-83d7a0edb1f5)

At this question, you will find this is a PKZIP file. Use zip2john to take the file hash and crack the password by using john

![image](https://github.com/1nv1sibl3/OS-CTF/assets/120787381/989a82fa-ba24-46fe-93ca-91d25232c4c6)

Then you will have a docx file

![image](https://github.com/1nv1sibl3/OS-CTF/assets/120787381/14a131f3-c74d-4e77-988e-64f034de56e5)

Now, you will find there are something strange on this word file: **ybirlbh**

![image](https://github.com/1nv1sibl3/OS-CTF/assets/120787381/04a3f972-754d-4fef-bfe4-7e0a63270731)

When you decode this with ROT-13, you will find it looks like a password

![image](https://github.com/1nv1sibl3/OS-CTF/assets/120787381/f8a04e4e-abdd-4ca3-824e-c1daba698e63)

When you extract the word file and look into the media directory, you will find it has 2 images

![image](https://github.com/1nv1sibl3/OS-CTF/assets/120787381/bf93de9a-4c9f-45ed-a2d4-72e468a1722d)

But in the word file, there is only one.

![image](https://github.com/1nv1sibl3/OS-CTF/assets/120787381/f061833f-a331-4d15-9c8f-c181882ee738)

It seems like the picture got encrypted. Now using this tool: https://decrypt.imageonline.co/ with the password is the decoded rot13 of the previous rot13 I said.

![image](https://github.com/1nv1sibl3/OS-CTF/assets/120787381/43b33f53-cef2-4fbf-8a58-8fd2e9ee2cbe)

You will got the flag!
