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
import abc
from typing import Awaitable, Callable, Dict, Optional, Sequence, Union

import google.api_core
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
import google.auth  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2
from google.oauth2 import service_account  # type: ignore

from google.cloud.dialogflow_v2beta1 import gapic_version as package_version
from google.cloud.dialogflow_v2beta1.types import participant as gcd_participant
from google.cloud.dialogflow_v2beta1.types import participant

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)


class ParticipantsTransport(abc.ABC):
    """Abstract transport class for Participants."""

    AUTH_SCOPES = (
        "https://www.googleapis.com/auth/cloud-platform",
        "https://www.googleapis.com/auth/dialogflow",
    )

    DEFAULT_HOST: str = "dialogflow.googleapis.com"

    def __init__(
        self,
        *,
        host: str = DEFAULT_HOST,
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        api_audience: Optional[str] = None,
        **kwargs,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A list of scopes.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
        """

        scopes_kwargs = {"scopes": scopes, "default_scopes": self.AUTH_SCOPES}

        # Save the scopes.
        self._scopes = scopes

        # If no credentials are provided, then determine the appropriate
        # defaults.
        if credentials and credentials_file:
            raise core_exceptions.DuplicateCredentialArgs(
                "'credentials_file' and 'credentials' are mutually exclusive"
            )

        if credentials_file is not None:
            credentials, _ = google.auth.load_credentials_from_file(
                credentials_file, **scopes_kwargs, quota_project_id=quota_project_id
            )
        elif credentials is None:
            credentials, _ = google.auth.default(
                **scopes_kwargs, quota_project_id=quota_project_id
            )
            # Don't apply audience if the credentials file passed from user.
            if hasattr(credentials, "with_gdch_audience"):
                credentials = credentials.with_gdch_audience(
                    api_audience if api_audience else host
                )

        # If the credentials are service account credentials, then always try to use self signed JWT.
        if (
            always_use_jwt_access
            and isinstance(credentials, service_account.Credentials)
            and hasattr(service_account.Credentials, "with_always_use_jwt_access")
        ):
            credentials = credentials.with_always_use_jwt_access(True)

        # Save the credentials.
        self._credentials = credentials

        # Save the hostname. Default to port 443 (HTTPS) if none is specified.
        if ":" not in host:
            host += ":443"
        self._host = host

    def _prep_wrapped_messages(self, client_info):
        # Precompute the wrapped methods.
        self._wrapped_methods = {
            self.create_participant: gapic_v1.method.wrap_method(
                self.create_participant,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_participant: gapic_v1.method.wrap_method(
                self.get_participant,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_participants: gapic_v1.method.wrap_method(
                self.list_participants,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_participant: gapic_v1.method.wrap_method(
                self.update_participant,
                default_timeout=None,
                client_info=client_info,
            ),
            self.analyze_content: gapic_v1.method.wrap_method(
                self.analyze_content,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=220.0,
                ),
                default_timeout=220.0,
                client_info=client_info,
            ),
            self.streaming_analyze_content: gapic_v1.method.wrap_method(
                self.streaming_analyze_content,
                default_timeout=220.0,
                client_info=client_info,
            ),
            self.suggest_articles: gapic_v1.method.wrap_method(
                self.suggest_articles,
                default_timeout=None,
                client_info=client_info,
            ),
            self.suggest_faq_answers: gapic_v1.method.wrap_method(
                self.suggest_faq_answers,
                default_timeout=None,
                client_info=client_info,
            ),
            self.suggest_smart_replies: gapic_v1.method.wrap_method(
                self.suggest_smart_replies,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_suggestions: gapic_v1.method.wrap_method(
                self.list_suggestions,
                default_timeout=None,
                client_info=client_info,
            ),
            self.compile_suggestion: gapic_v1.method.wrap_method(
                self.compile_suggestion,
                default_timeout=None,
                client_info=client_info,
            ),
        }

    def close(self):
        """Closes resources associated with the transport.

        .. warning::
             Only call this method if the transport is NOT shared
             with other clients - this may cause errors in other clients!
        """
        raise NotImplementedError()

    @property
    def create_participant(
        self,
    ) -> Callable[
        [gcd_participant.CreateParticipantRequest],
        Union[gcd_participant.Participant, Awaitable[gcd_participant.Participant]],
    ]:
        raise NotImplementedError()

    @property
    def get_participant(
        self,
    ) -> Callable[
        [participant.GetParticipantRequest],
        Union[participant.Participant, Awaitable[participant.Participant]],
    ]:
        raise NotImplementedError()

    @property
    def list_participants(
        self,
    ) -> Callable[
        [participant.ListParticipantsRequest],
        Union[
            participant.ListParticipantsResponse,
            Awaitable[participant.ListParticipantsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_participant(
        self,
    ) -> Callable[
        [gcd_participant.UpdateParticipantRequest],
        Union[gcd_participant.Participant, Awaitable[gcd_participant.Participant]],
    ]:
        raise NotImplementedError()

    @property
    def analyze_content(
        self,
    ) -> Callable[
        [gcd_participant.AnalyzeContentRequest],
        Union[
            gcd_participant.AnalyzeContentResponse,
            Awaitable[gcd_participant.AnalyzeContentResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def streaming_analyze_content(
        self,
    ) -> Callable[
        [participant.StreamingAnalyzeContentRequest],
        Union[
            participant.StreamingAnalyzeContentResponse,
            Awaitable[participant.StreamingAnalyzeContentResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def suggest_articles(
        self,
    ) -> Callable[
        [participant.SuggestArticlesRequest],
        Union[
            participant.SuggestArticlesResponse,
            Awaitable[participant.SuggestArticlesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def suggest_faq_answers(
        self,
    ) -> Callable[
        [participant.SuggestFaqAnswersRequest],
        Union[
            participant.SuggestFaqAnswersResponse,
            Awaitable[participant.SuggestFaqAnswersResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def suggest_smart_replies(
        self,
    ) -> Callable[
        [participant.SuggestSmartRepliesRequest],
        Union[
            participant.SuggestSmartRepliesResponse,
            Awaitable[participant.SuggestSmartRepliesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_suggestions(
        self,
    ) -> Callable[
        [participant.ListSuggestionsRequest],
        Union[
            participant.ListSuggestionsResponse,
            Awaitable[participant.ListSuggestionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def compile_suggestion(
        self,
    ) -> Callable[
        [participant.CompileSuggestionRequest],
        Union[
            participant.CompileSuggestionResponse,
            Awaitable[participant.CompileSuggestionResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_operations(
        self,
    ) -> Callable[
        [operations_pb2.ListOperationsRequest],
        Union[
            operations_pb2.ListOperationsResponse,
            Awaitable[operations_pb2.ListOperationsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_operation(
        self,
    ) -> Callable[
        [operations_pb2.GetOperationRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def cancel_operation(
        self,
    ) -> Callable[[operations_pb2.CancelOperationRequest], None,]:
        raise NotImplementedError()

    @property
    def get_location(
        self,
    ) -> Callable[
        [locations_pb2.GetLocationRequest],
        Union[locations_pb2.Location, Awaitable[locations_pb2.Location]],
    ]:
        raise NotImplementedError()

    @property
    def list_locations(
        self,
    ) -> Callable[
        [locations_pb2.ListLocationsRequest],
        Union[
            locations_pb2.ListLocationsResponse,
            Awaitable[locations_pb2.ListLocationsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def kind(self) -> str:
        raise NotImplementedError()


__all__ = ("ParticipantsTransport",)