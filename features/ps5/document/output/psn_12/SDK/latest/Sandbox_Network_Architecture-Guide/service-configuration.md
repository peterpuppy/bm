# Sandbox Network Architecture Guide – SDK 13.000

Source: https://game.develop.playstation.net/resources/documents/SDK/latest/Sandbox_Network_Architecture-Guide/service-configuration.html

# Configuring PlayStation™Network Services in Sandbox

This topic explains the two methods of configuring PlayStation™Network Services in Sandbox: using the CLI-based tool `np-service-config` and using a web-based tool such as the Title Cloud Storage Tool.

Nearly all PlayStation™Network service usage remains the same with Sandbox, but you must update workflows for service configuration management and [game server authentication](game-and-server-code.html#general_api_topic__section_hlq_ldl_4hc).

There are two methods to update service configurations for services in Sandbox:

* Using `np-service-config`, a CLI based tool.
* Using web-based tools (Universal Data System (UDS) Management Tool, Title Cloud Storage Tool, etc.)

Note: You can't update service configuration in Sandbox using the service's respective management API. For example, the Title Cloud Storage Management Web API.

## Configuring Services with the Np Config Tool

Sandbox enables you to treat the configuration of PlayStation™Network services (with the exception of Commerce) as code, storing it alongside game code in a source control system. Using `np-service-config`, you can specify your network configuration as a JSON file and push the configuration whenever you want. For more information on configuring services with `np-service-config`, see [NP Service Config User's Guide](../NP_Service_Config-Users_Guide/__document_toc.html).

Storing your network configuration in a source control system means you can rollback to a previous network configuration if necessary. PlayStation™Network doesn't automatically rollback the deployment in the instance of a deployment fail, so you can retry deploying or rollback the changes. If you suspect that there was something wrong with the configuration files, you may also consider uploading a new configuration and then deploying that.

Follow the best practices listed below to get the most out of `np-service-config` and ensure that your service configurations work as intended:

* **Check configuration files into a source code system** - SIE recommends that you check configuration files into your source code system on the same basis as you do your source code. This provides you with two benefits:
  + You can obtain a rich version history of everything you have checked into your mainline and the option of rolling back to a previous version.
  + If you have multiple developers working simultaneously on multiple versions of the configuration, you can use your source system to merge divergent changes.
* **Frequently check-in minor edits to configuration** - Even for minor edits such as changing a trophy name, regularly check changes into your source control system as you edit service configuration in Sandbox.
* **Leverage your source control system for large changes to configuration** - While SIE stores uploaded copies of your configuration for you indefinitely, it does not offer the functionality of a revision stream for merging divergent changes or rolling back to a select version. SIE can't produce a linear order of your configurations, has no notion of branching if you are working in multiple streams, and does not provide tooling to rollback your configuration.
* **Keep the network configuration synced with the version in source control** - Designate a branch in your source control system to represent the version of the configuration in DEV. When you check a new version of the files into DEV, use `np-service-config` to push them to PlayStation™Network. You can integrate `np-service-config` with your build system to make this automatic.

## Configuring Services with Web-Based Tools

PlayStation™Network service configuration is also available through the web-based tools such as the UDS Management Tool and the Title Cloud Storage Tool.

The following tools have been updated to support configuration in Sandbox:

* NP Communication ID Metadata
* UDS Management Tool
* Trophies
* Leaderboards
* Online Multiplayer
* Title Cloud Storage Tool

Note: Currently, the Game Help Tool does not support configuration in Sandbox.

These tools allow you to stage changes in a draft of your configuration before they are visible in Sandbox. To update a service's configuration using one of these tools, do the following:

1. From the respective tool, navigate to **Service State** > **Draft**.
2. Update your service's configuration. Toggle **Published to DEV** to see a read-only preview of the configuration in DEV.
3. When you are ready to test your configuration, select **Actions** > **Publish to DEV**.
4. To publish the configuration to CERT and RETAIL, go to the **Published to DEV** view and select **Actions** > **Publish to CERT and RETAIL**.

## Config ID

Sandbox introduces a mechanism for labeling a title's configuration for PlayStation™Network services called Config ID. Similar to the NP Config Tag used in Legacy, a Config ID corresponds to an immutable version of the configuration that can be applied to different sandboxes as the title moves through the development, certification, and publishing process.

When you create a Config ID, you may add a description to it for tracking purposes.

The NP Config Tag and the Config ID differ in the following ways:

| NP Config Tag | Config ID |
| --- | --- |
| Created manually by you | Created automatically every time the configuration in DEV is modified |
| Applies only to the Universal Data System (UDS) and Trophy services. | Applies to the UDS, Trophy, Matchmaking, Leaderboards, Title Cloud Storage, Game Help, and Tournaments services. Config ID is not used for Commerce. |
| Only one active NP Config Tag per environment. | In CERT and RETAIL, you can deploy one Config ID per service. |

The configuration associated with the Config ID is represented as a set of JSON files, one per service.

Config ID Configuration Example

Service configuration is performed separately from requesting a service in DevNet. If you attempt to deploy a configuration for a service that you have not requested for the given title, it fails. If you wish to re-use the configuration of an existing title when developing an upcoming sequel, request the relevant services in the new title before deploying the configuration to DEV.

For more information on requesting PlayStation™Network services, see 'Requesting to Add a New Service for a New Product' under [PlayStation™Network Service Setup Guide - Making Service Requests - Service Request Overview](../PSN_Service_Setup-Guide/service-request-overview.html).