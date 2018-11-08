# Accept Suite 

Developer Guide to deploy the Python Web API Application on Heroku.

## Prerequisites:

*   Python 2.7
*   Git
*	Heroku CLI
*	Free Heroku Account

## Python Setup

After installing Python successfully, below steps are to be followed to setup Python

### Set Environment Variables

There will be a folder named "Python27" in the local directory where Python is installed.

1. Search for environment variables in your system and go to the list of environment variables.

![Image of envVariables](Github-Images/envVariables.PNG)

2. In the "User environment variables", select "path" variable and click Edit.

3. Add the path of the Python27 folder as value to the Path variable.

4. Add the path of the scripts folder inside Python27 folder as value to the Path variable.

5. Now in the "System environment variables", click New.

6. Add variable name as "PYTHON_HOME".

7. Add path of the Python27 folder as variable value and click OK.

![Image of pythonHome](Github-Images/pythonHome.PNG)

## Deploying Python Application on Heroku

Please follow step by step procedure to host the Python Web API applications on Heroku.
	
*   Clone the Repository or Download the source code to local folder.
	
*	Open Command prompt in Administrator mode.

*	Go to the path of the "Accept-Suite-Python-ServiceApp" application directory in command prompt by running the command

	cd path\to\application\directory
	
	For example cd C:\Users\ljakka\AcceptSuiteService-Python-master\Accept-Suite-Python-ServiceApp

	![Image of redirect](Github-Images/redirect.PNG)
	
*	Run the following commands with username(mail id) and password to set proxy,

	set https_proxy=https://unsername:password@internet.visa.com:443
	
	set http_proxy=http://unsername:password@internet.visa.com:80

*	Run the command "heroku login". It will ask for the login details and provide your heroku account mail id and password.

*	After logging in , run the command "heroku create appName". Here appName is the name of your application.

	![Image of createApp](Github-Images/createApp.PNG)

*   Run “git init” command. This will create a git repository for the application in Heroku.

	![Image of init](Github-Images/init.PNG)

*	Run command “git remote -v”, it should be the created application git URL. 

	![Image of remote](Github-Images/remote.PNG)
	
	If URL is not found, then set remote for the application
	by running the command,
	
	heroku git:remote -a appName
	
	![Image of remote-cmd](Github-Images/remote-cmd.PNG)

* 	Run “git status” command, it will provide the details of files not pushed to git.

	![Image of status](Github-Images/status.PNG)

*	Run the command “git add .” This command tells Git that you want to include updates of files in the next commit.

*	To commit the files, run git commit –am “Comments” command.

*	Finally, run the command “git push heroku master” which will do the deployment of our application.

	![Image of deploy](Github-Images/deploy.PNG)

At last, it will provide us the URL of the hosted application on Heroku.