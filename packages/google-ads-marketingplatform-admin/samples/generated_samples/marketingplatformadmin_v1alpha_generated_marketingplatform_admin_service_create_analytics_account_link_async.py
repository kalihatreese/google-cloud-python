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
# Generated code. DO NOT EDIT!
#
# Snippet for CreateAnalyticsAccountLink
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-ads-marketingplatform-admin


# [START marketingplatformadmin_v1alpha_generated_MarketingplatformAdminService_CreateAnalyticsAccountLink_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.ads import marketingplatform_admin_v1alpha


async def sample_create_analytics_account_link():
    # Create a client
    client = marketingplatform_admin_v1alpha.MarketingplatformAdminServiceAsyncClient()

    # Initialize request argument(s)
    analytics_account_link = marketingplatform_admin_v1alpha.AnalyticsAccountLink()
    analytics_account_link.analytics_account = "analytics_account_value"

    request = marketingplatform_admin_v1alpha.CreateAnalyticsAccountLinkRequest(
        parent="parent_value",
        analytics_account_link=analytics_account_link,
    )

    # Make the request
    response = await client.create_analytics_account_link(request=request)

    # Handle the response
    print(response)

# [END marketingplatformadmin_v1alpha_generated_MarketingplatformAdminService_CreateAnalyticsAccountLink_async]