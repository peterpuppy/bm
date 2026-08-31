# NpUniversalDataSystem Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpUniversalDataSystem-Overview/feature-and-overview.html

# NpUniversalDataSystem Code Generation Tool

This topic explains the Host Tool that generates code for executing the creation and posting of events. The functions and structures created using this tool can be embedded in an application to reduce the workload required for implementing event-posting processing.

# Feature and Overview

The NpUniversalDataSystem code generation tool, np-universal-data-system-codegen, is a tool for assisting the implementation of the processing to post events using the NpUniversalDataSystem library. The NpUniversalDataSystem library provides generic API features for creating arbitrarily formatted events; this causes the application's code for creating events to become lengthy.

Although limited to events defined in advance, np-universal-data-system-codegen generates dedicated functions that can be easily called for creating events, assembling their properties, and posting events. The generated code can be embedded in the application to reduce the load of implementing processing for each event.

np-universal-data-system-codegen is a command line tool that is installed on the host PC as follows:

* sdk/host\_tools/bin/np-universal-data-system-codegen.exe

How to use the tool and an overview of the generated code are explained below.

# Development Flow

The code generation flow is indicated in [the following figure](development-flow.html#np-universal-data-system-library-overview_2_2__7534a6d4-e267-11ee-bd3d-0242ac120002).

Code Generation Flow

## Define Events and Obtain the Event Definition File

Define events using the UDS Management Tool. Information of defined events can be downloaded from the UDS Management Tool. Refer to [Universal Data System Guide - Using the UDS Management Tool](../Universal_Data_System-Guide/using-the-uds-management-tool.html) for details on how to define events and on how to download the event definition file.

## Generate the Code

Input the downloaded event definition file and launch np-universal-data-system-codegen. Details on usage are described below.

**Syntax**

```
> np-universal-data-system-codegen.exe [ <options> | <event definition file> ]
```

**Options**

The options that can be specified are as follows:

| **Option** | **Description** |
| --- | --- |
| `/headerpath` or `/hp`  The default is `np_universal_data_system_codegen.h` | Path of the header file to generate |
| `/sourcepath` or `/sp`  The default is `np_universal_data_system_codegen.c` | Path of the source file to generate |
| `/help` or `/h` | Help display |

A hyphen (-) can be used instead of a slash (/) as a symbol to indicate the start of an option.

**Usage Example**

Execute as follows to generate include\post\_event.h, src\post\_event.c from the events\_definition.json event definition file:

```
> np-universal-data-system-codegen.exe -hp include¥post_event.h -sp src¥post_event.c events_definition.json
```

**Supplementary Note**

If the entered event definition file is invalid and code generation fails, a message indicating as such will be output to the console and the processing will end in an error.

## Embed into the Application

Use the generated source file and header file by embedding them to the application project. The generated processing replaces "event creation", "event posting", and "event deletion". Initialization and deletion of the context and handle are still required; carry them out in the same way you would when you're using NpUniversalDataSystem on its own.

# Overview of the Generated Code

The generated code will contain the following elements for each of the defined events:

* Functions to post an event
  + Function to post an event that doesn't include optional properties
  + Function to post an event that includes optional properties
* Definition of an optional property structure
* Function to initialize the optional property structure
* Function to register properties to the optional property structure

The function to post an event is central to the generated code. Event properties are received, an event is created based on those properties, the event is posted, and the event is finally deleted. If the event definition has optional properties, two functions to post an event will be generated.

Arguments corresponding to the required properties will be generated.

If the required property is an array, an argument to specify the number of elements will also be generated. A function (function to post an event) that has three required properties and one or more optional properties is exemplified below:

```
int sceNpUniversalDataSystemCodegenPost<event name>(
	SceNpUniversalDataSystemContext _context,
	SceNpUniversalDataSystemHandle _handle,
	int32_t property1,           // Required property 1
	int32_t property2,           // Required property 2
	const int32_t *property3,   // Required property 3 (array)
	size_t _sizeproperty3,      // Number of elements in required property 3
)
int sceNpUniversalDataSystemCodegenPost<event name>WithOption(
	SceNpUniversalDataSystemContext _context,
	SceNpUniversalDataSystemHandle _handle,
	int32_t property1,          // Required property 1
	int32_t property2,          // Required property 2
	const int32_t *property3,   // Required property 3 (array)
	size_t _sizeproperty3,      // Number of elements in required property 3
	const SceNpUniversalDataSystemCodegen<event name>Option *_option
)
```

If the event definition doesn't have optional properties, `sceNpUniversalDataSystemCodegenPost<`*event name*`>WithOption` will not be generated. If you want to post an event without setting optional properties, use `sceNpUniversalDataSystemCodegenPost<`*event name*`>`.

If, instead, you want to post an event with optional properties set, you must set optional properties in the optional property structure and pass it to `sceNpUniversalDataSystemCodegenPost<`*event name*`>WithOption`. Because of this, the optional property structure and several functions for handling it will be generated for event definitions that have optional properties.

If the optional property is an array, a member to specify the number of elements will also be generated. In addition, bool type members will be generated to select whether or not to use each optional property. A structure that has three optional properties is exemplified below:

```
struct SceNpUniversalDataSystemCodegen<event name>Option {
	int32_t property1,           // Optional property 1
	bool _useproperty1,          // Use optional property 1
	int32_t property2,           // Optional property 2
	bool _useproperty2,          // Use optional property 2
	const int32_t *property3,    // Optional property 3 (array)
	size_t _sizeproperty3,       // Number of elements in optional property 3
	bool _useproperty3           // Use optional property 3
} SceNpUniversalDataSystemCodegen<event name>Option;
```

# Code Generation Example

The implementation of the processing to post events is explained below using three examples of simple event definitions: SampleActivityStart, SampleCustomEvent, and SampleActivityPriorityChange.

## Event Definitions

**SampleActivityStart**

This is an example of an activityStart, which is a type of feature event. It has activityId, which is a required property of the string type, and property1, which is an optional property of the int32 type.

**SampleCustomEvent**

This is an example of a custom event. It has property1, which is an optional property of the int32 type, and property2, which is an array of int32-type optional properties.

**SampleActivityPriorityChange**

This is an example of an activityPriorityChange, which is a type of feature event. It has prioritizedActivities - an object-type array - as a required property.

## Code Generation

When code is generated based on these three events, a header file like the one shown below, containing functions and type definitions, and a source file, containing their implementations, will be generated.

```
/***********************/
/* SampleActivityStart */
/***********************/

typedef struct SceNpUniversalDataSystemCodegenSampleActivityStartOption SceNpUniversalDataSystemCodegenSampleActivityStartOption;
void sceNpUniversalDataSystemCodegenSampleActivityStartOptionInit(
    SceNpUniversalDataSystemCodegenSampleActivityStartOption *_option
    );
void sceNpUniversalDataSystemCodegenSampleActivityStartOptionSetproperty1(
    SceNpUniversalDataSystemCodegenSampleActivityStartOption *_option,
    const int32_t property1
    );
struct SceNpUniversalDataSystemCodegenSampleActivityStartOption {
    int32_t property1;
    bool _useproperty1;
};
int sceNpUniversalDataSystemCodegenPostSampleActivityStart(
    SceNpUniversalDataSystemContext _context,
    SceNpUniversalDataSystemHandle _handle,
    const char *activityId
    );

int sceNpUniversalDataSystemCodegenPostSampleActivityStartWithOption(
    SceNpUniversalDataSystemContext _context,
    SceNpUniversalDataSystemHandle _handle,
    const char *activityId,
    const SceNpUniversalDataSystemCodegenSampleActivityStartOption *_option
    );

/*********************/
/* SampleCustomEvent */
/*********************/

typedef struct SceNpUniversalDataSystemCodegenSampleCustomEventOption SceNpUniversalDataSystemCodegenSampleCustomEventOption;
void sceNpUniversalDataSystemCodegenSampleCustomEventOptionInit(
    SceNpUniversalDataSystemCodegenSampleCustomEventOption *_option
    );
void sceNpUniversalDataSystemCodegenSampleCustomEventOptionSetproperty1(
    SceNpUniversalDataSystemCodegenSampleCustomEventOption *_option,
    const int32_t property1
    );
void sceNpUniversalDataSystemCodegenSampleCustomEventOptionSetproperty2(
    SceNpUniversalDataSystemCodegenSampleCustomEventOption *_option,
    const int32_t *property2,
    size_t _sizeproperty2
    );
struct SceNpUniversalDataSystemCodegenSampleCustomEventOption {
    int32_t property1;
    bool _useproperty1;
    const int32_t *property2;
    size_t _sizeproperty2;
    bool _useproperty2;
};
int sceNpUniversalDataSystemCodegenPostSampleCustomEvent(
    SceNpUniversalDataSystemContext _context,
    SceNpUniversalDataSystemHandle _handle
    );
int sceNpUniversalDataSystemCodegenPostSampleCustomEventWithOption(
    SceNpUniversalDataSystemContext _context,
    SceNpUniversalDataSystemHandle _handle,
    const SceNpUniversalDataSystemCodegenSampleCustomEventOption *_option
    );

/********************************/
/* SampleActivityPriorityChange */
/********************************/

typedef struct SceNpUniversalDataSystemCodegenSampleActivityPriorityChange ObjectPrioritizedActivities SceNpUniversalDataSystemCodegenSampleActivityPriorityChangeObjectPrioritizedActivities;

struct SceNpUniversalDataSystemCodegenSampleActivityPriorityChangeObjectPrioritizedActivities {
    const char *activityId;
    int32_t priority;
};
int sceNpUniversalDataSystemCodegenPostSampleActivityPriorityChange (
    SceNpUniversalDataSystemContext _context,
    SceNpUniversalDataSystemHandle _handle, 
    const SceNpUniversalDataSystemCodegenSampleActivityPriorityChangeObjectPrioritizedActivities *prioritizedActivities,
    size_t _sizeprioritizedActivities
    );
```

## Processing to Post an Event

Processing to post SampleActivityStart using the generated function is provided as an example below.

```
SceNpUniversalDataSystemContext ctxId;
SceNpUniversalDataSystemHandle handle;

// Assume appropriate values are stored in ctxId and handle

// Set optional properties
SceNpUniversalDataSystemCodegenSampleActivityStartOption option;
sceNpUniversalDataSystemCodegenSampleActivityStartOptionInit(&option);
sceNpUniversalDataSystemCodegenSampleActivityStartOptionSetproperty1(&option, 1);
// Post event
ret = sceNpUniversalDataSystemCodegenPostSampleActivityStartWithOption(ctxId, handle, "ABC", &option);
if (ret < 0) {
    // Error handling
}
```

The processing to post SampleCustomEvent using the generated function is exemplified below.

```
SceNpUniversalDataSystemContext ctxId;
SceNpUniversalDataSystemHandle handle;

// Assume appropriate values are stored in ctxId and handle

int32_t property2[] = { 1, 2, 3 };
size_t sizeproperty2 = sizeof(property2) / sizeof(int32_t);

// Set optional properties SceNpUniversalDataSystemCodegenSampleCustomEventOption option;
sceNpUniversalDataSystemCodegenSampleCustomEventOptionInit(&option);
sceNpUniversalDataSystemCodegenSampleCustomEventOptionSetproperty1(&option, 1);
sceNpUniversalDataSystemCodegenSampleCustomEventOptionSetproperty2(&option, property2, sizeproperty2);
// Post event
ret = sceNpUniversalDataSystemCodegenPostSampleCustomEventWithOption(ctxId, handle, &option);
if (ret < 0) {
    // Error handling
}
```

Processing to post SampleActivityPriorityChange using the generated function is provided as an example below.

```
SceNpUniversalDataSystemContext ctxId;
SceNpUniversalDataSystemHandle handle;

// Assume appropriate values are stored in ctxId and handle

SceNpUniversalDataSystemCodegenSampleActivityPriorityChangeObjectPrioritizedActivities activities[] = {{"QuestA", 3}, {"QuestB", 2}, {"QuestC", 1}};
size_t sizeActivities = sizeof(activities) / sizeof(activities[0]);

ret = sceNpUniversalDataSystemCodegenSampleActivityPriorityChange(ctxId, handle, activities, sizeActivities);
if (ret < 0) {
    // Error handling
}
```

# Details of Generated Functions and Structures

## sceNpUniversalDataSystemCodegenPost<*event name*>

Function that posts an <*event name*> event

**Definition**

```
#include <np.h>
int sceNpUniversalDataSystemCodegenPost<event name>(
	SceNpUniversalDataSystemContext _context,
	SceNpUniversalDataSystemHandle _handle,
	[{<required property type> <required property name>,
	size_t _size<required property name>},
	…]
)
```

Arguments

|  |  |
| --- | --- |
| `_context` | [In] Initialization parameters |
| `_handle` | [In] Handle |
| `<`*required property name*`>` | [In] Required property values of the event to post (pointer to the starting element if the required property is an array) |
| `_size<`*required property name*`>` | [In] Number of elements in the array (only when the required property is an array)  Omitted when the required property is not an array |

**Return Values**

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. May also return an error returned by the internally called `sceNpUniversalDataSystemPostEvent()` function or property operating function.

**Description**

This function posts an <*event name*> event to the context specified in `_context`. The number of arguments, their names, and type will differ depending on the event definition. Properties defined as required properties can be specified as individual arguments; properties defined as optional properties can be specified as the optional property structure.

If the argument is an array, specify the number of elements in the array to `_size<`*required property name*`>`.

The user posting an event must be logged in to the PlayStation®5 system.

## sceNpUniversalDataSystemCodegenPost<*event name*>WithOption

Function to post an <*event name*> event with optional properties

**Definition**

```
#include <np.h>
int sceNpUniversalDataSystemCodegenPost<event name>(
	SceNpUniversalDataSystemContext _context,
	SceNpUniversalDataSystemHandle _handle,
	[{<required property type> <required property name>,
	size_t _size<required property name>},
	…],
	const SceNpUniversalDataSystemCodegen<event name>Option *_option
)
```

Arguments

|  |  |
| --- | --- |
| `_context` | [In] Initialization parameters |
| `_handle` | [In] Handle |
| `<`*required property name*`>` | [In] Required property values of the event to post (pointer to the starting element if the required property is an array) |
| `_size<`*required property name*`>` | [In] Number of elements in the array (only when the required property is an array)  Omitted when the required property is not an array |
| `_option` | [In] Pointer to the optional property structure of the event to post, or NULL |

**Return Values**

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. May also return an error returned by the internally called `sceNpUniversalDataSystemPostEvent()` function or property operating function.

**Description**

This function posts an <*event name*> event to the context specified in `_context`. The number of arguments, their names, and type will differ depending on the event definition. Properties defined as required properties can be specified as individual arguments; properties defined as optional properties can be specified as the optional property structure.

If the argument is an array, specify the number of elements in the array to `_size<`*required property name*`>`.

To omit all optional properties, you can specify NULL for `_option`. In this case, the function is equivalent to `sceNpUniversalDataSystemCodegenPost<`*event name*`>`. When setting one or more optional properties, initialize a `SceNpUniversalDataSystemCodegen<`*event name*`>Option` type variable with `sceNpUniversalDataSystemCodegen<`*event name*`>OptionInit`, set the required properties with `sceNpUniversalDataSystemCodegen<`*event name*`>OptionSet<`*property name*`>`, and specify this optional property structure for `_option`.

The user posting an event must be logged in to the PlayStation®5 system.

## SceNpUniversalDataSystemCodegen<*event name*>Option

Optional property structure of an <*event name*> event

**Definition**

```
typedef struct SceNpUniversalDataSystemCodegen<event name>Option {
	[{<Optional property type> <optional property name>;
             size_t _size<optional property name>;
             bool _use<optional property name>;},
	…]
} SceNpUniversalDataSystemCodegen<event name>Option;
```

Members

|  |  |
| --- | --- |
| `<`*optional property name*`>` | Optional property values of the event to post (pointer to the starting element if the optional property is an array) |
| `_size<`*optional property name*`>` | Number of elements in the array (only when the optional property is an array)  Omitted when the optional property is not an array |
| `_use<`*optional property name*`>` | Flag for whether or not to use <*optional property name*> |

**Description**

This structure represents optional properties of an event to post.

When setting optional properties, initialize the structure using `sceNpUniversalDataSystemCodegen<`*event name*`>OptionInit` and then set values to the required properties with `sceNpUniversalDataSystemCodegen<`*event name*`>OptionSet<`*property name*`>`.

## sceNpUniversalDataSystemCodegen<*event name*>OptionInit

Function that initializes the optional property structure of an <*event name*> event

**Definition**

```
void sceNpUniversalDataSystemCodegen<event name>OptionInit(
	SceNpUniversalDataSystemCodegen<event name>Option *_option
)
```

Arguments

|  |  |
| --- | --- |
| `_option` | [In/Out] Pointer to the optional property structure |

**Description**

This function initializes the optional property structure for an event to post.

Use this function first to initialize the optional property structure if you want to set optional properties for an event to post.

## sceNpUniversalDataSystemCodegen<*event name*>OptionSet<*property name*>

Function that registers properties to the optional property structure of an <*event name*> event

**Definition**

```
void sceNpUniversalDataSystemCodegen<event name>OptionSet<optional property name>(
	SceNpUniversalDataSystemCodegen<event name>Option *_option,
	<optional property type> <optional property name>,
             size_t _size<optional property name>
)
```

Arguments

|  |  |
| --- | --- |
| `_option` | [In/Out] Optional properties of the event to post |
| `<`*optional property name*`>` | [In] Optional property values (pointer to the starting element if the optional property is an array) |
| `_size<`*optional property name*`>` | [In] Number of elements in the array (only when the optional property is an array)  Omitted when the optional property is not an array |

**Description**

This function sets values to the members of the optional property structure for an event to post.

For `option`, specify the optional property structure initialized with `sceNpUniversalDataSystemCodegen<`*event name*`>OptionInit()`.

If the applicable property is an array, `_size<`*optional property name*`>` will be added as an argument; specify the number of elements in the array.

## SceNpUniversalDataSystemCodegen<*event name*>Object<*property name*>

<*event name*> event structure that represents a property whose data type is object

**Definition**

```
typedef struct SceNpUniversalDataSystemCodegen<event name>Object<property name> {
	[{<member property type> <member property name>;
             size_t _size<member property name>;
	…]
} SceNpUniversalDataSystemCodegen<event name>Object<property name>;
```

Arguments

|  |  |
| --- | --- |
| `<`*member property name*`>` | [In] Member property values of the properties indicated by <*property name*> (pointer to the starting element if the member property is an array) |
| `_size<`*member property name*`>` | [In] Number of elements in the array (only when the member property is an array)  Omitted when the member property is not an array |

**Description**

This structure represents a property whose data type is object. When the data type is object, the property has member properties, which are represented by the members of the generated structure. Unlike an optional structure, neither an initialization function nor a setting function will be generated; set the values of the member properties directly.