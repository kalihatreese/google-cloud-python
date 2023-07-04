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
from google.cloud.deploy_v1 import gapic_version as package_version

__version__ = package_version.__version__


from .services.cloud_deploy import CloudDeployAsyncClient, CloudDeployClient
from .types.cloud_deploy import (
    AbandonReleaseRequest,
    AbandonReleaseResponse,
    AdvanceChildRolloutJob,
    AdvanceChildRolloutJobRun,
    AdvanceRolloutRequest,
    AdvanceRolloutResponse,
    AnthosCluster,
    ApproveRolloutRequest,
    ApproveRolloutResponse,
    BuildArtifact,
    Canary,
    CanaryDeployment,
    CancelRolloutRequest,
    CancelRolloutResponse,
    ChildRolloutJobs,
    CloudRunConfig,
    CloudRunLocation,
    CloudRunMetadata,
    CloudRunRenderMetadata,
    Config,
    CreateChildRolloutJob,
    CreateChildRolloutJobRun,
    CreateDeliveryPipelineRequest,
    CreateReleaseRequest,
    CreateRolloutRequest,
    CreateTargetRequest,
    CustomCanaryDeployment,
    DefaultPool,
    DeleteDeliveryPipelineRequest,
    DeleteTargetRequest,
    DeliveryPipeline,
    DeployArtifact,
    DeployJob,
    DeployJobRun,
    DeployJobRunMetadata,
    DeploymentJobs,
    DeployParameters,
    ExecutionConfig,
    GetConfigRequest,
    GetDeliveryPipelineRequest,
    GetJobRunRequest,
    GetReleaseRequest,
    GetRolloutRequest,
    GetTargetRequest,
    GkeCluster,
    IgnoreJobRequest,
    IgnoreJobResponse,
    Job,
    JobRun,
    KubernetesConfig,
    ListDeliveryPipelinesRequest,
    ListDeliveryPipelinesResponse,
    ListJobRunsRequest,
    ListJobRunsResponse,
    ListReleasesRequest,
    ListReleasesResponse,
    ListRolloutsRequest,
    ListRolloutsResponse,
    ListTargetsRequest,
    ListTargetsResponse,
    Metadata,
    MultiTarget,
    OperationMetadata,
    Phase,
    PipelineCondition,
    PipelineReadyCondition,
    PrivatePool,
    Release,
    RenderMetadata,
    RetryJobRequest,
    RetryJobResponse,
    Rollout,
    RuntimeConfig,
    SerialPipeline,
    SkaffoldSupportState,
    SkaffoldVersion,
    Stage,
    Standard,
    Strategy,
    Target,
    TargetArtifact,
    TargetsPresentCondition,
    TargetsTypeCondition,
    TerminateJobRunRequest,
    TerminateJobRunResponse,
    UpdateDeliveryPipelineRequest,
    UpdateTargetRequest,
    VerifyJob,
    VerifyJobRun,
)
from .types.deliverypipeline_notification_payload import (
    DeliveryPipelineNotificationEvent,
)
from .types.jobrun_notification_payload import JobRunNotificationEvent
from .types.log_enums import Type
from .types.release_notification_payload import ReleaseNotificationEvent
from .types.release_render_payload import ReleaseRenderEvent
from .types.rollout_notification_payload import RolloutNotificationEvent
from .types.target_notification_payload import TargetNotificationEvent

__all__ = (
    "CloudDeployAsyncClient",
    "AbandonReleaseRequest",
    "AbandonReleaseResponse",
    "AdvanceChildRolloutJob",
    "AdvanceChildRolloutJobRun",
    "AdvanceRolloutRequest",
    "AdvanceRolloutResponse",
    "AnthosCluster",
    "ApproveRolloutRequest",
    "ApproveRolloutResponse",
    "BuildArtifact",
    "Canary",
    "CanaryDeployment",
    "CancelRolloutRequest",
    "CancelRolloutResponse",
    "ChildRolloutJobs",
    "CloudDeployClient",
    "CloudRunConfig",
    "CloudRunLocation",
    "CloudRunMetadata",
    "CloudRunRenderMetadata",
    "Config",
    "CreateChildRolloutJob",
    "CreateChildRolloutJobRun",
    "CreateDeliveryPipelineRequest",
    "CreateReleaseRequest",
    "CreateRolloutRequest",
    "CreateTargetRequest",
    "CustomCanaryDeployment",
    "DefaultPool",
    "DeleteDeliveryPipelineRequest",
    "DeleteTargetRequest",
    "DeliveryPipeline",
    "DeliveryPipelineNotificationEvent",
    "DeployArtifact",
    "DeployJob",
    "DeployJobRun",
    "DeployJobRunMetadata",
    "DeployParameters",
    "DeploymentJobs",
    "ExecutionConfig",
    "GetConfigRequest",
    "GetDeliveryPipelineRequest",
    "GetJobRunRequest",
    "GetReleaseRequest",
    "GetRolloutRequest",
    "GetTargetRequest",
    "GkeCluster",
    "IgnoreJobRequest",
    "IgnoreJobResponse",
    "Job",
    "JobRun",
    "JobRunNotificationEvent",
    "KubernetesConfig",
    "ListDeliveryPipelinesRequest",
    "ListDeliveryPipelinesResponse",
    "ListJobRunsRequest",
    "ListJobRunsResponse",
    "ListReleasesRequest",
    "ListReleasesResponse",
    "ListRolloutsRequest",
    "ListRolloutsResponse",
    "ListTargetsRequest",
    "ListTargetsResponse",
    "Metadata",
    "MultiTarget",
    "OperationMetadata",
    "Phase",
    "PipelineCondition",
    "PipelineReadyCondition",
    "PrivatePool",
    "Release",
    "ReleaseNotificationEvent",
    "ReleaseRenderEvent",
    "RenderMetadata",
    "RetryJobRequest",
    "RetryJobResponse",
    "Rollout",
    "RolloutNotificationEvent",
    "RuntimeConfig",
    "SerialPipeline",
    "SkaffoldSupportState",
    "SkaffoldVersion",
    "Stage",
    "Standard",
    "Strategy",
    "Target",
    "TargetArtifact",
    "TargetNotificationEvent",
    "TargetsPresentCondition",
    "TargetsTypeCondition",
    "TerminateJobRunRequest",
    "TerminateJobRunResponse",
    "Type",
    "UpdateDeliveryPipelineRequest",
    "UpdateTargetRequest",
    "VerifyJob",
    "VerifyJobRun",
)