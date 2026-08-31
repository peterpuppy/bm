# Profanity Filter Web API Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Profanity_Filter_WebAPI-Overview/using-the-profanity-filter.html

# Using the Profanity Filter

This topic provides information on how to use Profanity Filter.

## Parameters

The Profanity Filter consists of one request that can either filter or test text for profanity. You must have a valid OAuth access token in order to make this request. See [PlayStation™Network Web APIs Overview - Usage - Obtaining Access Tokens](../../../SDK/latest/PSN_WebAPI-Overview/obtaining-access-tokens.html) for more information.

| **Parameter Name** | **Type** |  |
| --- | --- | --- |
| `locale` | String | Set to a valid locale as defined in the [Auth Web API Overview](../Auth_WebAPI-Overview/__document_toc.html). For example, "en-GB". To obtain the correct locale, see the section [Obtaining a Valid Locale](using-the-profanity-filter.html#profanity-filter-web-api-overview_1__profanity-filter-web-api-overview_1_2).  The locale selects the dictionary used to filter the text. The resulting filtering behavior can vary significantly by language and country/region. For this reason, select the same locale of either the author of the content or the reader of the content, depending on your title's internal policy.  You may also use a comma-separated list to filter through multiple locales. Do not include spaces. See [Filtering Through Multiple Locales](using-the-profanity-filter.html#profanity-filter-web-api-overview_1__profanity-filter-web-api-overview_1_3) for more information. |
| `serviceLabel` | String | Set to the service label corresponding to a Communication ID issued by PlayStation™Network. You must have previously provisioned the Profanity Filter service for your title. |
| `text` | String | Text to filter. This text can be a maximum of 4KB in size. |

## Obtaining a Valid Locale

The Profanity Filter will accept only valid locales for filtering. You can get the
current user's system language by calling `sceSystemServiceParamGetInt()` with a
[parameter value to fetch the
language](https://p.siedev.net/resources/documents/SDK/latest/SystemService-Reference/0002.html). You can use the numeric
code to map the correct language code to use. Please see [Auth Web API Overview - Appendix - Language Codes](../Auth_WebAPI-Overview/language-codes.html) for a list of values.

## Filtering Through Multiple Locales

You can provide a comma-separated list of locales for the `locale` parameter to filter text in multiple locales, simultaneously. The service filters the string through each dictionary in sequence and returns the result.

SIE recommends that you filter this way only when required. Filtering through multiple locales reduces the advantages of locale-specific filtering such as cultural context and regional differences. Additionally, this may increase response times.

Filtering strings through multiple locales is only compatible with `filterProfanity`.

## Filter Profanity In Text

Censors profanity in a user content string. The string is returned in the response and any profanity detected is replaced by "\*" characters.

**Response**

The string you submitted as the "text" parameter is returned in potentially modified form.

Input:

```
When the bell rang a second time the King shouted angrily, "Smudge and blazes!" and at a third ring he screamed in a fury, "Hippikaloric!" which must be a dreadful word because we don't know what it means.
```

Output:

```
When the bell rang a second time the King shouted angrily, "****** and ******!" and at a third ring he screamed in a fury, "************!" which must be a dreadful word because we don't know what it means.
```

If there is no profanity detected in the text, it is returned unchanged.

## Test Text For Profanity

Checks a user content string for profanity. The string is returned in the response and any profanity is surrounded by "[]" characters.

**Response**

The string you submitted as the "text" parameter is returned in potentially modified form.

Input:

```
When the bell rang a second time the King shouted angrily, "Smudge and blazes!" and at a third ring he screamed in a fury, "Hippikaloric!" which must be a dreadful word because we don't know what it means.
```

Output:

```
When the bell rang a second time the King shouted angrily, "[Smudge] and [blazes]!" and at a third ring he screamed in a fury, "[Hippikaloric]!" which must be a dreadful word because we don't know what it means.
```

If there is no profanity detected in the text, it is returned unchanged.

**Handling Errors**

Error messages from the service in JSON can return in the body. These can be helpful during troubleshooting. A typical example is:

```
{
    "error": {
        "code": 3350785,
        "message": "Bad request - Service label doesn't exist. (0x332101)",
        "status": 400,
        "tid": "32f00b1e-389e-4b83-bd6d-982fbebd8506"
    }
}
```

In the JSON above, the message field can reveal additional details on the nature of the error. The "errorCode" and "tid" fields can be useful in troubleshooting your issue with support.