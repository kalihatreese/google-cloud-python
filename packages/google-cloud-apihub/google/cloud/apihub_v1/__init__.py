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
from google.cloud.apihub_v1 import gapic_version as package_version

__version__ = package_version.__version__


from .services.api_hub import ApiHubClient
from .services.api_hub_dependencies import ApiHubDependenciesClient
from .services.api_hub_plugin import ApiHubPluginClient
from .services.host_project_registration_service import (
    HostProjectRegistrationServiceClient,
)
from .services.linting_service import LintingServiceClient
from .services.provisioning import ProvisioningClient
from .services.runtime_project_attachment_service import (
    RuntimeProjectAttachmentServiceClient,
)
from .types.apihub_service import (
    ApiHubResource,
    CreateApiRequest,
    CreateAttributeRequest,
    CreateDependencyRequest,
    CreateDeploymentRequest,
    CreateExternalApiRequest,
    CreateSpecRequest,
    CreateVersionRequest,
    DeleteApiRequest,
    DeleteAttributeRequest,
    DeleteDependencyRequest,
    DeleteDeploymentRequest,
    DeleteExternalApiRequest,
    DeleteSpecRequest,
    DeleteVersionRequest,
    GetApiOperationRequest,
    GetApiRequest,
    GetAttributeRequest,
    GetDefinitionRequest,
    GetDependencyRequest,
    GetDeploymentRequest,
    GetExternalApiRequest,
    GetSpecContentsRequest,
    GetSpecRequest,
    GetVersionRequest,
    ListApiOperationsRequest,
    ListApiOperationsResponse,
    ListApisRequest,
    ListApisResponse,
    ListAttributesRequest,
    ListAttributesResponse,
    ListDependenciesRequest,
    ListDependenciesResponse,
    ListDeploymentsRequest,
    ListDeploymentsResponse,
    ListExternalApisRequest,
    ListExternalApisResponse,
    ListSpecsRequest,
    ListSpecsResponse,
    ListVersionsRequest,
    ListVersionsResponse,
    SearchResourcesRequest,
    SearchResourcesResponse,
    SearchResult,
    UpdateApiRequest,
    UpdateAttributeRequest,
    UpdateDependencyRequest,
    UpdateDeploymentRequest,
    UpdateExternalApiRequest,
    UpdateSpecRequest,
    UpdateVersionRequest,
)
from .types.common_fields import (
    Api,
    ApiHubInstance,
    ApiOperation,
    Attribute,
    AttributeValues,
    Definition,
    Dependency,
    DependencyEntityReference,
    DependencyErrorDetail,
    Deployment,
    Documentation,
    ExternalApi,
    HttpOperation,
    Issue,
    Linter,
    LintResponse,
    LintState,
    OpenApiSpecDetails,
    OperationDetails,
    OperationMetadata,
    Owner,
    Path,
    Point,
    Range,
    Schema,
    Severity,
    Spec,
    SpecContents,
    SpecDetails,
    Version,
)
from .types.host_project_registration_service import (
    CreateHostProjectRegistrationRequest,
    GetHostProjectRegistrationRequest,
    HostProjectRegistration,
    ListHostProjectRegistrationsRequest,
    ListHostProjectRegistrationsResponse,
)
from .types.linting_service import (
    GetStyleGuideContentsRequest,
    GetStyleGuideRequest,
    LintSpecRequest,
    StyleGuide,
    StyleGuideContents,
    UpdateStyleGuideRequest,
)
from .types.plugin_service import (
    DisablePluginRequest,
    EnablePluginRequest,
    GetPluginRequest,
    Plugin,
)
from .types.provisioning_service import (
    CreateApiHubInstanceRequest,
    GetApiHubInstanceRequest,
    LookupApiHubInstanceRequest,
    LookupApiHubInstanceResponse,
)
from .types.runtime_project_attachment_service import (
    CreateRuntimeProjectAttachmentRequest,
    DeleteRuntimeProjectAttachmentRequest,
    GetRuntimeProjectAttachmentRequest,
    ListRuntimeProjectAttachmentsRequest,
    ListRuntimeProjectAttachmentsResponse,
    LookupRuntimeProjectAttachmentRequest,
    LookupRuntimeProjectAttachmentResponse,
    RuntimeProjectAttachment,
)

__all__ = (
    "Api",
    "ApiHubClient",
    "ApiHubDependenciesClient",
    "ApiHubInstance",
    "ApiHubPluginClient",
    "ApiHubResource",
    "ApiOperation",
    "Attribute",
    "AttributeValues",
    "CreateApiHubInstanceRequest",
    "CreateApiRequest",
    "CreateAttributeRequest",
    "CreateDependencyRequest",
    "CreateDeploymentRequest",
    "CreateExternalApiRequest",
    "CreateHostProjectRegistrationRequest",
    "CreateRuntimeProjectAttachmentRequest",
    "CreateSpecRequest",
    "CreateVersionRequest",
    "Definition",
    "DeleteApiRequest",
    "DeleteAttributeRequest",
    "DeleteDependencyRequest",
    "DeleteDeploymentRequest",
    "DeleteExternalApiRequest",
    "DeleteRuntimeProjectAttachmentRequest",
    "DeleteSpecRequest",
    "DeleteVersionRequest",
    "Dependency",
    "DependencyEntityReference",
    "DependencyErrorDetail",
    "Deployment",
    "DisablePluginRequest",
    "Documentation",
    "EnablePluginRequest",
    "ExternalApi",
    "GetApiHubInstanceRequest",
    "GetApiOperationRequest",
    "GetApiRequest",
    "GetAttributeRequest",
    "GetDefinitionRequest",
    "GetDependencyRequest",
    "GetDeploymentRequest",
    "GetExternalApiRequest",
    "GetHostProjectRegistrationRequest",
    "GetPluginRequest",
    "GetRuntimeProjectAttachmentRequest",
    "GetSpecContentsRequest",
    "GetSpecRequest",
    "GetStyleGuideContentsRequest",
    "GetStyleGuideRequest",
    "GetVersionRequest",
    "HostProjectRegistration",
    "HostProjectRegistrationServiceClient",
    "HttpOperation",
    "Issue",
    "LintResponse",
    "LintSpecRequest",
    "LintState",
    "Linter",
    "LintingServiceClient",
    "ListApiOperationsRequest",
    "ListApiOperationsResponse",
    "ListApisRequest",
    "ListApisResponse",
    "ListAttributesRequest",
    "ListAttributesResponse",
    "ListDependenciesRequest",
    "ListDependenciesResponse",
    "ListDeploymentsRequest",
    "ListDeploymentsResponse",
    "ListExternalApisRequest",
    "ListExternalApisResponse",
    "ListHostProjectRegistrationsRequest",
    "ListHostProjectRegistrationsResponse",
    "ListRuntimeProjectAttachmentsRequest",
    "ListRuntimeProjectAttachmentsResponse",
    "ListSpecsRequest",
    "ListSpecsResponse",
    "ListVersionsRequest",
    "ListVersionsResponse",
    "LookupApiHubInstanceRequest",
    "LookupApiHubInstanceResponse",
    "LookupRuntimeProjectAttachmentRequest",
    "LookupRuntimeProjectAttachmentResponse",
    "OpenApiSpecDetails",
    "OperationDetails",
    "OperationMetadata",
    "Owner",
    "Path",
    "Plugin",
    "Point",
    "ProvisioningClient",
    "Range",
    "RuntimeProjectAttachment",
    "RuntimeProjectAttachmentServiceClient",
    "Schema",
    "SearchResourcesRequest",
    "SearchResourcesResponse",
    "SearchResult",
    "Severity",
    "Spec",
    "SpecContents",
    "SpecDetails",
    "StyleGuide",
    "StyleGuideContents",
    "UpdateApiRequest",
    "UpdateAttributeRequest",
    "UpdateDependencyRequest",
    "UpdateDeploymentRequest",
    "UpdateExternalApiRequest",
    "UpdateSpecRequest",
    "UpdateStyleGuideRequest",
    "UpdateVersionRequest",
    "Version",
)