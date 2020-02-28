![](https://img.shields.io/badge/STATUS-NOT%20CURRENTLY%20MAINTAINED-red.svg?longCache=true&style=flat)

# Important Notice
We have decided to stop the maintenance of this public GitHub repository.

LinkedIn Data Access Connector for SAP Lumira
===========================
By [Alper Derici](http://scn.sap.com/people/alper.derici%40sap)

A Lumira Data Access Extension To Fetch Linkedin Contacts

This extension will download your list of contacts from Linkedin, and will let you analyze the dataset in SAP Lumira.

A Step-by-Step Guide to Installation & Execution of the LinkedIn Data Access Extension is shown as follows:

<strong>Step 1:	Creation of a LinkedIn app</strong> <br>
The reason why we need to create a LinkedIn app is so that we can access the LinkedIn API keys, which will be our main source of extracting LinkedIn data which is primarily the list of your LinkedIn contacts,  and importing it into SAP Lumira for visualization where we can then analyze the dataset. <br>

1. Log in to your LinkedIn account (or sign up if you don’t already have one), and then go to https://www.linkedin.com/developer/apps and create a new LinkedIn application.
![My image](https://github.com/SAP/lumira-extension-da-linkedin/blob/master/readmescreenshots/1.jpg) <br>

![My image](https://github.com/SAP/lumira-extension-da-linkedin/blob/master/readmescreenshots/2.jpg) <br>

2.After creating the application, we can now retrieve the API client ID and client secret which we will use later. <br>
![My image](https://github.com/SAP/lumira-extension-da-linkedin/blob/master/readmescreenshots/3.jpg) 

<strong>NOTE:</strong> We will also require the User Key and User Secret, i.e. the OAuth token and OAuth secret respectively. This can be done only programmatically. You can try it out using the following reference: https://developer.linkedin.com/docs/oauth2 
<br>

<strong>Step 2:	Activate Data Source Extensions in Lumira</strong> <br>
1. Go to the directory where SAP Lumira is installed: C:\Program Files\SAP Lumira\Desktop <br>
2. Find the file SAPLumira.ini and open it with a text editor. <br>
![My image](https://github.com/SAP/lumira-extension-da-linkedin/blob/master/readmescreenshots/a.jpg) <br>

3.Add the following lines of code to the SAPLumira.ini file: <br>
  -Dhilo.externalds.folder=C:\Program Files\SAP Lumira\Desktop\daextensions <br>
  -Dactivate.externaldatasource.ds=true <br>
![My image](https://github.com/SAP/lumira-extension-da-linkedin/blob/master/readmescreenshots/b.jpg)<br>

4. Now save this file and create a folder called daextensions in the C:\Program Files\SAP Lumira\Desktop directory so that we have a directory called C:\Program Files\SAP Lumira\Desktop\daextensions <br>
5. Download the executable file called LinkedinExtractor.exe to the directory we just created.<br>

<strong>Step 3:	Import data extension into Lumira</strong> <br>
1. Now open up Lumira and add a new dataset from an external data source as follows:<br>
![My image](https://github.com/SAP/lumira-extension-da-linkedin/blob/master/readmescreenshots/d.jpg)<br>

2. We can see the linkedinextractor as an uncategorized extension:<br>
![My image](https://github.com/SAP/lumira-extension-da-linkedin/blob/master/readmescreenshots/e.jpg)<br>

<strong>Step 4:	Provide extraction parameters</strong> <br>
The LinkedinExtractor.exe will automatically open up when we click on Next above. Enter the Client ID and Client Secret from what we obtained earlier as Consumer Key and Consumer Secret respectively. The User Key and User Secret are the OAuth Key and OAuth Secret, if you are able to obtain that programmatically from the link: https://developer.linkedin.com/docs/oauth2 as mentioned above.<br>
![My image](https://github.com/SAP/lumira-extension-da-linkedin/blob/master/readmescreenshots/c.png)<br>

<strong>Step 5:	Create dataset</strong> <br>
Live LinkedIn data will be imported as a dataset, which we can choose to create. In this case, it only imports the first name and last name information for your LinkedIn contacts. <br>

<strong>Step 6:	Get live insights</strong> <br>
Once you have the dataset imported into Lumira, you can now play around with the data and charts as you please!<br>

================================================================

<strong>NOTE: </strong><br>
This is a developer-centric extension, and involves custom coding for further use. Please refer to LinkedIn's guide to leveraging your application: https://developer.linkedin.com/docs/oauth2 
