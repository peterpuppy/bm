# Sandbox Network Architecture Guide – SDK 13.000

Source: https://game.develop.playstation.net/resources/documents/SDK/latest/Sandbox_Network_Architecture-Guide/sandbox-infrastructure.html

# Sandbox Network Architecture Overview

This topic provides an overview of the changes introduced by the Sandbox network architecture. It covers changes in development, testing, and certification processes, and explains the benefits and expected impacts on game developer workflows.

The Sandbox network architecture is a significant reworking of SIE's network development infrastructure. It introduces changes in tooling, development and testing workflows, and certification work across PlayStation® platforms.

The Legacy PlayStation® environments sp-int, prod-qa, and np, are all physically separate from one another. This means that configurations that pass in sp-int have the potential to fail in prod-qa and vice versa. This can lead to certification delays, confusion, and rework for both developers and certification teams.

Sandbox solves these problems by having development and certification take place in virtual environments called sandboxes that exist within the same infrastructure as SIE's live player network. This eliminates any obstacles created from maintaining different physical environments. Sandboxes are isolated from one another and from the production environment but they use the same underlying services, meaning that services and features you provision work across development, certification, and retail environments.

In addition to solving these issues, Sandbox offers a number of improvements over Legacy:

* Guaranteed feature parity between development, certification, and retail environments by using the same underlying network infrastructure.
* Allows you to treat the configuration of PlayStation™Network services as code, enabling version control, repeatability, and rollback of network configurations.
* Ability to test using the same network infrastructure as live players while keeping data isolated.
* Improvements to test fidelity by ensuring that behavior in development and certification environments matches retail conditions.
* PlayStation® environment context is embedded in your access tokens, so PlayStation™Network can route requests to the correct environment automatically.

These changes lay the foundation for future improvements to the publishing pipeline. Over 2026, SIE will work with partners to migrate all PlayStation®5 titles and applicable PlayStation®4 titles from the Legacy architecture to the Sandbox architecture.

## Differences Between Sandbox and Legacy Architectures

Sandbox introduces the following key changes to development workflows:

* The [domain for PlayStation™Network APIs is unified](game-and-server-code.html "This topic provides guidance on adapting game and server code to accommodate the Sandbox network architecture changes. It highlights changes to network API requests and access token modifications.") between the development, certification, and retail environments.
* [Separate and dedicated accounts for development in Sandbox are required](accounts-for-development-for-sandbox.html "This topic outlines the process for creating new accounts for development in Sandbox and explains the migration process of accounts for development in the Legacy architecture."). You can use a newly created account or an existing account that SIE has migrated from the Legacy architecture.
* Unlike service configuration data, accounts for PlayStation™Network are shared across the development and certification environments but can't be used in the retail environment. The different environments are distinguished at the account level by the attribute `account_type`. The `account_type` is set to `CUSTOMER` or `SANDBOX`.
* The *NP Environments* setting in the DevKit and TestKit *★Debug Settings* menu is replaced by a *Network Architecture* setting.

  Note: Currently, the *Network Architecture* setting is not available.
* The `np-service-config` tool can be used to configure PlayStation™Network services and Universal Data System objects.

Note: To use the Sandbox architecture for existing titles, migration by SIE is required. Once migrated, you can't make further changes to service configurations in the Legacy architecture.

## Getting Started

To get started with Sandbox:

* Read [Sandbox Architecture](sandbox-infrastructure.html "This topic provides an overview of the Sandbox network architecture's design, including information on the available sandboxes and how data is partitioned between each sandbox."), [Accounts for Development in Sandbox](accounts-for-development-for-sandbox.html "This topic outlines the process for creating new accounts for development in Sandbox and explains the migration process of accounts for development in the Legacy architecture."), and [Titles in Sandbox](sandbox-title-migration.html "This topic outlines the options available for getting titles into the Sandbox network architecture. It covers migrating existing titles and creating titles directly in Sandbox.") to understand more about how Sandbox works, including account and migration information.
* Read [Configuring PlayStation™Network Services in Sandbox](service-configuration.html "This topic explains the two methods of configuring PlayStation™Network Services in Sandbox: using the CLI-based tool np-service-config and using a web-based tool such as the Title Cloud Storage Tool.") to understand how Sandbox works with PlayStation™Network services.
* After SIE has migrated your accounts and titles, follow the guidance of the topics in [Developing and Publishing with Sandbox](developing-and-publishing-workflow.html "This chapter highlights the updates to development and publishing workflows brought on by the introduction of Sandbox. It focuses on IP allowlist management, account setup, service configuration, and submission processes.") to develop and publish titles in Sandbox.

# Sandbox Architecture

This topic provides an overview of the Sandbox network architecture's design, including information on the available sandboxes and how data is partitioned between each sandbox.

The two available sandboxes, DEV and CERT, are used for game development and certification workflows, respectively. DEV and CERT exist within a single, global PlayStation™Network environment called RETAIL. This is the same environment that currently serves production requests.

Sandbox Architecture

DEV, CERT, and RETAIL are separated by a set of access measures and data segregation rules. This means that what you do on PlayStation™Network in one of these environments does not affect the others.

## Differences Between Sandbox and Legacy Architectures

The Legacy architecture consists of a dedicated set of services unique to each environment, meaning services are not shared across the development and certification environments. Each environment in the Legacy architecture is physically and logically isolated from the others and data is only transferred when a console application or configuration is published or submitted for certification.

The Sandbox architecture, on the other hand, differs from the Legacy architecture in a few key areas:

* Sandboxes are virtual environments within the production environment. Each sandbox is virtually isolated from the others and from the rest of the production environment (RETAIL) with which end-users interact.
* You can configure DevKit or TestKit consoles to connect to DEV and CERT. Data saved locally to the console is partitioned separately based on the network environment to which it's connecting.
* When a console makes calls to PlayStation™Network, the access token has embedded information about the sandbox to which it's connected. This sandbox context allows PlayStation™Network to handle the request correctly. DevKit manages this without changes to your code. For more information on using PlayStation™Network services with Sandbox, see [Configuring PlayStation™Network Services in Sandbox](service-configuration.html "This topic explains the two methods of configuring PlayStation™Network Services in Sandbox: using the CLI-based tool np-service-config and using a web-based tool such as the Title Cloud Storage Tool.").

## How Sandbox Data is Partitioned

While DEV and CERT are largely separate, you use the same accounts to access them. Data tied to these accounts is usually global, meaning that a change in one environment is visible in the other. Data tied to specific titles is generally local, meaning that it's isolated to that specific environment.

Global and Local Data

## Access Controls and Authentication

Requests sent to PlayStation™Network services go to one global PlayStation™Network environment and are processed and managed by the same authentication mechanism as a live request. This allows PlayStation™Network SDKs to manage authentication to sandboxes just as they do for the Legacy PlayStation® environments.

Access is managed with the use of OAuth tokens and authentication codes. Access tokens issued by the OAuth service are either usable only for live requests, or only for a specific sandbox. When a specific sandbox is selected, any authentication granted to the DevKit or TestKit is exclusive to that sandbox. SIE enforces sandbox separation at the service level in addition to existing title separation mechanisms.

You can manage title separation per account for PlayStation™Network using the Developer Accounts Tool. For more information, see [Development Accounts User's Guide - Managing an Account in the Account Library - Managing Title Privileges In Bulk](../Development_Accounts-Users_Guide/managing-title-privileges-in-bulk.html).

**Sandbox Context**

Requests to PlayStation™Network services use the same APIs as the Legacy PlayStation® environments, but sandbox context is embedded in your access tokens so PlayStation™Network can route requests to the correct environment.

For example, when a DevKit sends a request to a PlayStation™Network service to fetch a list of trophies for the title being played, instead of querying a specific URL that connects to a specific network environment, the request includes a *Sandbox ID* selected from the system configuration that refers to the target sandbox. PlayStation™Network then returns with data applying to that sandbox only, using the *Sandbox ID* to ensure that live data isn't returned for a sandbox request, and that data in the DEV sandbox isn't returned for a request for the CERT sandbox or RETAIL.

You can test your configuration using the same network infrastructure as your end users, with sandbox context ensuring that only you can see that data until you choose to make it live.