# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from collections import OrderedDict
import functools
import re
from typing import (
    Dict,
    Mapping,
    MutableMapping,
    MutableSequence,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
)

from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.metastore_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.api_core import operation  # type: ignore
from google.api_core import operation_async  # type: ignore
from google.protobuf import empty_pb2  # type: ignore
from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore

from google.cloud.metastore_v1.services.dataproc_metastore_federation import pagers
from google.cloud.metastore_v1.types import metastore, metastore_federation

from .client import DataprocMetastoreFederationClient
from .transports.base import DEFAULT_CLIENT_INFO, DataprocMetastoreFederationTransport
from .transports.grpc_asyncio import DataprocMetastoreFederationGrpcAsyncIOTransport


class DataprocMetastoreFederationAsyncClient:
    """Configures and manages metastore federation services. Dataproc
    Metastore Federation Service allows federating a collection of
    backend metastores like BigQuery, Dataplex Lakes, and other Dataproc
    Metastores. The Federation Service exposes a gRPC URL through which
    metadata from the backend metastores are served at query time.

    The Dataproc Metastore Federation API defines the following resource
    model:

    -  The service works with a collection of Google Cloud projects.
    -  Each project has a collection of available locations.
    -  Each location has a collection of federations.
    -  Dataproc Metastore Federations are resources with names of the
       form:
       ``projects/{project_number}/locations/{location_id}/federations/{federation_id}``.
    """

    _client: DataprocMetastoreFederationClient

    DEFAULT_ENDPOINT = DataprocMetastoreFederationClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = DataprocMetastoreFederationClient.DEFAULT_MTLS_ENDPOINT

    federation_path = staticmethod(DataprocMetastoreFederationClient.federation_path)
    parse_federation_path = staticmethod(
        DataprocMetastoreFederationClient.parse_federation_path
    )
    common_billing_account_path = staticmethod(
        DataprocMetastoreFederationClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        DataprocMetastoreFederationClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(
        DataprocMetastoreFederationClient.common_folder_path
    )
    parse_common_folder_path = staticmethod(
        DataprocMetastoreFederationClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        DataprocMetastoreFederationClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        DataprocMetastoreFederationClient.parse_common_organization_path
    )
    common_project_path = staticmethod(
        DataprocMetastoreFederationClient.common_project_path
    )
    parse_common_project_path = staticmethod(
        DataprocMetastoreFederationClient.parse_common_project_path
    )
    common_location_path = staticmethod(
        DataprocMetastoreFederationClient.common_location_path
    )
    parse_common_location_path = staticmethod(
        DataprocMetastoreFederationClient.parse_common_location_path
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            DataprocMetastoreFederationAsyncClient: The constructed client.
        """
        return DataprocMetastoreFederationClient.from_service_account_info.__func__(DataprocMetastoreFederationAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            DataprocMetastoreFederationAsyncClient: The constructed client.
        """
        return DataprocMetastoreFederationClient.from_service_account_file.__func__(DataprocMetastoreFederationAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[ClientOptions] = None
    ):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variabel is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return DataprocMetastoreFederationClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> DataprocMetastoreFederationTransport:
        """Returns the transport used by the client instance.

        Returns:
            DataprocMetastoreFederationTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(DataprocMetastoreFederationClient).get_transport_class,
        type(DataprocMetastoreFederationClient),
    )

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Union[str, DataprocMetastoreFederationTransport] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the dataproc metastore federation client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.DataprocMetastoreFederationTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = DataprocMetastoreFederationClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def list_federations(
        self,
        request: Optional[
            Union[metastore_federation.ListFederationsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListFederationsAsyncPager:
        r"""Lists federations in a project and location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import metastore_v1

            async def sample_list_federations():
                # Create a client
                client = metastore_v1.DataprocMetastoreFederationAsyncClient()

                # Initialize request argument(s)
                request = metastore_v1.ListFederationsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_federations(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.metastore_v1.types.ListFederationsRequest, dict]]):
                The request object. Request message for ListFederations.
            parent (:class:`str`):
                Required. The relative resource name of the location of
                metastore federations to list, in the following form:
                ``projects/{project_number}/locations/{location_id}``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.metastore_v1.services.dataproc_metastore_federation.pagers.ListFederationsAsyncPager:
                Response message for ListFederations
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = metastore_federation.ListFederationsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_federations,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListFederationsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_federation(
        self,
        request: Optional[
            Union[metastore_federation.GetFederationRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> metastore_federation.Federation:
        r"""Gets the details of a single federation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import metastore_v1

            async def sample_get_federation():
                # Create a client
                client = metastore_v1.DataprocMetastoreFederationAsyncClient()

                # Initialize request argument(s)
                request = metastore_v1.GetFederationRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_federation(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.metastore_v1.types.GetFederationRequest, dict]]):
                The request object. Request message for GetFederation.
            name (:class:`str`):
                Required. The relative resource name of the metastore
                federation to retrieve, in the following form:

                ``projects/{project_number}/locations/{location_id}/federations/{federation_id}``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.metastore_v1.types.Federation:
                Represents a federation of multiple
                backend metastores.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = metastore_federation.GetFederationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_federation,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def create_federation(
        self,
        request: Optional[
            Union[metastore_federation.CreateFederationRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        federation: Optional[metastore_federation.Federation] = None,
        federation_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Creates a metastore federation in a project and
        location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import metastore_v1

            async def sample_create_federation():
                # Create a client
                client = metastore_v1.DataprocMetastoreFederationAsyncClient()

                # Initialize request argument(s)
                request = metastore_v1.CreateFederationRequest(
                    parent="parent_value",
                    federation_id="federation_id_value",
                )

                # Make the request
                operation = client.create_federation(request=request)

                print("Waiting for operation to complete...")

                response = (await operation).result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.metastore_v1.types.CreateFederationRequest, dict]]):
                The request object. Request message for
                CreateFederation.
            parent (:class:`str`):
                Required. The relative resource name of the location in
                which to create a federation service, in the following
                form:

                ``projects/{project_number}/locations/{location_id}``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            federation (:class:`google.cloud.metastore_v1.types.Federation`):
                Required. The Metastore Federation to create. The
                ``name`` field is ignored. The ID of the created
                metastore federation must be provided in the request's
                ``federation_id`` field.

                This corresponds to the ``federation`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            federation_id (:class:`str`):
                Required. The ID of the metastore
                federation, which is used as the final
                component of the metastore federation's
                name.
                This value must be between 2 and 63
                characters long inclusive, begin with a
                letter, end with a letter or number, and
                consist of alpha-numeric ASCII
                characters or hyphens.

                This corresponds to the ``federation_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.metastore_v1.types.Federation`
                Represents a federation of multiple backend metastores.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, federation, federation_id])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = metastore_federation.CreateFederationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if federation is not None:
            request.federation = federation
        if federation_id is not None:
            request.federation_id = federation_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_federation,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            metastore_federation.Federation,
            metadata_type=metastore.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def update_federation(
        self,
        request: Optional[
            Union[metastore_federation.UpdateFederationRequest, dict]
        ] = None,
        *,
        federation: Optional[metastore_federation.Federation] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Updates the fields of a federation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import metastore_v1

            async def sample_update_federation():
                # Create a client
                client = metastore_v1.DataprocMetastoreFederationAsyncClient()

                # Initialize request argument(s)
                request = metastore_v1.UpdateFederationRequest(
                )

                # Make the request
                operation = client.update_federation(request=request)

                print("Waiting for operation to complete...")

                response = (await operation).result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.metastore_v1.types.UpdateFederationRequest, dict]]):
                The request object. Request message for
                UpdateFederation.
            federation (:class:`google.cloud.metastore_v1.types.Federation`):
                Required. The metastore federation to update. The server
                only merges fields in the service if they are specified
                in ``update_mask``.

                The metastore federation's ``name`` field is used to
                identify the metastore service to be updated.

                This corresponds to the ``federation`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Required. A field mask used to specify the fields to be
                overwritten in the metastore federation resource by the
                update. Fields specified in the ``update_mask`` are
                relative to the resource (not to the full request). A
                field is overwritten if it is in the mask.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.metastore_v1.types.Federation`
                Represents a federation of multiple backend metastores.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([federation, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = metastore_federation.UpdateFederationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if federation is not None:
            request.federation = federation
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_federation,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("federation.name", request.federation.name),)
            ),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            metastore_federation.Federation,
            metadata_type=metastore.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def delete_federation(
        self,
        request: Optional[
            Union[metastore_federation.DeleteFederationRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Deletes a single federation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import metastore_v1

            async def sample_delete_federation():
                # Create a client
                client = metastore_v1.DataprocMetastoreFederationAsyncClient()

                # Initialize request argument(s)
                request = metastore_v1.DeleteFederationRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_federation(request=request)

                print("Waiting for operation to complete...")

                response = (await operation).result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.metastore_v1.types.DeleteFederationRequest, dict]]):
                The request object. Request message for
                DeleteFederation.
            name (:class:`str`):
                Required. The relative resource name of the metastore
                federation to delete, in the following form:

                ``projects/{project_number}/locations/{location_id}/federations/{federation_id}``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated
                   empty messages in your APIs. A typical example is to
                   use it as the request or the response type of an API
                   method. For instance:

                      service Foo {
                         rpc Bar(google.protobuf.Empty) returns
                         (google.protobuf.Empty);

                      }

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = metastore_federation.DeleteFederationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_federation,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=metastore.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)


__all__ = ("DataprocMetastoreFederationAsyncClient",)