# -*- coding: utf-8 -*-
# Copyright 2024 Google LLC
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
import dataclasses
import json  # type: ignore
import logging
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union
import warnings

from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.protobuf import empty_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.shopping.merchant_reviews_v1beta.types import merchantreviews

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseMerchantReviewsServiceRestTransport

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object, None]  # type: ignore

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = logging.getLogger(__name__)

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=BASE_DEFAULT_CLIENT_INFO.gapic_version,
    grpc_version=None,
    rest_version=f"requests@{requests_version}",
)


class MerchantReviewsServiceRestInterceptor:
    """Interceptor for MerchantReviewsService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the MerchantReviewsServiceRestTransport.

    .. code-block:: python
        class MyCustomMerchantReviewsServiceInterceptor(MerchantReviewsServiceRestInterceptor):
            def pre_delete_merchant_review(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_merchant_review(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_merchant_review(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_insert_merchant_review(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_insert_merchant_review(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_merchant_reviews(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_merchant_reviews(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = MerchantReviewsServiceRestTransport(interceptor=MyCustomMerchantReviewsServiceInterceptor())
        client = MerchantReviewsServiceClient(transport=transport)


    """

    def pre_delete_merchant_review(
        self,
        request: merchantreviews.DeleteMerchantReviewRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        merchantreviews.DeleteMerchantReviewRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_merchant_review

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MerchantReviewsService server.
        """
        return request, metadata

    def pre_get_merchant_review(
        self,
        request: merchantreviews.GetMerchantReviewRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        merchantreviews.GetMerchantReviewRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_merchant_review

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MerchantReviewsService server.
        """
        return request, metadata

    def post_get_merchant_review(
        self, response: merchantreviews.MerchantReview
    ) -> merchantreviews.MerchantReview:
        """Post-rpc interceptor for get_merchant_review

        Override in a subclass to manipulate the response
        after it is returned by the MerchantReviewsService server but before
        it is returned to user code.
        """
        return response

    def pre_insert_merchant_review(
        self,
        request: merchantreviews.InsertMerchantReviewRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        merchantreviews.InsertMerchantReviewRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for insert_merchant_review

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MerchantReviewsService server.
        """
        return request, metadata

    def post_insert_merchant_review(
        self, response: merchantreviews.MerchantReview
    ) -> merchantreviews.MerchantReview:
        """Post-rpc interceptor for insert_merchant_review

        Override in a subclass to manipulate the response
        after it is returned by the MerchantReviewsService server but before
        it is returned to user code.
        """
        return response

    def pre_list_merchant_reviews(
        self,
        request: merchantreviews.ListMerchantReviewsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        merchantreviews.ListMerchantReviewsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_merchant_reviews

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MerchantReviewsService server.
        """
        return request, metadata

    def post_list_merchant_reviews(
        self, response: merchantreviews.ListMerchantReviewsResponse
    ) -> merchantreviews.ListMerchantReviewsResponse:
        """Post-rpc interceptor for list_merchant_reviews

        Override in a subclass to manipulate the response
        after it is returned by the MerchantReviewsService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class MerchantReviewsServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: MerchantReviewsServiceRestInterceptor


class MerchantReviewsServiceRestTransport(_BaseMerchantReviewsServiceRestTransport):
    """REST backend synchronous transport for MerchantReviewsService.

    Service to manage merchant reviews.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "merchantapi.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[MerchantReviewsServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'merchantapi.googleapis.com').
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.

            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Callable[[], Tuple[bytes, bytes]]): Client
                certificate to configure mutual TLS HTTP channel. It is ignored
                if ``channel`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you are developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
            url_scheme: the protocol scheme for the API endpoint.  Normally
                "https", but for testing or local servers,
                "http" can be specified.
        """
        # Run the base constructor
        # TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.
        # TODO: When custom host (api_endpoint) is set, `scopes` must *also* be set on the
        # credentials object
        super().__init__(
            host=host,
            credentials=credentials,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            url_scheme=url_scheme,
            api_audience=api_audience,
        )
        self._session = AuthorizedSession(
            self._credentials, default_host=self.DEFAULT_HOST
        )
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = interceptor or MerchantReviewsServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _DeleteMerchantReview(
        _BaseMerchantReviewsServiceRestTransport._BaseDeleteMerchantReview,
        MerchantReviewsServiceRestStub,
    ):
        def __hash__(self):
            return hash("MerchantReviewsServiceRestTransport.DeleteMerchantReview")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: merchantreviews.DeleteMerchantReviewRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete merchant review method over HTTP.

            Args:
                request (~.merchantreviews.DeleteMerchantReviewRequest):
                    The request object. Request message for the ``DeleteMerchantReview`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseMerchantReviewsServiceRestTransport._BaseDeleteMerchantReview._get_http_options()
            )

            request, metadata = self._interceptor.pre_delete_merchant_review(
                request, metadata
            )
            transcoded_request = _BaseMerchantReviewsServiceRestTransport._BaseDeleteMerchantReview._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseMerchantReviewsServiceRestTransport._BaseDeleteMerchantReview._get_query_params_json(
                transcoded_request
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.shopping.merchant.reviews_v1beta.MerchantReviewsServiceClient.DeleteMerchantReview",
                    extra={
                        "serviceName": "google.shopping.merchant.reviews.v1beta.MerchantReviewsService",
                        "rpcName": "DeleteMerchantReview",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                MerchantReviewsServiceRestTransport._DeleteMerchantReview._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

    class _GetMerchantReview(
        _BaseMerchantReviewsServiceRestTransport._BaseGetMerchantReview,
        MerchantReviewsServiceRestStub,
    ):
        def __hash__(self):
            return hash("MerchantReviewsServiceRestTransport.GetMerchantReview")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: merchantreviews.GetMerchantReviewRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> merchantreviews.MerchantReview:
            r"""Call the get merchant review method over HTTP.

            Args:
                request (~.merchantreviews.GetMerchantReviewRequest):
                    The request object. Request message for the ``GetMerchantReview`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.merchantreviews.MerchantReview:
                    A review for a merchant. For more information, see
                `Introduction to Merchant Review
                Feeds <https://developers.google.com/merchant-review-feeds>`__

            """

            http_options = (
                _BaseMerchantReviewsServiceRestTransport._BaseGetMerchantReview._get_http_options()
            )

            request, metadata = self._interceptor.pre_get_merchant_review(
                request, metadata
            )
            transcoded_request = _BaseMerchantReviewsServiceRestTransport._BaseGetMerchantReview._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseMerchantReviewsServiceRestTransport._BaseGetMerchantReview._get_query_params_json(
                transcoded_request
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.shopping.merchant.reviews_v1beta.MerchantReviewsServiceClient.GetMerchantReview",
                    extra={
                        "serviceName": "google.shopping.merchant.reviews.v1beta.MerchantReviewsService",
                        "rpcName": "GetMerchantReview",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                MerchantReviewsServiceRestTransport._GetMerchantReview._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = merchantreviews.MerchantReview()
            pb_resp = merchantreviews.MerchantReview.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_merchant_review(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = merchantreviews.MerchantReview.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.shopping.merchant.reviews_v1beta.MerchantReviewsServiceClient.get_merchant_review",
                    extra={
                        "serviceName": "google.shopping.merchant.reviews.v1beta.MerchantReviewsService",
                        "rpcName": "GetMerchantReview",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _InsertMerchantReview(
        _BaseMerchantReviewsServiceRestTransport._BaseInsertMerchantReview,
        MerchantReviewsServiceRestStub,
    ):
        def __hash__(self):
            return hash("MerchantReviewsServiceRestTransport.InsertMerchantReview")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: merchantreviews.InsertMerchantReviewRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> merchantreviews.MerchantReview:
            r"""Call the insert merchant review method over HTTP.

            Args:
                request (~.merchantreviews.InsertMerchantReviewRequest):
                    The request object. Request message for the ``InsertMerchantReview`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.merchantreviews.MerchantReview:
                    A review for a merchant. For more information, see
                `Introduction to Merchant Review
                Feeds <https://developers.google.com/merchant-review-feeds>`__

            """

            http_options = (
                _BaseMerchantReviewsServiceRestTransport._BaseInsertMerchantReview._get_http_options()
            )

            request, metadata = self._interceptor.pre_insert_merchant_review(
                request, metadata
            )
            transcoded_request = _BaseMerchantReviewsServiceRestTransport._BaseInsertMerchantReview._get_transcoded_request(
                http_options, request
            )

            body = _BaseMerchantReviewsServiceRestTransport._BaseInsertMerchantReview._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = _BaseMerchantReviewsServiceRestTransport._BaseInsertMerchantReview._get_query_params_json(
                transcoded_request
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.shopping.merchant.reviews_v1beta.MerchantReviewsServiceClient.InsertMerchantReview",
                    extra={
                        "serviceName": "google.shopping.merchant.reviews.v1beta.MerchantReviewsService",
                        "rpcName": "InsertMerchantReview",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                MerchantReviewsServiceRestTransport._InsertMerchantReview._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    body,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = merchantreviews.MerchantReview()
            pb_resp = merchantreviews.MerchantReview.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_insert_merchant_review(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = merchantreviews.MerchantReview.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.shopping.merchant.reviews_v1beta.MerchantReviewsServiceClient.insert_merchant_review",
                    extra={
                        "serviceName": "google.shopping.merchant.reviews.v1beta.MerchantReviewsService",
                        "rpcName": "InsertMerchantReview",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListMerchantReviews(
        _BaseMerchantReviewsServiceRestTransport._BaseListMerchantReviews,
        MerchantReviewsServiceRestStub,
    ):
        def __hash__(self):
            return hash("MerchantReviewsServiceRestTransport.ListMerchantReviews")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: merchantreviews.ListMerchantReviewsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> merchantreviews.ListMerchantReviewsResponse:
            r"""Call the list merchant reviews method over HTTP.

            Args:
                request (~.merchantreviews.ListMerchantReviewsRequest):
                    The request object. Request message for the ``ListMerchantsReview`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.merchantreviews.ListMerchantReviewsResponse:
                    Response message for the ``ListMerchantsReview`` method.
            """

            http_options = (
                _BaseMerchantReviewsServiceRestTransport._BaseListMerchantReviews._get_http_options()
            )

            request, metadata = self._interceptor.pre_list_merchant_reviews(
                request, metadata
            )
            transcoded_request = _BaseMerchantReviewsServiceRestTransport._BaseListMerchantReviews._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseMerchantReviewsServiceRestTransport._BaseListMerchantReviews._get_query_params_json(
                transcoded_request
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.shopping.merchant.reviews_v1beta.MerchantReviewsServiceClient.ListMerchantReviews",
                    extra={
                        "serviceName": "google.shopping.merchant.reviews.v1beta.MerchantReviewsService",
                        "rpcName": "ListMerchantReviews",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                MerchantReviewsServiceRestTransport._ListMerchantReviews._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = merchantreviews.ListMerchantReviewsResponse()
            pb_resp = merchantreviews.ListMerchantReviewsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_merchant_reviews(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        merchantreviews.ListMerchantReviewsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.shopping.merchant.reviews_v1beta.MerchantReviewsServiceClient.list_merchant_reviews",
                    extra={
                        "serviceName": "google.shopping.merchant.reviews.v1beta.MerchantReviewsService",
                        "rpcName": "ListMerchantReviews",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def delete_merchant_review(
        self,
    ) -> Callable[[merchantreviews.DeleteMerchantReviewRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteMerchantReview(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_merchant_review(
        self,
    ) -> Callable[
        [merchantreviews.GetMerchantReviewRequest], merchantreviews.MerchantReview
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetMerchantReview(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def insert_merchant_review(
        self,
    ) -> Callable[
        [merchantreviews.InsertMerchantReviewRequest], merchantreviews.MerchantReview
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._InsertMerchantReview(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_merchant_reviews(
        self,
    ) -> Callable[
        [merchantreviews.ListMerchantReviewsRequest],
        merchantreviews.ListMerchantReviewsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListMerchantReviews(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("MerchantReviewsServiceRestTransport",)