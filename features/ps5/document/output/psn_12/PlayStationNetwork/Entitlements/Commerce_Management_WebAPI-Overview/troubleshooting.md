# Commerce Management Web API Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Commerce_Management_WebAPI-Overview/troubleshooting.html

# Troubleshooting

This chapter includes issues you may encounter when implementing the Commerce Management Web API.

## Attempting to access an event stream returned a system error.

Ensure that the correct stream URL is being used by using the below API:

In the above example, you would need to replace "AMAZINGGAMEPUBLISHER" with your name as well as pass in a valid token. If you are still facing an error, please open a DevNet support ticket.

## Attempting to access an event stream returned an "Invalid Token" error.

When requesting the OAuth token, ensure you are passing in the parameter "`token_format=jwt`".

Below is an example request to obtain the token: