# rma.RmaApi

All URIs are relative to *https://rma.api.gogemini.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_note**](RmaApi.md#add_note) | **POST** /rma.Rma/AddNote | Add a note to an RMA
[**approve_return**](RmaApi.md#approve_return) | **POST** /rma.Rma/ApproveReturn | Approve a return
[**cancel_return**](RmaApi.md#cancel_return) | **POST** /rma.Rma/CancelReturn | Cancel a return
[**confirm_return_approve_items**](RmaApi.md#confirm_return_approve_items) | **POST** /rma.Rma/ConfirmReturnApproveItems | Confirm return approve items
[**create_return**](RmaApi.md#create_return) | **POST** /rma.Rma/CreateReturn | Create a return
[**delete_note**](RmaApi.md#delete_note) | **POST** /rma.Rma/DeleteNote | Delete a note from an RMA
[**edit_note**](RmaApi.md#edit_note) | **POST** /rma.Rma/EditNote | Edit a note on an RMA
[**get_return**](RmaApi.md#get_return) | **POST** /rma.Rma/GetReturn | Get a return
[**list_notes_by_return_id**](RmaApi.md#list_notes_by_return_id) | **POST** /rma.Rma/ListNotesByReturnId | List notes by return id
[**list_returns**](RmaApi.md#list_returns) | **POST** /rma.Rma/ListReturns | List returns
[**refund_return**](RmaApi.md#refund_return) | **POST** /rma.Rma/RefundReturn | Refund a return
[**reject_return**](RmaApi.md#reject_return) | **POST** /rma.Rma/RejectReturn | Reject a return
[**set_received_items**](RmaApi.md#set_received_items) | **POST** /rma.Rma/SetReceivedItems | Set received items
[**skip_return_status**](RmaApi.md#skip_return_status) | **POST** /rma.Rma/SkipReturnStatus | Skip a return status


# **add_note**
> RmaNoteResponse add_note(body)

Add a note to an RMA

### Example


```python
import time
import os
import rma
from rma.models.rma_add_note_request import RmaAddNoteRequest
from rma.models.rma_note_response import RmaNoteResponse
from rma.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rma.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = rma.Configuration(
    host = "https://rma.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with rma.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rma.RmaApi(api_client)
    body = rma.RmaAddNoteRequest() # RmaAddNoteRequest | 

    try:
        # Add a note to an RMA
        api_response = api_instance.add_note(body)
        print("The response of RmaApi->add_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RmaApi->add_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RmaAddNoteRequest**](RmaAddNoteRequest.md)|  | 

### Return type

[**RmaNoteResponse**](RmaNoteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **approve_return**
> RpcStatus approve_return(body)

Approve a return

### Example


```python
import time
import os
import rma
from rma.models.rma_approve_return_request import RmaApproveReturnRequest
from rma.models.rpc_status import RpcStatus
from rma.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rma.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = rma.Configuration(
    host = "https://rma.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with rma.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rma.RmaApi(api_client)
    body = rma.RmaApproveReturnRequest() # RmaApproveReturnRequest | 

    try:
        # Approve a return
        api_response = api_instance.approve_return(body)
        print("The response of RmaApi->approve_return:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RmaApi->approve_return: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RmaApproveReturnRequest**](RmaApproveReturnRequest.md)|  | 

### Return type

[**RpcStatus**](RpcStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_return**
> object cancel_return(body)

Cancel a return

### Example


```python
import time
import os
import rma
from rma.models.rma_cancel_return_request import RmaCancelReturnRequest
from rma.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rma.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = rma.Configuration(
    host = "https://rma.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with rma.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rma.RmaApi(api_client)
    body = rma.RmaCancelReturnRequest() # RmaCancelReturnRequest | 

    try:
        # Cancel a return
        api_response = api_instance.cancel_return(body)
        print("The response of RmaApi->cancel_return:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RmaApi->cancel_return: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RmaCancelReturnRequest**](RmaCancelReturnRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_return_approve_items**
> object confirm_return_approve_items(body)

Confirm return approve items

### Example


```python
import time
import os
import rma
from rma.models.rma_confirm_return_approve_items_request import RmaConfirmReturnApproveItemsRequest
from rma.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rma.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = rma.Configuration(
    host = "https://rma.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with rma.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rma.RmaApi(api_client)
    body = rma.RmaConfirmReturnApproveItemsRequest() # RmaConfirmReturnApproveItemsRequest | 

    try:
        # Confirm return approve items
        api_response = api_instance.confirm_return_approve_items(body)
        print("The response of RmaApi->confirm_return_approve_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RmaApi->confirm_return_approve_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RmaConfirmReturnApproveItemsRequest**](RmaConfirmReturnApproveItemsRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_return**
> RmaReturnResponse create_return(body)

Create a return

### Example


```python
import time
import os
import rma
from rma.models.rma_create_return_request import RmaCreateReturnRequest
from rma.models.rma_return_response import RmaReturnResponse
from rma.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rma.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = rma.Configuration(
    host = "https://rma.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with rma.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rma.RmaApi(api_client)
    body = rma.RmaCreateReturnRequest() # RmaCreateReturnRequest | 

    try:
        # Create a return
        api_response = api_instance.create_return(body)
        print("The response of RmaApi->create_return:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RmaApi->create_return: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RmaCreateReturnRequest**](RmaCreateReturnRequest.md)|  | 

### Return type

[**RmaReturnResponse**](RmaReturnResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_note**
> object delete_note(body)

Delete a note from an RMA

### Example


```python
import time
import os
import rma
from rma.models.rma_delete_note_request import RmaDeleteNoteRequest
from rma.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rma.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = rma.Configuration(
    host = "https://rma.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with rma.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rma.RmaApi(api_client)
    body = rma.RmaDeleteNoteRequest() # RmaDeleteNoteRequest | 

    try:
        # Delete a note from an RMA
        api_response = api_instance.delete_note(body)
        print("The response of RmaApi->delete_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RmaApi->delete_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RmaDeleteNoteRequest**](RmaDeleteNoteRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_note**
> RmaNoteResponse edit_note(body)

Edit a note on an RMA

### Example


```python
import time
import os
import rma
from rma.models.rma_edit_note_request import RmaEditNoteRequest
from rma.models.rma_note_response import RmaNoteResponse
from rma.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rma.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = rma.Configuration(
    host = "https://rma.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with rma.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rma.RmaApi(api_client)
    body = rma.RmaEditNoteRequest() # RmaEditNoteRequest | 

    try:
        # Edit a note on an RMA
        api_response = api_instance.edit_note(body)
        print("The response of RmaApi->edit_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RmaApi->edit_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RmaEditNoteRequest**](RmaEditNoteRequest.md)|  | 

### Return type

[**RmaNoteResponse**](RmaNoteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_return**
> RmaReturnResponse get_return(body)

Get a return

### Example


```python
import time
import os
import rma
from rma.models.rma_get_return_request import RmaGetReturnRequest
from rma.models.rma_return_response import RmaReturnResponse
from rma.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rma.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = rma.Configuration(
    host = "https://rma.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with rma.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rma.RmaApi(api_client)
    body = rma.RmaGetReturnRequest() # RmaGetReturnRequest | 

    try:
        # Get a return
        api_response = api_instance.get_return(body)
        print("The response of RmaApi->get_return:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RmaApi->get_return: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RmaGetReturnRequest**](RmaGetReturnRequest.md)|  | 

### Return type

[**RmaReturnResponse**](RmaReturnResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_notes_by_return_id**
> RmaListNotesByReturnIdResponse list_notes_by_return_id(body)

List notes by return id

### Example


```python
import time
import os
import rma
from rma.models.rma_list_notes_by_return_id_request import RmaListNotesByReturnIdRequest
from rma.models.rma_list_notes_by_return_id_response import RmaListNotesByReturnIdResponse
from rma.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rma.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = rma.Configuration(
    host = "https://rma.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with rma.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rma.RmaApi(api_client)
    body = rma.RmaListNotesByReturnIdRequest() # RmaListNotesByReturnIdRequest | 

    try:
        # List notes by return id
        api_response = api_instance.list_notes_by_return_id(body)
        print("The response of RmaApi->list_notes_by_return_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RmaApi->list_notes_by_return_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RmaListNotesByReturnIdRequest**](RmaListNotesByReturnIdRequest.md)|  | 

### Return type

[**RmaListNotesByReturnIdResponse**](RmaListNotesByReturnIdResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_returns**
> RmaListReturnsResponse list_returns(body)

List returns

### Example


```python
import time
import os
import rma
from rma.models.rma_list_returns_request import RmaListReturnsRequest
from rma.models.rma_list_returns_response import RmaListReturnsResponse
from rma.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rma.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = rma.Configuration(
    host = "https://rma.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with rma.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rma.RmaApi(api_client)
    body = rma.RmaListReturnsRequest() # RmaListReturnsRequest | 

    try:
        # List returns
        api_response = api_instance.list_returns(body)
        print("The response of RmaApi->list_returns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RmaApi->list_returns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RmaListReturnsRequest**](RmaListReturnsRequest.md)|  | 

### Return type

[**RmaListReturnsResponse**](RmaListReturnsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refund_return**
> object refund_return(body)

Refund a return

### Example


```python
import time
import os
import rma
from rma.models.rma_refund_return_request import RmaRefundReturnRequest
from rma.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rma.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = rma.Configuration(
    host = "https://rma.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with rma.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rma.RmaApi(api_client)
    body = rma.RmaRefundReturnRequest() # RmaRefundReturnRequest | 

    try:
        # Refund a return
        api_response = api_instance.refund_return(body)
        print("The response of RmaApi->refund_return:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RmaApi->refund_return: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RmaRefundReturnRequest**](RmaRefundReturnRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reject_return**
> object reject_return(body)

Reject a return

### Example


```python
import time
import os
import rma
from rma.models.rma_reject_return_request import RmaRejectReturnRequest
from rma.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rma.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = rma.Configuration(
    host = "https://rma.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with rma.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rma.RmaApi(api_client)
    body = rma.RmaRejectReturnRequest() # RmaRejectReturnRequest | 

    try:
        # Reject a return
        api_response = api_instance.reject_return(body)
        print("The response of RmaApi->reject_return:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RmaApi->reject_return: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RmaRejectReturnRequest**](RmaRejectReturnRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_received_items**
> object set_received_items(body)

Set received items

### Example


```python
import time
import os
import rma
from rma.models.rma_set_received_items_request import RmaSetReceivedItemsRequest
from rma.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rma.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = rma.Configuration(
    host = "https://rma.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with rma.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rma.RmaApi(api_client)
    body = rma.RmaSetReceivedItemsRequest() # RmaSetReceivedItemsRequest | 

    try:
        # Set received items
        api_response = api_instance.set_received_items(body)
        print("The response of RmaApi->set_received_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RmaApi->set_received_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RmaSetReceivedItemsRequest**](RmaSetReceivedItemsRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **skip_return_status**
> object skip_return_status(body)

Skip a return status

### Example


```python
import time
import os
import rma
from rma.models.rma_skip_return_status_request import RmaSkipReturnStatusRequest
from rma.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rma.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = rma.Configuration(
    host = "https://rma.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with rma.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rma.RmaApi(api_client)
    body = rma.RmaSkipReturnStatusRequest() # RmaSkipReturnStatusRequest | 

    try:
        # Skip a return status
        api_response = api_instance.skip_return_status(body)
        print("The response of RmaApi->skip_return_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RmaApi->skip_return_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RmaSkipReturnStatusRequest**](RmaSkipReturnStatusRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

