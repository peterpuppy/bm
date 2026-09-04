# PlayStation™Network Service Setup Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_Service_Setup-Guide/development-preparation.html

# FAQ

This chapter provides information on frequently asked questions.

# Development Preparation

This topic provides answers to frequently asked questions about development preparation.

**Q: How do I resolve the error that the PlayStation®4 Console-type product cannot be
registered in PlayStation®5 DevNet?**

**A:** The NP Title ID cannot be registered in multiple DevNet platforms. If you see the
error "This NP Title ID is already registered" when you attempt to register a product in
PlayStation®5 DevNet, it means that the NP Title ID has already been registered in
PlayStation®4 DevNet.

In this case, you need to use the **Migrate product to PS5** menu item in the product
detail page instead of registering a new product as **App (PS4 Cross-gen)** product.

Use the following recommended steps to migrate PlayStation®4 console-type products:

1. Register the **App (PS5)** product in PlayStation®5 DevNet. Obtain the PlayStation®5
   NP Title ID from Content Pipeline.
2. Migrate the PlayStation®4 console-type product as the same franchise/title
   PlayStation®5 product created in step 1.

For detailed steps, see Migrating a PlayStation®4 Product to PlayStation®5 DevNet.

**Q: What are tips for setting up cross-gen services for App (PS4 Cross-gen)
products?**

**A:** Use PlayStation™Network services available in **PS5 on PS4 App** product.
Setup a service in **App (PS5)** first. Then share the service to **App (PS4
Cross-gen)** product.

This order of steps also avoids service request errors when you attempt to request Trophy2
in **App (PS5)**.

If you see the error message "Error communicating with the server", make sure that the same
NP Communication ID is used for Trophy in **App (PS4 Cross-gen)**. This error is due to
the limitation that Trophy2 and Trophy cannot use the same NP Communication ID. If you
encounter this error message and need to request the Trophy2 Service, remove the Trophy
Service from **App (PS4 Cross-gen)**.

If you can't find the Trophy Service in **App (PS4 Cross-gen)**, click the **PS4**
tab in the product detail page.

# Development

This topic provides answers to frequently asked questions about development with PlayStation™Network.

**Q: How do I create an account for PlayStation™Network for development?**

**A:** From the **Settings** menu on the PlayStation®5 Development Kit/Testing Kit, select the **Sign In To PlayStation™Network** menu to create an account for PlayStation™Network in the development environment. A method using the web browser on your PC is also available.

For details on methods for creating an account, refer to "An Account for PlayStation™Network in the Development Environment" section in [PlayStation™Network Overview - Beginning Development - Before You Start](../PSN-Overview/before-you-start.html).

**Q: How do I add a source IP address to ACL in the development environment (sp-int)?**

**A:** Contact Private Support by using the <https://p.siedev.net/support/newissue> page to create a support request. For details on how IP allowlisting works on PlayStation™Network, see [IP Allowlisting for PlayStation™Network Services](https://learn.playstation.net/csh?context=psp_IPallowlisting_gs).

**Q. How do I get access to Content Pipeline?**

**A:** Request access from the Partner Admin for Content Pipeline in your company or organization. If you are not sure who your Partner Admin is, click **Contact Support** in the [PlayStation™Partners Help Center](https://playstationpartners.service-now.com/csm) and fill out a **User Accounts > Other** ticket.