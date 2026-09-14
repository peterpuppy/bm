# Target Manager CLI User's Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Target_Manager_CLI-Users_Guide/target-manager-cli-mutual-tls-encryption.html

# Target Manager CLI Mutual TLS Encryption

## Overview

Encrypted communication with a Target is supported using mutual TLS (mTLS). This uses a pair of server/client keys that share a common root certificate to encrypt communication.

This is a security measure to prevent external parties from intercepting data as it is being transferred between the Host PC and a Target.

Note: The Private Mode configuration tool is used to enable the use of mTLS certificates. To request access to this tool, please ask your DevNet 'Org Admin' to create a Private DevNet tracker to request access to the Private Mode configuration tool.

## Generating Certificates

Target Manager Server includes a set of default certificates that **should** be overridden, as they are the same for all instances of Target Manager Server.

Compatible certificates can be generated using the following OpenSSL commands and filling in the relevant information when prompted:

1. Create a private key for the custom root certificate authority:

   `openssl genpkey -out root_ca.key -algorithm RSA -pkeyopt rsa_keygen_bits:3072`
2. Create a certificate signing request for the custom root certificate authority:

   `openssl req -new -sha256 -key root_ca.key -out root_ca.csr`
3. Create a public certificate for the custom root certificate authority:

   `openssl x509 -req -sha256 -days <days> -in root_ca.csr -signkey root_ca.key -out root_ca.crt`
4. Create a private key for the server (Target) certificate:

   `openssl genpkey -out server.key -algorithm RSA -pkeyopt rsa_keygen_bits:3072`
5. Create a certificate signing request for the server (Target) certificate:

   `openssl req -new -sha256 -key server.key -out server.csr`
6. Create a certificate for the server (Target), signed by the custom root certificate authority:

   `openssl x509 -req -in server.csr -CA root_ca.crt -CAkey root_ca.key -CAcreateserial -out server.crt -days <days> -sha256`
7. Create a private key for the client (Target Manager Server) certificate:

   `openssl genpkey -out client.key -algorithm RSA -pkeyopt rsa_keygen_bits:3072`
8. Create a certificate signing request for the client (Target Manager Server) certificate:

   `openssl req -new -sha256 -key client.key -out client.csr`
9. Create a certificate for the client (Target Manager Server), signed by the custom root certificate authority:

   `openssl x509 -req -in client.csr -CA root_ca.crt -CAkey root_ca.key -CAcreateserial -out client.crt -days <days> -sha256`

Note: Ensure that the expiration duration for the certificate, indicated as `<days>` in the commands, is set to an appropriate number. For example, setting `<days>` to 365 will cause the certificate to expire after a year.

## Private Mode Configuration Tool

The Private Mode configuration tool has been updated to support the new mTLS functionality and allow you to enable/disable the use of the override certificates. More information on the Private Mode configuration tool can be found in the tool's readme file.

Note: The following commands require the Target to be powered off.

**Enabling/Disabling encrypted communication mode on a Target can be performed via this command:**

`prospero-private-mode set-encryption <target> <passcode> {ON|OFF}`

**Overriding Target certificates can be performed via the following command:**

`prospero-private-mode override-certificates <target> <passcode> /clientCert:<file> /clientKey:<file> /serverCert:<file> /serverKey:<file> /rootCert:<file>`

**Clearing Target certificates can be performed via the following command:**

`prospero-private-mode clear-certificates <target> <passcode>`

**Accessing the Target security log can be performed with the following command:**

`prospero-private-mode get-audit-log <target> <passcode> <file>`

## Applying the Certificates

If the Target has overridden certificates, Target Manager Server needs to be configured to use the corresponding client and root certificates. Paths to overridden certificates are stored in the registry of the Host PC and updating the paths can be achieved through `prospero-ctrl`. The `/global` argument sets or clears the certificates globally, rather than for a specific Target.

When connecting to a Target, the default behavior is to look for Target specific certificates, then global certificates, then if neither exists to use the default certificates.

**Overriding TMS certificates can be done via the following command:**

`target set-encryption-certificates <clientCertificatePath> <clientKeyPath> <rootCertificatePath> [/global] [/target:<target>]`

**Clearing the override certificates can be done via the following command:**

`target unset-encryption-certificates [/global] [/target:<target>]`

You can verify certificates have been updated successfully using the Windows Registry Editor application on the Host PC and checking under:

**Global certificates:**

`Computer\HKEY_CURRENT_USER\Software\SCE\Prospero\TMServer\Authentication\`

**Target certificates:**

`Computer\HKEY_CURRENT_USER\Software\SCE\Prospero\TMServer\Authentication\ <target hostname>`

## Additional Firewall settings

In addition to the Host PC firewall settings required by Target Manager Server described in the [Target Manager GUI User's Guide - Using Target Manager to Manage Targets - Connecting to Targets Through Target Manager](../Target_Manager_GUI-Users_Guide/connecting-to-targets-through-target-manager.html) section, the following ports must be set to enable outgoing connections on the Host PC:

Private Mode Tool:

* TCP Port 8657

Encrypted Communications:

* TCP Port 8656
* TCP Port 8568

## Limitations

* If the certificates are lost, the Target can be recovered by initializing the Target using Safe Mode or by applying new certificates to a USB drive as described in the System Software UI. Refer to [System Software User's Guide (Settings) - Features of the ★Debug Settings Menu](../System_Software-Users_Guide_for_Settings/features-of-the-debug-settings-menu.html) for more information.
* Certificates must be in PEM format.
* Certificate expiry dates should not exceed 19th January 2038.
* Operations using the peer-to-peer file transfer mechanism described in [Appendix C: Network Configuration](network-configuration-for-targets.html) require that all Targets specified have the same TLS configuration.

  Example operations include package install to multiple Targets, system software update to multiple Targets and Standalone Workspace push / deploy to multiple Targets.

  The Targets must all have TLS enabled with the same certificates, or all have TLS disabled.