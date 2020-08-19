# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import map_error

from .. import models


class ServiceOperations(object):
    """ServiceOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar resource: The value must be "account" for all account operations. Constant value: "account".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self._config = config
        self.resource = "account"

    def list_file_systems(self, prefix=None, continuation=None, max_results=None, request_id=None, timeout=None, cls=None, **kwargs):
        """List FileSystems.

        List filesystems and their properties in given account.

        :param prefix: Filters results to filesystems within the specified
         prefix.
        :type prefix: str
        :param continuation: Optional.  When deleting a directory, the number
         of paths that are deleted with each invocation is limited.  If the
         number of paths to be deleted exceeds this limit, a continuation token
         is returned in this response header.  When a continuation token is
         returned in the response, it must be specified in a subsequent
         invocation of the delete operation to continue deleting the directory.
        :type continuation: str
        :param max_results: An optional value that specifies the maximum
         number of items to return. If omitted or greater than 5,000, the
         response will include up to 5,000 items.
        :type max_results: int
        :param request_id: Provides a client-generated, opaque value with a 1
         KB character limit that is recorded in the analytics logs when storage
         analytics logging is enabled.
        :type request_id: str
        :param timeout: The timeout parameter is expressed in seconds. For
         more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>
        :type timeout: int
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: FileSystemList or the result of cls(response)
        :rtype: ~azure.storage.filedatalake.models.FileSystemList
        :raises:
         :class:`StorageErrorException<azure.storage.filedatalake.models.StorageErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.list_file_systems.metadata['url']
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['resource'] = self._serialize.query("self.resource", self.resource, 'str')
        if prefix is not None:
            query_parameters['prefix'] = self._serialize.query("prefix", prefix, 'str')
        if continuation is not None:
            query_parameters['continuation'] = self._serialize.query("continuation", continuation, 'str')
        if max_results is not None:
            query_parameters['maxResults'] = self._serialize.query("max_results", max_results, 'int', minimum=1)
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("request_id", request_id, 'str')
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.StorageErrorException(response, self._deserialize)

        header_dict = {}
        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('FileSystemList', response)
            header_dict = {
                'Date': self._deserialize('rfc-1123', response.headers.get('Date')),
                'x-ms-request-id': self._deserialize('str', response.headers.get('x-ms-request-id')),
                'x-ms-version': self._deserialize('str', response.headers.get('x-ms-version')),
                'x-ms-continuation': self._deserialize('str', response.headers.get('x-ms-continuation')),
                'Content-Type': self._deserialize('str', response.headers.get('Content-Type')),
                'x-ms-error-code': self._deserialize('str', response.headers.get('x-ms-error-code')),
            }

        if cls:
            return cls(response, deserialized, header_dict)

        return deserialized
    list_file_systems.metadata = {'url': '/'}
