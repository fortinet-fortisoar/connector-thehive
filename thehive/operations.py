"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""
import json
import os
import uuid

import requests
from connectors.core.connector import get_logger, ConnectorError
from connectors.cyops_utilities.builtins import download_file_from_cyops, upload_file_to_cyops
from django.conf import settings

logger = get_logger('thehive')


class TheHive(object):

    def __init__(self, config):
        self.server_url = config.get('server_url', '').strip('/')
        if not self.server_url.startswith('https://') and not self.server_url.startswith('http://'):
            self.server_url = 'https://' + self.server_url
        self.verify_ssl = config.get('verify_ssl', False)
        self.api_key = config.get('api_key')
        self.headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {self.api_key}'}

    def make_api_call(self, endpoint, method='POST', payload=None, files={}, params=None):
        service_endpoint = self.server_url + endpoint
        try:
            response = requests.request(method, service_endpoint, data=payload, headers=self.headers, params=params,
                                        verify=self.verify_ssl)
            logger.debug('API Payload: {0}'.format(payload))
            logger.debug('API Response Reason: {0}'.format(response.reason))
            logger.debug('API Service Endpoint: {0}'.format(service_endpoint))
            logger.debug('API Response Status code: {0}'.format(response.status_code))
            logger.debug('API Response: {0}'.format(response.text))
            content_type = response.headers.get('Content-Type')
            if response.ok:
                if 'application/json' in content_type:
                    return response.json()
                else:
                    content_type = response.headers.get('Content-Disposition')
                    if content_type:
                        content_type = content_type.split(";")
                    if isinstance(content_type, list) and 'attachment' == content_type[0]:
                        return response.content, content_type[1].split("=")[1].replace('"', '')
                    else:
                        return response.content, uuid.uuid4()
            else:
                raise ConnectorError({'status': 'Failure', 'status_code': str(response.status_code), 'response': response.text})
        except requests.exceptions.SSLError as err:
            logger.error(err)
            raise ConnectorError('SSL certificate validation failed')
        except requests.exceptions.ConnectTimeout as err:
            logger.error(err)
            raise ConnectorError('The request timed out while trying to connect to the server')
        except requests.exceptions.ReadTimeout as err:
            logger.error(err)
            raise ConnectorError('The server did not send any data in the allotted amount of time')
        except requests.exceptions.ConnectionError as err:
            logger.error(err)
            raise ConnectorError('Invalid endpoint or credentials')
        except Exception as err:
            logger.error(err)
            raise ConnectorError(str(err))


def get_file_object(file_iri):
    if file_iri:
        file_metadata = download_file_from_cyops(file_iri)
        file_path = file_metadata.get('cyops_file_path')
        filename = file_metadata.get('filename')
        fil_absolute_path = os.path.join('/tmp/', file_path)
        files_obj = {filename: open(fil_absolute_path, 'rb')}
        return filename, files_obj


def create_alert(config, params):
    hive_obj = TheHive(config)
    file_iri = params.pop('attachment', {}).get('@id')
    observables = params.get('observables', [])
    additional_field = params.pop('additional_field', {})
    files = {}
    if file_iri:
        filename, files_obj = get_file_object(file_iri)
        if filename and files_obj:
            observables.append({"dataType": "file", "attachment": filename})
            params['observables'] = observables
    if additional_field:
        params = {**params, **additional_field}
    params = {k: v for k, v in params.items() if v is not None and v != ''}
    files = {'_json': json.dumps(params), **files}
    return hive_obj.make_api_call('/api/v1/alert', files=files)


def get_alert(config, params):
    hive_obj = TheHive(config)
    alert_id = params.get('alertID')
    endpoint = f'/v1/alert/{alert_id}'
    return hive_obj.make_api_call(endpoint, method='GET')


def update_alerts(config, params):
    hive_obj = TheHive(config)
    additional_field = params.pop('additional_field', {})
    action_type = params.pop('action_type', {})
    if action_type == 'Single Record Update':
        alert_id = params.pop('alert_id', '')
        endpoint = f'/api/v1/alert/{alert_id}'
    else:
        alert_ids = params.pop('alert_ids', '')
        if isinstance(alert_ids, str):
            alert_ids = alert_ids.split(',')
            alert_ids = [alert_id.strip() for alert_id in alert_ids if alert_id != '']
        else:
            alert_ids = list(alert_ids)
        params['ids'] = alert_ids
        endpoint = '/api/v1/alert/_bulk'
    if additional_field:
        params = {**params, **additional_field}
    params = {k: v for k, v in params.items() if v is not None and v != ''}
    payload = json.dumps(params)
    return hive_obj.make_api_call(endpoint, method='PATCH', payload=payload)


def delete_alert(config, params):
    hive_obj = TheHive(config)
    alert_id = params.get('alertID')
    endpoint = f'/api/v1/alert/{alert_id}'
    return hive_obj.make_api_call(endpoint, method='DELETE')


def add_alert_attachment(config, params):
    hive_obj = TheHive(config)
    alert_id = params.pop('alertId', '')
    file_iri = params.pop('attachment', {}).get('@id')
    files_obj = {}
    if file_iri:
        filename, files_obj = get_file_object(file_iri)
    params = {k: v for k, v in params.items() if v is not None and v != ''}
    endpoint = f'/api/v1/alert/{alert_id}/attachments'
    payload = json.dumps(params)
    return hive_obj.make_api_call(endpoint, method='POST', files=files_obj, payload=payload)


def get_alert_attachment(config, params):
    hive_obj = TheHive(config)
    alert_id = params.pop('alertID', '')
    attachment_id = params.pop('attachmentId', '')
    endpoint = f'/api/v1/alert/{alert_id}/attachment/{attachment_id}'
    return hive_obj.make_api_call(endpoint, method='GET')


def delete_alert_attachment(config, params):
    hive_obj = TheHive(config)
    alert_id = params.pop('alertID', '')
    attachment_id = params.pop('attachmentId', '')
    endpoint = f'/api/v1/alert/{alert_id}/attachment/{attachment_id}'
    return hive_obj.make_api_call(endpoint, method='DELETE')


def download_alert_attachment(config, params):
    hive_obj = TheHive(config)
    alert_id = params.pop('alertID', '')
    attachment_id = params.pop('attachmentId', '')
    endpoint = f'/api/v1/alert/{alert_id}/attachment/{attachment_id}'
    resp, file_name = hive_obj.make_api_call(endpoint, method='GET')
    path = os.path.join(settings.TMP_FILE_ROOT, file_name)
    with open(path, 'wb') as fp:
        fp.write(resp)
    attach_response = upload_file_to_cyops(file_path=file_name, filename=file_name,
                                           name=file_name, create_attachment=True)
    return attach_response


def create_case(config, params):
    hive_obj = TheHive(config)
    additional_field = params.pop('additional_field', {})
    if additional_field:
        params = {**params, **additional_field}
    params = {k: v for k, v in params.items() if v is not None and v != ''}
    payload = json.dumps(params)
    return hive_obj.make_api_call('/api/v1/alert', payload=payload)


def get_case(config, params):
    hive_obj = TheHive(config)
    case_id = params.get('caseID')
    endpoint = f'/api/v1/case/{case_id}'
    return hive_obj.make_api_call(endpoint, method='GET')


def update_case(config, params):
    hive_obj = TheHive(config)
    additional_field = params.pop('additional_field', {})
    action_type = params.pop('action_type', {})
    if action_type == 'Single Record Update':
        case_id = params.pop('case_id', '')
        endpoint = f'/api/v1/case/{case_id}'
    else:
        case_ids = params.pop('case_ids', '')
        if isinstance(case_ids, str):
            case_ids = case_ids.split(',')
            case_ids = [case_id.strip() for case_id in case_ids if case_id != '']
        else:
            case_ids = list(case_ids)
        params['ids'] = case_ids
        endpoint = '/api/v1/case/_bulk'
    if additional_field:
        params = {**params, **additional_field}
    params = {k: v for k, v in params.items() if v is not None and v != ''}
    payload = json.dumps(params)
    return hive_obj.make_api_call(endpoint, method='PATCH', payload=payload)


def delete_case(config, params):
    hive_obj = TheHive(config)
    case_id = params.get('caseID')
    endpoint = f'/api/v1/case/{case_id}'
    return hive_obj.make_api_call(endpoint, method='DELETE')


def build_observable_payload(params):
    data_type = params.get('dataType', '').lower()
    files_obj = {}
    params['dataType'] = data_type
    if data_type == 'file':
        file_iri = params.pop('attachment', {}).get('@id')
        if file_iri:
            filename, files_obj = get_file_object(file_iri)
    params = {k: v for k, v in params.items() if v is not None and v != ''}
    payload = json.dumps(params)
    return payload, files_obj


def create_observable_in_case(config, params):
    hive_obj = TheHive(config)
    case_id = params.get('caseID')
    endpoint = f'/api/v1/case/{case_id}/observable'
    payload, files_obj = build_observable_payload(params)
    return hive_obj.make_api_call(endpoint, payload=payload, files=files_obj)


def create_observable_in_alert(config, params):
    hive_obj = TheHive(config)
    alert_id = params.get('alertID')
    endpoint = f'/api/v1/alert/{alert_id}/observable'
    payload, files_obj = build_observable_payload(params)
    return hive_obj.make_api_call(endpoint, payload=payload, files=files_obj)


def get_observable(config, params):
    hive_obj = TheHive(config)
    observable_id = params.get('observableId')
    endpoint = f'/api/v1/observable/{observable_id}'
    return hive_obj.make_api_call(endpoint, method='GET')


def update_observable(config, params):
    hive_obj = TheHive(config)
    additional_field = params.pop('additional_field', {})
    action_type = params.pop('action_type', {})
    data_type = params.get('dataType', '').lower()
    params['dataType'] = data_type
    if action_type == 'Single Record Update':
        observable_id = params.pop('observable_id', '')
        endpoint = f'/api/v1/observable/{observable_id}'
    else:
        observable_ids = params.pop('observable_ids', '')
        if isinstance(observable_ids, str):
            observable_ids = observable_ids.split(',')
            observable_ids = [observable_id.strip() for observable_id in observable_ids if observable_id != '']
        else:
            observable_ids = list(observable_ids)
        params['ids'] = observable_ids
        endpoint = '/api/v1/case/_bulk'
    if additional_field:
        params = {**params, **additional_field}
    params = {k: v for k, v in params.items() if v is not None and v != ''}
    payload = json.dumps(params)
    return hive_obj.make_api_call(endpoint, method='PATCH', payload=payload)


def delete_observable(config, params):
    hive_obj = TheHive(config)
    observable_id = params.get('observableId')
    endpoint = f'/api/v1/observable/{observable_id}'
    return hive_obj.make_api_call(endpoint, method='DELETE')


def create_task(config, params):
    hive_obj = TheHive(config)
    case_id = params.pop('caseId', '')
    additional_field = params.pop('additional_field', {})
    if additional_field:
        params = {**params, **additional_field}
    params = {k: v for k, v in params.items() if v is not None and v != ''}
    payload = json.dumps(params)
    endpoint = f'/api/v1/case/{case_id}/task'
    return hive_obj.make_api_call(endpoint, payload=payload)


def get_task(config, params):
    hive_obj = TheHive(config)
    task_id = params.get('TaskID')
    endpoint = f'/api/v1/task/{task_id}'
    return hive_obj.make_api_call(endpoint, method='GET')


def update_task(config, params):
    hive_obj = TheHive(config)
    action_type = params.pop('action_type', {})
    if action_type == 'Single Record Update':
        task_id = params.pop('taskID', '')
        endpoint = f'/api/v1/task/{task_id}'
    else:
        task_ids = params.pop('taskIDs', '')
        if isinstance(task_ids, str):
            task_ids = task_ids.split(',')
            task_ids = [task_id.strip() for task_id in task_ids if task_id != '']
        else:
            task_ids = list(task_ids)
        params['ids'] = task_ids
        endpoint = f'/api/v1/task/_bulk'
    additional_field = params.pop('additional_field', {})
    if additional_field:
        params = {**params, **additional_field}
    params = {k: v for k, v in params.items() if v is not None and v != ''}
    payload = json.dumps(params)
    return hive_obj.make_api_call(endpoint, method='PATCH', payload=payload)


def delete_task(config, params):
    hive_obj = TheHive(config)
    task_id = params.get('taskID')
    endpoint = f'/api/v1/task/{task_id}'
    return hive_obj.make_api_call(endpoint, method='DELETE')


def _check_health(config):
    hive_obj = TheHive(config)
    return hive_obj.make_api_call('/api/v1/caseReport/formats', method='GET')


operations = {
    'create_alert': create_alert,
    'get_alert': get_alert,
    'update_alerts': update_alerts,
    'delete_alert': delete_alert,
    'add_alert_attachment': add_alert_attachment,
    'get_alert_attachment': get_alert_attachment,
    'delete_alert_attachment': delete_alert_attachment,
    'download_alert_attachment': download_alert_attachment,
    'create_case': create_case,
    'get_case': get_case,
    'update_case': update_case,
    'delete_case': delete_case,
    'create_observable_in_case': create_observable_in_case,
    'create_observable_in_alert': create_observable_in_alert,
    'get_observable': get_observable,
    'update_observable': update_observable,
    'delete_observable': delete_observable,
    'create_task': create_task,
    'get_task': get_task,
    'update_task': update_task,
    'delete_task': delete_task

}
