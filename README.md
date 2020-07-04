# Python connector for Dynamics 365
## How to Install
```
pip install pdynamics
```
## Usage
```
from pdynamics import crm
```
### On-Premises
#### AD
Connect on-premises organizations via user and password

AD access sample:
```
crmurl = 'http://servername:port/orgname/'
user = 'domain\\username'
password = 'yourpassword'
crmorg = crm.client(crmurl, user, password)
crmorg.test_connection()
```
#### IFD
Connect to Dynamics 365 IFD organizations, access_token is required to send requests, it's necessary to create an application group, it has a client id. For example: client id is: 289c7417-83b7-41c3-8fab-68f111b5ba60, and CRM IFD URL is https://mycrmorg.company.com:443/

Run powershell as Admin on AD FS server

```powershell
PS C:\windows\system32> Grant-AdfsApplicationPermission
cmdlet Grant-AdfsApplicationPermission at command pipeline position 1
Supply values for the following parameters:
ClientRoleIdentifier: 289c7417-83b7-41c3-8fab-68f111b5ba60
ServerRoleIdentifier: https://mycrmorg.company.com:443/
```
What's the token endpoint?

When log in CRM, system will redirect to ADFS login page, url is something like https://mycrmorg.company.com:5555/adfs/ls/?wa=wsignin1.0&wtrealm=....., then your token endpoint will be https://mycrmorg.company.com:5555/adfs/oauth2/token

IFD Connection Sample:
```
crmurl = 'https://mycrmorg.company.com:443/'
tokenurl = 'https://mycrmorg.company.com:5555/adfs/oauth2/token'
user = 'domain\\username'
password = 'yourpassword'
clientid = '289c7417-83b7-41c3-8fab-68f111b5ba60'
crmorg = crm.client(crmurl, user, password, clientid, tokenurl)
crmorg.test_connection()
```
### Online
Access Dynamics 365 Online:

1. Go to office 365 admin center -> Azure Active Directory or https://aad.portal.azure.com/yourcompanydomain
2. Azure Active Directory -> App registrations -> Register an application
    a. input a Name
    b. select "Accounts in this organizational directory only (Single tenant)" - other options might also work
    c. Manage -> Certificates & secrets -> New client secret (keep this client_secret for later use)
    d. API permissions -> Add a permission -> Select an API -> Microsoft APIs-> Dynamics CRM
    e. Grant admin consent for '{your company}'
    f. Find client id (Application ID) in Overview page 

Dynamics 365 Online Connection Sample:
```python
crmurl = 'https://mycrmorg.crm.dynamics.com/'
user = 'username@mycrmorg.onmicrosoft.com'
password = 'yourpassword'
clientid = '289c7417-83b7-41c3-8fab-68f111b5ba60'
clientsecret = 'Pq-oEk~_7044Q2V~QGXwaH~2v9k0qlSG1K'
crmorg = crm.client(crmurl, user, password, clientid, client_secret=clientsecret)
crmorg.test_connection()
```