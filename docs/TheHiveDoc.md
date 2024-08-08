## About the connector
TheHive Security Incident Response Platform involves connecting external security tools, systems, or data sources with TheHive's platform. This integration facilitates centralized incident management, response coordination, and automation, enhancing overall security operations by streamlining incident detection, investigation, and resolution processes.
<p>This document provides information about the TheHive Connector, which facilitates automated interactions, with a TheHive server using FortiSOAR&trade; playbooks. Add the TheHive Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with TheHive.</p>

### Version information

Connector Version: 1.0.0


Authored By: Fortinet

Certified: No
## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-thehive</pre>

## Prerequisites to configuring the connector
- You must have the credentials of TheHive server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the TheHive server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>TheHive</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>Specify the Rest API endpoint URL of the TheHive server to connect and perform automated operations.</td>
</tr><tr><td>API Key</td><td>Specify the API key to access the TheHive Rest API endpoint to which you will connect and perform the automated operations.</td>
</tr><tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set to True.</td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Create Alert</td><td>Creates an alert in TheHive based on the input parameters you have specified.</td><td>create_alert <br/>Investigation</td></tr>
<tr><td>Get Alert</td><td>Retrieve detailed information of the specified alert based on its ID.</td><td>get_alert <br/>Investigation</td></tr>
<tr><td>Update Alerts</td><td>Update an alert in TheHive based on the input parameters you have specified.</td><td>update_alerts <br/>Investigation</td></tr>
<tr><td>Delete Alert</td><td>Delete an alert record from the TheHive platform based on the specified alert ID.</td><td>delete_alert <br/>Investigation</td></tr>
<tr><td>Add Alert Attachment</td><td>Add an attachment to an existing alert in TheHive.</td><td>add_alert_attachment <br/>Investigation</td></tr>
<tr><td>Get Alert Attachment</td><td>Retrieves an information about a specific attachment associated with an alert in TheHive.</td><td>get_alert_attachment <br/>Investigation</td></tr>
<tr><td>Delete Alert Attachment</td><td>Delete a specific attachment associated with an alert in TheHive.</td><td>delete_alert_attachment <br/>Investigation</td></tr>
<tr><td>Download Alert Attachment</td><td>Download a specific attachment associated with an alert in TheHive.</td><td>download_alert_attachment <br/>Investigation</td></tr>
<tr><td>Create Case</td><td>Creates a case in the in TheHive based on the input parameters you have specified.</td><td>create_case <br/>Investigation</td></tr>
<tr><td>Get Case</td><td>Retrieves a specific case information from the TheHive platform based on the Case ID you have specified.</td><td>get_case <br/>Investigation</td></tr>
<tr><td>Update Case</td><td>Update a case in the in TheHive based on the input parameters you have specified.</td><td>update_case <br/>Investigation</td></tr>
<tr><td>Delete Case</td><td>Delete a specific case from the TheHive platform based on the Case ID you have specified.</td><td>delete_case <br/>Investigation</td></tr>
<tr><td>Create Observable in Case</td><td>Add an observable to an existing case.</td><td>create_observable_in_case <br/>Investigation</td></tr>
<tr><td>Create Observable in Alert</td><td>Add an observable to an existing alert.</td><td>create_observable_in_alert <br/>Investigation</td></tr>
<tr><td>Get Observable</td><td>Retrieves a specific observable information from the TheHive platform based on the observable ID you have specified.</td><td>get_observable <br/>Investigation</td></tr>
<tr><td>Update Observable</td><td>Update the details of an existing observable within TheHive platform.</td><td>update_observable <br/>Investigation</td></tr>
<tr><td>Delete Observable</td><td>Delete a specific observable from the TheHive platform based on the input parameters you have specified.</td><td>delete_observable <br/>Investigation</td></tr>
<tr><td>Create Task in Case</td><td>Creates a task in the TheHive based on the input parameters you have specified.</td><td>create_task <br/>Investigation</td></tr>
<tr><td>Get Task</td><td>Retrieves information about a specific task from TheHive platform based on the task ID you have specified.</td><td>get_task <br/>Investigation</td></tr>
<tr><td>Update Task</td><td>Update the details of an existing task within TheHive platform.</td><td>update_task <br/>Investigation</td></tr>
<tr><td>Delete Task</td><td>Delete a specific task from the TheHive platform based on the task ID you have specified.</td><td>delete_task <br/>Investigation</td></tr>
</tbody></table>

### operation: Create Alert

#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Title</td><td>Specify the title of the alert you want to create in TheHive Platform.
</td></tr><tr><td>Description</td><td>Specify the description of the alert you want to create in TheHive Platform.
</td></tr><tr><td>Source Reference</td><td>Provide the source reference for the alert you want to create in TheHive Platform.
</td></tr><tr><td>Source</td><td>Specify the source of the alert you want to create in TheHive Platform.
</td></tr><tr><td>Alert Type</td><td>Specify the type of the alert you want to create in TheHive Platform.
</td></tr><tr><td>Severity</td><td>Specify the severity of the alert you want to create in TheHive Platform.
</td></tr><tr><td>Assignee</td><td>Specify the assignee of the alert you want to create in TheHive Platform.
</td></tr><tr><td>Summary</td><td>Specify the summary of the alert you want to create in TheHive Platform.
</td></tr><tr><td>Attachment</td><td>Upload a file attachment that contains multipart observables data which you want to add when creating the alert in TheHive platform.
</td></tr><tr><td>Observables</td><td>Specify the list of observables that you want to add at the time of creating the alert in TheHive Platform.
</td></tr><tr><td>Additional Field</td><td>Specify the additional fields required for the use case. Provide the fields in JSON format.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "_id": "",
    "_type": "",
    "_createdBy": "",
    "_updatedBy": "",
    "_createdAt": "",
    "_updatedAt": "",
    "type": "",
    "source": "",
    "sourceRef": "",
    "externalLink": "",
    "title": "",
    "description": "",
    "severity": "",
    "severityLabel": "",
    "date": "",
    "tags": [],
    "tlp": "",
    "tlpLabel": "",
    "pap": "",
    "papLabel": "",
    "follow": "",
    "customFields": [
        {
            "_id": "",
            "name": "",
            "type": "",
            "value": "",
            "order": ""
        }
    ],
    "caseTemplate": "",
    "observableCount": "",
    "caseId": "",
    "status": "",
    "stage": "",
    "assignee": "",
    "summary": "",
    "extraData": {},
    "newDate": "",
    "inProgressDate": "",
    "closedDate": "",
    "importedDate": "",
    "timeToDetect": "",
    "timeToTriage": "",
    "timeToQualify": "",
    "timeToAcknowledge": ""
}</pre>
### operation: Get Alert
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Alert ID</td><td>Specify the ID of the alert you want to retrieve the information of the alert.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "_id": "",
    "_type": "",
    "_createdBy": "",
    "_updatedBy": "",
    "_createdAt": "",
    "_updatedAt": "",
    "type": "",
    "source": "",
    "sourceRef": "",
    "externalLink": "",
    "title": "",
    "description": "",
    "severity": "",
    "severityLabel": "",
    "date": "",
    "tags": [],
    "tlp": "",
    "tlpLabel": "",
    "pap": "",
    "papLabel": "",
    "follow": "",
    "customFields": [
        {
            "_id": "",
            "name": "",
            "type": "",
            "value": "",
            "order": ""
        }
    ],
    "caseTemplate": "",
    "observableCount": "",
    "caseId": "",
    "status": "",
    "stage": "",
    "assignee": "",
    "summary": "",
    "extraData": {},
    "newDate": "",
    "inProgressDate": "",
    "closedDate": "",
    "importedDate": "",
    "timeToDetect": "",
    "timeToTriage": "",
    "timeToQualify": "",
    "timeToAcknowledge": ""
}</pre>
### operation: Update Alerts
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Action Type</td><td>Select the action type for updating alerts. You can choose either a single record update or a bulk update.
<br><strong>If you choose 'Single Record Update'</strong><ul><li>Alert ID: Specify the ID of the alert you want to update.</li></ul><strong>If you choose 'Bulk Update'</strong><ul><li>Alert IDs: Specify the IDs of the alerts you want to update in bulk.</li></ul></td></tr><tr><td>Title</td><td>Specify the title of the alert you want to update in TheHive Platform.
</td></tr><tr><td>Description</td><td>Specify the description of the alert you want to update in TheHive Platform.
</td></tr><tr><td>Source</td><td>Specify the source of the alert you want to update in TheHive Platform.
</td></tr><tr><td>Alert Type</td><td>Specify the type of the alert you want to update in TheHive Platform.
</td></tr><tr><td>Severity</td><td>Specify the Severity of the alert you want to update in TheHive Platform.
</td></tr><tr><td>Assignee</td><td>Specify the assignee of the alert you want to update in TheHive Platform.
</td></tr><tr><td>Summary</td><td>Specify the summary of the alert you want to update in TheHive Platform.
</td></tr><tr><td>Additional Field</td><td>Specify the additional fields you want to update and provide them in JSON format.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "_id": "",
    "_type": "",
    "_createdBy": "",
    "_updatedBy": "",
    "_createdAt": "",
    "_updatedAt": "",
    "type": "",
    "source": "",
    "sourceRef": "",
    "externalLink": "",
    "title": "",
    "description": "",
    "severity": "",
    "severityLabel": "",
    "date": "",
    "tags": [],
    "tlp": "",
    "tlpLabel": "",
    "pap": "",
    "papLabel": "",
    "follow": "",
    "customFields": [
        {
            "_id": "",
            "name": "",
            "type": "",
            "value": "",
            "order": ""
        }
    ],
    "caseTemplate": "",
    "observableCount": "",
    "caseId": "",
    "status": "",
    "stage": "",
    "assignee": "",
    "summary": "",
    "extraData": {},
    "newDate": "",
    "inProgressDate": "",
    "closedDate": "",
    "importedDate": "",
    "timeToDetect": "",
    "timeToTriage": "",
    "timeToQualify": "",
    "timeToAcknowledge": ""
}</pre>
### operation: Delete Alert
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Alert ID</td><td>Specify the ID of the alert you want to delete.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "type": "",
    "message": ""
}</pre>
### operation: Add Alert Attachment
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Alert ID</td><td>Specify the ID of the alert you want to add an attachment.
</td></tr><tr><td>Attachment</td><td>Upload a file attachment that contains multipart data which you want to add attachment to the alert in TheHive platform.
</td></tr><tr><td>Can Rename</td><td>If set to true, the files can be renamed if they already exist with the same name.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "attachments": [
        {
            "_id": "",
            "_type": "",
            "_createdBy": "",
            "_updatedBy": "",
            "_createdAt": "",
            "_updatedAt": "",
            "name": "",
            "hashes": [],
            "size": "",
            "contentType": "",
            "id": ""
        }
    ]
}</pre>
### operation: Get Alert Attachment
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Alert ID</td><td>Specify the ID of the alert from which you want to retrieve attachment.
</td></tr><tr><td>Attachment ID</td><td>Specify the ID of the attachment of which you want to retrieve information.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "type": "",
    "message": ""
}</pre>
### operation: Delete Alert Attachment
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Alert ID</td><td>Specify the ID of the alert from which you want to delete an attachment.
</td></tr><tr><td>Attachment ID</td><td>Specify the ID of the attachment you want to delete.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "type": "",
    "message": ""
}</pre>
### operation: Download Alert Attachment
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Alert ID</td><td>Specify the ID of the alert from which you want to download the associated attachment.
</td></tr><tr><td>Attachment ID</td><td>Specify the ID of the attachment you want to download.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "type": "",
    "message": ""
}</pre>
### operation: Create Case
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Title</td><td>Specify the title of the case you want to create in TheHive Platform.
</td></tr><tr><td>Description</td><td>Specify the description of the case you want to create in TheHive Platform.
</td></tr><tr><td>Summary</td><td>Specify the summary of the case you want to create in TheHive Platform.
</td></tr><tr><td>Assignee</td><td>Specify the assignee of the case you want to create in TheHive Platform.
</td></tr><tr><td>Severity</td><td>Specify the severity of the case you want to create in TheHive Platform.
</td></tr><tr><td>Status</td><td>Specify the status of the case you want to create in TheHive Platform.
</td></tr><tr><td>Additional Field</td><td>Specify the additional fields required for the use case. Provide the fields in JSON format.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "title": "",
    "description": "",
    "severity": "",
    "startDate": "",
    "endDate": "",
    "tags": [
        ""
    ],
    "flag": "",
    "tlp": "",
    "pap": "",
    "status": "",
    "summary": "",
    "assignee": "",
    "customFields": {
        "property1": "",
        "property2": ""
    },
    "caseTemplate": "",
    "tasks": [
        {
            "title": "",
            "group": "",
            "description": "",
            "status": "",
            "flag": "",
            "startDate": "",
            "endDate": "",
            "order": "",
            "dueDate": "",
            "assignee": "",
            "mandatory": ""
        }
    ],
    "pages": [
        {
            "title": "",
            "content": "",
            "order": "",
            "category": ""
        }
    ],
    "sharingParameters": [
        {
            "organisation": "",
            "share": "",
            "profile": "",
            "taskRule": "",
            "observableRule": ""
        }
    ],
    "taskRule": "string",
    "observableRule": "string"
}</pre>
### operation: Get Case
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Case ID</td><td>Specify the ID of the case you want to retrieve information from TheHive Platform.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "_id": "",
    "_type": "",
    "_createdBy": "",
    "_updatedBy": "",
    "_createdAt": "",
    "_updatedAt": "",
    "number": "",
    "title": "",
    "description": "",
    "severity": "",
    "severityLabel": "",
    "startDate": "",
    "endDate": "",
    "tags": [],
    "flag": "",
    "tlp": "",
    "tlpLabel": "",
    "pap": "",
    "papLabel": "",
    "status": "",
    "stage": "",
    "summary": "",
    "impactStatus": "",
    "assignee": "",
    "customFields": [
        {
            "_id": "",
            "name": "",
            "type": "",
            "value": "",
            "order": ""
        }
    ],
    "userPermissions": [],
    "extraData": {},
    "newDate": "",
    "inProgressDate": "",
    "closedDate": "",
    "alertDate": "",
    "alertNewDate": "",
    "alertInProgressDate": "",
    "alertImportedDate": "",
    "timeToDetect": "",
    "timeToTriage": "",
    "timeToQualify": "",
    "timeToAcknowledge": "",
    "timeToResolve": "",
    "handlingDuration": ""
}</pre>
### operation: Update Case
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Action Type</td><td>Select the action type for updating case. You can choose either a single record update or a bulk update.
<br><strong>If you choose 'Single Record Update'</strong><ul><li>Case ID: Specify the ID of the case you want to update.</li></ul><strong>If you choose 'Bulk Update'</strong><ul><li>Case IDs: Specify the IDs of the case you want to update in bulk.</li></ul></td></tr><tr><td>Title</td><td>Specify the title of the case you want to update in TheHive Platform.
</td></tr><tr><td>Description</td><td>Specify the description of the case you want to update in TheHive Platform.
</td></tr><tr><td>Summary</td><td>Specify the summary of the case you want to update in TheHive Platform.
</td></tr><tr><td>Assignee</td><td>Specify the assignee of the case you want to update in TheHive Platform.
</td></tr><tr><td>Severity</td><td>Specify the severity of the case you want to update in TheHive Platform.
</td></tr><tr><td>Status</td><td>Specify the status of the case you want to update in TheHive Platform.
</td></tr><tr><td>Additional Field</td><td>Specify the additional fields required for the use case. Provide the fields in JSON format.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "type": "",
    "message": ""
}</pre>
### operation: Delete Case
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Case ID</td><td>Specify the ID of the case you want to delete from TheHive Platform.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "_id": "",
    "_type": "",
    "_createdBy": "",
    "_updatedBy": "",
    "_createdAt": "",
    "_updatedAt": "",
    "number": "",
    "title": "",
    "description": "",
    "severity": "",
    "severityLabel": "",
    "startDate": "",
    "endDate": "",
    "tags": [],
    "flag": "",
    "tlp": "",
    "tlpLabel": "",
    "pap": "",
    "papLabel": "",
    "status": "",
    "stage": "",
    "summary": "",
    "impactStatus": "",
    "assignee": "",
    "customFields": [
        {
            "_id": "",
            "name": "",
            "type": "",
            "value": "",
            "order": ""
        }
    ],
    "userPermissions": [],
    "extraData": {},
    "newDate": "",
    "inProgressDate": "",
    "closedDate": "",
    "alertDate": "",
    "alertNewDate": "",
    "alertInProgressDate": "",
    "alertImportedDate": "",
    "timeToDetect": "",
    "timeToTriage": "",
    "timeToQualify": "",
    "timeToAcknowledge": "",
    "timeToResolve": "",
    "handlingDuration": ""
}</pre>
### operation: Create Observable in Case
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Case ID</td><td>Specify the ID of the case for which you want to create an observable in TheHive Platform.
</td></tr><tr><td>Data Type</td><td>Select the input type for creating an observable. You can choose either 'Create Observable using Attachment' or 'Create Observable using Plain Text.'
<br><strong>If you choose 'Autonomous-System'</strong><ul><li>Data: Provide the data for the observable that you wish to create and associate with a case in TheHive Platform.</li></ul><strong>If you choose 'Domain'</strong><ul><li>Data: Provide the data for the observable that you wish to create and associate with a case in TheHive Platform.</li></ul><strong>If you choose 'FQDN'</strong><ul><li>Data: Provide the data for the observable that you wish to create and associate with a case in TheHive Platform.</li></ul><strong>If you choose 'Hash'</strong><ul><li>Data: Provide the data for the observable that you wish to create and associate with a case in TheHive Platform.</li></ul><strong>If you choose 'IP'</strong><ul><li>Data: Provide the data for the observable that you wish to create and associate with a case in TheHive Platform.</li></ul><strong>If you choose 'Mail'</strong><ul><li>Data: Provide the data for the observable that you wish to create and associate with a case in TheHive Platform.</li></ul><strong>If you choose 'Mail_Subject'</strong><ul><li>Data: Provide the data for the observable that you wish to create and associate with a case in TheHive Platform.</li></ul><strong>If you choose 'Other'</strong><ul><li>Data: Provide the data for the observable that you wish to create and associate with a case in TheHive Platform.</li></ul><strong>If you choose 'Regexp'</strong><ul><li>Data: Provide the data for the observable that you wish to create and associate with a case in TheHive Platform.</li></ul><strong>If you choose 'Registry'</strong><ul><li>Data: Provide the data for the observable that you wish to create and associate with a case in TheHive Platform.</li></ul><strong>If you choose 'Uri_Path'</strong><ul><li>Data: Provide the data for the observable that you wish to create and associate with a case in TheHive Platform.</li></ul><strong>If you choose 'URL'</strong><ul><li>Data: Provide the data for the observable that you wish to create and associate with a case in TheHive Platform.</li></ul><strong>If you choose 'User-Agent'</strong><ul><li>Data: Provide the data for the observable that you wish to create and associate with a case in TheHive Platform.</li></ul><strong>If you choose 'File'</strong><ul><li>Attachment: Upload a file attachment that contains multipart observables data which you want to add with the case in TheHive platform.</li><li>Is Zip: If set to true, the file is unzipped using the Zip Password and each file in the zip is treated as an observable.</li><strong>If you choose 'true'</strong><ul><li>Zip Password: Specify the password for the zip file that you will use to unzip it.</li></ul></ul></td></tr><tr><td>Message</td><td>Specify the message of the observable you want to create for case in TheHive Platform.
</td></tr><tr><td>Tags</td><td>Specify the Tags of the observable you want to create for case in TheHive Platform.
</td></tr><tr><td>TLP</td><td>Specify the tlp of the observable you want to create for case in TheHive Platform.
</td></tr><tr><td>Ignore Similarity</td><td>Selecting this option will bypass the similarity check for the observable type being created for the case in TheHive Platform.
</td></tr><tr><td>Additional Field</td><td>Specify the additional fields required for the use case. Provide the fields in JSON format.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>[
    {
        "_id": "",
        "_type": "",
        "_createdBy": "",
        "_updatedBy": "",
        "_createdAt": "",
        "_updatedAt": "",
        "dataType": "",
        "data": "",
        "startDate": "",
        "attachment": {
            "_id": "",
            "_type": "",
            "_createdBy": "",
            "_updatedBy": "",
            "_createdAt": "",
            "_updatedAt": "",
            "name": "",
            "hashes": [],
            "size": "",
            "contentType": "",
            "id": ""
        },
        "tlp": "",
        "tlpLabel": "",
        "pap": "",
        "papLabel": "",
        "tags": [],
        "ioc": "",
        "sighted": "",
        "sightedAt": "",
        "reports": {},
        "message": "",
        "extraData": {},
        "ignoreSimilarity": ""
    }
]</pre>
### operation: Create Observable in Alert
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Alert ID</td><td>Specify the ID of the alert for which you want to create an observable in TheHive Platform.
</td></tr><tr><td>Data Type</td><td>Select the input type for creating an observable. You can choose either 'Create Observable using Attachment' or 'Create Observable using Plain Text.'
<br><strong>If you choose 'Autonomous-System'</strong><ul><li>Data: Provide the data for the observable that you wish to create and associate with a alert in TheHive Platform.</li></ul><strong>If you choose 'Domain'</strong><ul><li>Data: Provide the data for the observable that you wish to create and associate with a alert in TheHive Platform.</li></ul><strong>If you choose 'FQDN'</strong><ul><li>Data: Provide the data for the observable that you wish to create and associate with a alert in TheHive Platform.</li></ul><strong>If you choose 'Hash'</strong><ul><li>Data: Provide the data for the observable that you wish to create and associate with a alert in TheHive Platform.</li></ul><strong>If you choose 'IP'</strong><ul><li>Data: Provide the data for the observable that you wish to create and associate with a alert in TheHive Platform.</li></ul><strong>If you choose 'Mail'</strong><ul><li>Data: Provide the data for the observable that you wish to create and associate with a alert in TheHive Platform.</li></ul><strong>If you choose 'Mail_Subject'</strong><ul><li>Data: Provide the data for the observable that you wish to create and associate with a alert in TheHive Platform.</li></ul><strong>If you choose 'Other'</strong><ul><li>Data: Provide the data for the observable that you wish to create and associate with a alert in TheHive Platform.</li></ul><strong>If you choose 'Regexp'</strong><ul><li>Data: Provide the data for the observable that you wish to create and associate with a alert in TheHive Platform.</li></ul><strong>If you choose 'Registry'</strong><ul><li>Data: Provide the data for the observable that you wish to create and associate with a alert in TheHive Platform.</li></ul><strong>If you choose 'Uri_Path'</strong><ul><li>Data: Provide the data for the observable that you wish to create and associate with a alert in TheHive Platform.</li></ul><strong>If you choose 'URL'</strong><ul><li>Data: Provide the data for the observable that you wish to create and associate with a alert in TheHive Platform.</li></ul><strong>If you choose 'User-Agent'</strong><ul><li>Data: Provide the data for the observable that you wish to create and associate with a alert in TheHive Platform.</li></ul><strong>If you choose 'File'</strong><ul><li>Attachment: Upload a file attachment that contains multipart observables data which you want to add with the case in TheHive platform.</li><li>Is Zip: If set to true, the file is unzipped using the Zip Password and each file in the zip is treated as an observable.</li><strong>If you choose 'true'</strong><ul><li>Zip Password: Specify the password for the zip file that you will use to unzip it.</li></ul></ul></td></tr><tr><td>Message</td><td>Specify the message of the observable you want to create for alert in TheHive Platform.
</td></tr><tr><td>Tags</td><td>Specify the Tags of the observable you want to create for alert in TheHive Platform.
</td></tr><tr><td>Ignore Similarity</td><td>If you select this option, the similarity of the observable type you want to create for the alert in TheHive Platform will be ignored.
</td></tr><tr><td>Additional Field</td><td>Specify the additional fields required for the use case. Provide the fields in JSON format.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>[
    {
        "_id": "",
        "_type": "",
        "_createdBy": "",
        "_updatedBy": "",
        "_createdAt": "",
        "_updatedAt": "",
        "dataType": "",
        "data": "",
        "startDate": "",
        "attachment": {
            "_id": "",
            "_type": "",
            "_createdBy": "",
            "_updatedBy": "",
            "_createdAt": "",
            "_updatedAt": "",
            "name": "",
            "hashes": [],
            "size": "",
            "contentType": "",
            "id": ""
        },
        "tlp": "",
        "tlpLabel": "",
        "pap": "",
        "papLabel": "",
        "tags": [],
        "ioc": "",
        "sighted": "",
        "sightedAt": "",
        "reports": {},
        "message": "",
        "extraData": {},
        "ignoreSimilarity": ""
    }
]</pre>
### operation: Get Observable
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Observable ID</td><td>Specify the ID of the observable from which you want to retrieve information from TheHive Platform.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "_id": "",
    "_type": "",
    "_createdBy": "",
    "_updatedBy": "",
    "_createdAt": "",
    "_updatedAt": "",
    "dataType": "",
    "data": "",
    "startDate": "",
    "attachment": {
        "_id": "",
        "_type": "",
        "_createdBy": "",
        "_updatedBy": "",
        "_createdAt": "",
        "_updatedAt": "",
        "name": "",
        "hashes": [],
        "size": "",
        "contentType": "",
        "id": ""
    },
    "tlp": "",
    "tlpLabel": "",
    "pap": "",
    "papLabel": "",
    "tags": [],
    "ioc": "",
    "sighted": "",
    "sightedAt": "",
    "reports": {},
    "message": "",
    "extraData": {},
    "ignoreSimilarity": ""
}</pre>
### operation: Update Observable
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Action Type</td><td>Select the action type for updating observable. You can choose either a single record update or a bulk update.
<br><strong>If you choose 'Single Record Update'</strong><ul><li>Observable ID: Specify the ID of the observable for which you want to update an observable information in TheHive Platform.</li></ul><strong>If you choose 'Bulk Update'</strong><ul><li>Observable IDs: Specify the IDs of the observable you want to update in bulk.</li></ul></td></tr><tr><td>Data Type</td><td>Select the input type for creating an observable. You can choose either 'Create Observable using Attachment' or 'Create Observable using Plain Text.'
</td></tr><tr><td>Message</td><td>Specify the message of the observable you want to update for alert in TheHive Platform.
</td></tr><tr><td>Add Tags</td><td>Specify CSV list of tags will be added to the current observable.
</td></tr><tr><td>Remove Tags</td><td>Specify CSV list tags will be removed from the current observable.
</td></tr><tr><td>TLP</td><td>Specify the TLP of the observable you want to update.
</td></tr><tr><td>Additional Field</td><td>Specify the additional fields required for the use case. Provide the fields in JSON format.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>[
    {
        "_id": "",
        "_type": "",
        "_createdBy": "",
        "_updatedBy": "",
        "_createdAt": "",
        "_updatedAt": "",
        "dataType": "",
        "data": "",
        "startDate": "",
        "attachment": {
            "_id": "",
            "_type": "",
            "_createdBy": "",
            "_updatedBy": "",
            "_createdAt": "",
            "_updatedAt": "",
            "name": "",
            "hashes": [],
            "size": "",
            "contentType": "",
            "id": ""
        },
        "tlp": "",
        "tlpLabel": "",
        "pap": "",
        "papLabel": "",
        "tags": [],
        "ioc": "",
        "sighted": "",
        "sightedAt": "",
        "reports": {},
        "message": "",
        "extraData": {},
        "ignoreSimilarity": ""
    }
]</pre>
### operation: Delete Observable
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Observable ID</td><td>Specify the ID of the observable from which you want to retrieve information from TheHive Platform.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "type": "",
    "message": ""
}</pre>
### operation: Create Task in Case
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Case ID</td><td>Specify the ID of the case in which you want to create task in TheHive Platform.
</td></tr><tr><td>Title</td><td>Specify the title of the task you want to create in TheHive Platform.
</td></tr><tr><td>Description</td><td>Specify the description of the task you want to create in TheHive Platform.
</td></tr><tr><td>Status</td><td>Specify the status of the task you want to create in TheHive Platform.
</td></tr><tr><td>Group</td><td>Specify the group of the task you want to create in TheHive Platform.
</td></tr><tr><td>Assignee</td><td>Specify the assignee of the task you want to create in TheHive Platform.
</td></tr><tr><td>Additional Field</td><td>Specify the additional fields required for the use case. Provide the fields in JSON format.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "_id": "",
    "_type": "",
    "_createdBy": "",
    "_updatedBy": "",
    "_createdAt": "",
    "_updatedAt": "",
    "title": "",
    "group": "",
    "description": "",
    "status": "",
    "flag": "",
    "startDate": "",
    "endDate": "",
    "assignee": "",
    "order": "",
    "dueDate": "",
    "mandatory": "",
    "extraData": {}
}</pre>
### operation: Get Task
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Task ID</td><td>Specify the ID of the task you want to retrieve information from TheHive Platform.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "_id": "",
    "_type": "",
    "_createdBy": "",
    "_updatedBy": "",
    "_createdAt": "",
    "_updatedAt": "",
    "title": "",
    "group": "",
    "description": "",
    "status": "",
    "flag": "",
    "startDate": "",
    "endDate": "",
    "assignee": "",
    "order": "",
    "dueDate": "",
    "mandatory": "",
    "extraData": {}
}</pre>
### operation: Update Task
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Action Type</td><td>Select the action type for updating task. You can choose either a single record update or a bulk update.
<br><strong>If you choose 'Single Record Update'</strong><ul><li>Task ID: Specify the ID of the task for which you want to update an task information in TheHive Platform.</li></ul><strong>If you choose 'Bulk Update'</strong><ul><li>Task IDs: Specify the IDs of the task you want to update in bulk.</li></ul></td></tr><tr><td>Title</td><td>Specify the title of the task you want to update in TheHive Platform.
</td></tr><tr><td>Description</td><td>Specify the description of the task you want to update in TheHive Platform.
</td></tr><tr><td>Status</td><td>Specify the status of the task you want to update in TheHive Platform.
</td></tr><tr><td>Group</td><td>Specify the group of the task you want to update in TheHive Platform.
</td></tr><tr><td>Assignee</td><td>Specify the assignee of the task you want to update in TheHive Platform.
</td></tr><tr><td>Additional Field</td><td>Specify the additional fields required for the use case. Provide the fields in JSON format.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "type": "",
    "message": ""
}</pre>
### operation: Delete Task
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Task ID</td><td>Specify the ID of the task from which you want to delete from TheHive Platform.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "type": "",
    "message": ""
}</pre>
