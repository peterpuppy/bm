# PlayStation™Network Game Help Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_Game_Help-Guide/appendix-b1-unique-identifiers.html

# Reference Materials

This chapter contains topics with additional information that you may find useful when configuring Game Help content, such as PlayStation™Network object references and definitions.

# PlayStation™Network Hint Object

The following table describes the PlayStation™Network hint object and its attributes.

The PlayStation™Network Hint Object and its Attributes

| Attribute | | | Data Type | Max Length | Required? | Localization | Editable | Description |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| object id | | | string | 32 | yes | no | no | Object ID of a hint. Partners can define object IDs themselves. An object ID is a string of 1 to 32 characters that can include alphanumeric characters, underscores ("\_") and hyphens ("-"). Object IDs starting with an "\_" (underscore) are reserved for system use and cannot be specified by partners. |
| name | | | string | 64 | yes | yes | yes | The name of the hint. This name is displayed in the system UI. |
| description | | | string | 400 | no | yes | yes | The description text for the hint. This description is displayed in the system UI below the name. |
| active status | | |  |  | no | no | yes |  |
|  | active | | boolean |  | yes ([\*](appendix-a-psn-hint-object.html#psn-game-help-guide_6_1__psn-game-help-guide_6_1_1)) | no | yes | Whether the hint is active or not.  Active hints are available to users in the system UI. |
|  | order | | integer |  | yes ([\*](appendix-a-psn-hint-object.html#psn-game-help-guide_6_1__psn-game-help-guide_6_1_1)) | no | yes | The position in which the active hint will appear in the system UI (1, 2 or 3) |
| reference object | | | UDS object |  | yes | no | yes | A reference to the UDS object (activity or trophy) that the hint is associated with. |
|  | object id | | string | 32 | yes | no | yes | The object id for the UDS object referenced. |
| media | | |  |  | no | yes | yes |  |
|  | file name | | string | 1024 | yes ([\*](appendix-a-psn-hint-object.html#psn-game-help-guide_6_1__psn-game-help-guide_6_1_1)) | yes | yes | The name of the media file associated with the Hint. |
|  | segment timecode | |  |  | no | yes | yes |  |
|  |  | start | string | 8 | yes ([\*](appendix-a-psn-hint-object.html#psn-game-help-guide_6_1__psn-game-help-guide_6_1_1)) | yes | yes | The timecode when the video clip starts in HH:MM:SS format. |
|  |  | end | string | 8 | yes ([\*](appendix-a-psn-hint-object.html#psn-game-help-guide_6_1__psn-game-help-guide_6_1_1)) | yes | yes | The timecode when the video clip ends in HH:MM:SS format. |

\*The parent element ('active status', 'media', or 'segment timecode') is optional, but if it exists, it must contain an instance of this element.

# Unique Identifiers

The table below lists the unique identifiers for entities supported in the entity definition metadata for Game Help bulk configuration.

Unique Identifiers

| Entity Type | Entity Subtype | Property Used in Entity ID |
| --- | --- | --- |
| PSNObject | Hint | `objectId` property of the Hint object. |

# Schema for Bulk Configuration of Hints

This topic provides the JSON schema used for the bulk configuration of hints.

```
{
   "$schema":"http://json-schema.org/draft-07/schema#",
   "type":"object",
   "title":"Game Help",
   "description":"The Game Help schema.",
   "required":[
      "schemaVersion",
      "contextType",
      "contextId",
      "entities"
   ],
   "properties":{
      "schemaVersion":{
         "const":"2.0"
      },
      "contextType":{
         "const":"NPCommunicationId"
      },
      "contextId":{
         "type":"string",
         "pattern":"^[A-Z]{4}[0-9]{5}_[0-9]{2}$",
         "examples":[
            "NPWR17272_00"
         ]
      },
      "entities":{
         "type":"object",
         "properties":{
            "activityHints":{
               "type":"array",
               "items":{
                  "$ref":"#/definitions/activityHintEntity"
               },
               "minItems":0,
               "examples":[
                  {
                     "objectId":"tut1of4-driving",
                     "activeStatus":{
                        "active":true,
                        "order":1
                     },
                     "links":{
                        "associatedMedia":{
                           "en-US":{
                              "fileName":"driving-tutorial_en.mp4",
                              "segmentTimecode":{
                                 "start":"00:05:00",
                                 "end":"00:10:00"
                              }
                           },
                           "ja-JP":{
                              "fileName":"driving-tutorial_jp.mp4"
                           }
                        },
                        "associatedObject":{
                           "objectId":"tut1of4"
                        }
                     },
                     "description":{
                        "en-US":"A free-for-all, where everyone is out to get you!"
                     },
                     "name":{
                        "en-US":"Driving",
                        "ja-JP":"運転"
                     }
                  }
               ]
            },
            "trophyHints":{
               "type":"array",
               "items":{
                  "$ref":"#/definitions/trophyHintEntity"
               },
               "minItems":0,
               "examples":[
                  {
                     "objectId":"tut1of4-driving",
                     "activeStatus":{
                        "active":true,
                        "order":1
                     },
                     "links":{
                        "associatedMedia":{
                           "en-US":{
                              "fileName":"driving-tutorial_en.mp4",
                              "segmentTimecode":{
                                 "start":"00:05:00",
                                 "end":"00:10:00"
                              }
                           },
                           "ja-JP":{
                              "fileName":"driving-tutorial_jp.mp4"
                           }
                        },
                        "associatedObject":{
                           "objectId":"tut1of4"
                        }
                     },
                     "description":{
                        "en-US":"A free-for-all, where everyone is out to get you!"
                     },
                     "name":{
                        "en-US":"Driving",
                        "ja-JP":"運転"
                     }
                  }
               ]
            },
            "media":{
               "type":"array",
               "items":{
                     "$ref":"#/definitions/mediaFile"
                  },
                  "examples":[
                     {
                        "fileName":"driving-tutorial_en.mp4",
                        "source":"console",
                        "segmentTimecode":{
                           "start":"00:02:00",
                           "end":"00:14:00"
                        },
                        "dateUploaded":"2020-03-24T18:00:35.000Z",
                        "type":"video"
                     },
                     {
                        "fileName":"driving-tutorial_jp.mp4",
                        "type":"video",
                        "source":"console",
                        "dateUploaded":"2020-03-25T18:00:35.000Z"
                     }
                  ]
               }
            }
         },
         "additionalProperties":false
      },
   "additionalProperties":false,
   "definitions":{
      "activeStatus":{
         "type":"object",
         "properties":{
            "active":{
               "type":"boolean",
               "default":false,
               "examples":[
                  true,
                  false
               ]
            },
            "order":{
               "type":"integer",
               "default":1,
               "minimum":1,
               "maximum":3,
               "examples":[
                  1,
                  2,
                  3
               ]
            }
         },
         "required":[
            "active",
            "order"
         ],
         "examples":[
            {
               "active":true,
               "order":1
            }
         ]
      },
      "associatedObject":{
         "type":"object",
         "properties":{
            "objectId":{
               "$ref":"#/definitions/objectId"
            }
         },
         "required":[
            "objectId"
         ],
         "examples":[
            {
               "objectId":"tut1of4"
            }
         ]
      },
      "associatedMedia":{
         "type":"object",
         "minProperties":1,
         "patternProperties":{
            "^[a-z]{2}-[a-zA-Z0-9]+$":{
               "$ref":"#/definitions/mediaFile"
            }
         }
      },
      "activityHintLinks":{
         "type":"object",
         "properties":{
            "associatedObject":{
               "$ref":"#/definitions/associatedObject"
            },
            "associatedMedia":{
               "$ref":"#/definitions/associatedMedia"
            }
         },
         "additionalProperties":false
      },
      "trophyHintLinks":{
         "type":"object",
         "properties":{
            "associatedMedia":{
               "$ref":"#/definitions/associatedMedia"
            },
            "associatedObject":{
               "$ref":"#/definitions/associatedObject"
            }
         },
         "additionalProperties":false
      },
      "mediaFile":{
         "type":"object",
         "properties":{
            "fileName":{
               "type":"string"
            },
            "type": {
                "type": "string",
                "enum": [
                    "image",
                    "video"
                ]
            },
            "source": {
                "type": "string",
                "enum": [
                    "console",
                    "pc"
                ]
            },
            "dateUploaded": {
                "type": "string",
                "format": "date-time"
            },
            "segmentTimecode":{
               "type":"object",
               "properties":{
                  "start":{
                     "type":"string",
                     "pattern":"(\\d{2}):(\\d{2}):(\\d{2})"
                  },
                  "end":{
                     "type":"string",
                     "pattern":"(\\d{2}):(\\d{2}):(\\d{2})"
                  }
               },
               "required":[
                  "start",
                  "end"
               ]
            }
         },
         "required":[
            "fileName"
         ]
      },
      "name":{
         "type":"object",
         "minProperties":1,
         "patternProperties":{
            "^[a-z]{2}-[a-zA-Z0-9]+$":{
               "type":"string"
            }
         },
         "additionalProperties":false,
         "examples":[
            {
               "en-US":"Driving",
               "ja-JP":"運転"
            }
         ]
      },
      "description":{
         "type":"object",
         "minProperties":1,
         "patternProperties":{
            "^[a-z]{2}-[a-zA-Z0-9]+$":{
               "type":"string"
            }
         },
         "additionalProperties":false,
         "examples":[
            {
               "en-US":"A free-for-all, where everyone is out to get you!"
            }
         ]
      },
      "objectId":{
         "type":"string",
         "minLength":1,
         "maxLength":32,
         "pattern":"^(?!_)[0-9a-zA-Z\\-\\_]{0,32}$",
         "title":"Object Id",
         "examples":[
            "chapter-tutorial"
         ]
      },
      "activityHintEntity":{
         "type":"object",
         "description":"Hints help players get unstuck in games. Presented on activities, hints can contain a combination of media and text to guide players.",
         "properties":{
            "objectId":{
               "$ref":"#/definitions/objectId"
            },
            "name":{
               "$ref":"#/definitions/name"
            },
            "description":{
               "$ref":"#/definitions/description"
            },
            "activeStatus":{
               "$ref":"#/definitions/activeStatus"
            },
            "links":{
               "$ref":"#/definitions/activityHintLinks"
            }
         },
         "required":[
            "objectId",
            "links"
         ],
         "title":"Hint Entity"
      },
      "trophyHintEntity":{
         "type":"object",
         "description":"Hints help players get unstuck in games. Presented on trophies, hints can contain a combination of media and text to guide players.",
         "properties":{
            "objectId":{
               "$ref":"#/definitions/objectId"
            },
            "name":{
               "$ref":"#/definitions/name"
            },
            "description":{
               "$ref":"#/definitions/description"
            },
            "activeStatus":{
               "$ref":"#/definitions/activeStatus"
            },
            "links":{
               "$ref":"#/definitions/trophyHintLinks"
            }
         },
         "required":[
            "objectId",
            "links"
         ],
         "title":"Trophy Hint Entity"
      }
   }
}
```