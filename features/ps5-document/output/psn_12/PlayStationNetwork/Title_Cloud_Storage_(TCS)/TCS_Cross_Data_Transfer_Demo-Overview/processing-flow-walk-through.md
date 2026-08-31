# TCS Cross-Platform Data Sharing Demo Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/TCS_Cross_Data_Transfer_Demo-Overview/processing-flow-walk-through.html

# Processing Flow Walk-through

This section describes the processing flow and implementation for setting the update date/time or the slot state and uploading data, for the purpose of preventing conflicts.

# Processing Flow

The upload processing flow and sequence diagram are shown below.

Before starting the upload, carry out the following steps as preparation:

* [Initializing the TcsCrossDataTransferManager Class](preparation.html#topic13117_3_1_1__section_olw_kqz_xxb)
* [Obtaining the Existing TCS Data's Last Update Date and Time](preparation.html#topic13117_3_1_1__section_ozj_lqz_xxb)
* [Generating a Hash Value from the Data to Be Uploaded](preparation.html#topic13117_3_1_1__section_tq5_lqz_xxb)

Once preparation is complete, set the date and time of the last update if TCS data exists, set the state of the slot if TCS data doesn't exist, and start an atomic registration session.

* [(1) Specify the request header that starts the atomic registration session and set supplementary data](setting-the-last-update-date-and-time-and.html#topic13117_3_1_2__section_kg4_nqz_xxb)
* [(2) Obtain the atomic ID from the response header](setting-the-last-update-date-and-time-and.html#topic13117_3_1_2__section_kpl_4qz_xxb)
* [(2)' Set the last update date/time or the slot state in the header](setting-the-last-update-date-and-time-and.html#topic13117_3_1_2__section_zw5_4qz_xxb)
* [(3) Specify the request header when uploading data](setting-the-last-update-date-and-time-and.html#topic13117_3_1_2__section_ryg_pqz_xxb)
* [(4) Upload the data and end the atomic registration session](setting-the-last-update-date-and-time-and.html#topic13117_3_1_2__section_nxv_pqz_xxb)

Steps (1) through (4) are implemented according to the steps in [Title Cloud Storage Service Overview - Using the Service - Uploading and Downloading TCS Data Using the Title Cloud Storage Web API](../../../WebAPI/latest/TCS-Overview/uploading-and-downloading-tcs-data-using-the-title-cloud-sto.html). Refer also to this document for more details.

Upload Processing Flow

Of particular importance is logic (1) to (4), contained in the `setDataInfoThenUploadData()` method of the `TcsCrossDataTransferRequest` class in tcs\_cross\_data\_transfer\_request.cpp.

# Preparation

## Initializing the TcsCrossDataTransferManager Class

Initialize the `TcsCrossDataTransferRequest` class. This logic is contained in the `TcsCrossDataTransferManager` class of tcs\_cross\_data\_transfer\_manager.cpp.

## Obtaining the Existing TCS Data's Last Update Date and Time

Call `TCS::DataApi::getMultiDataStatusesByUser()` to obtain the date and time of the last TCS update if data exists in the TCS data slot. The last update date and time obtained here will be used for preventing conflicts when supplementary data is updated on TCS. The date and time of the last update is not obtained when data is first loaded to TCS or when data in the TCS data slot has been deleted. In such cases, set the state of the slot when uploading TCS data. This logic is contained in `getDataStatusLastUpdatedDateTime()` of the `TcsCrossDataTransferRequest` class in tcs\_cross\_data\_transfer\_request.cpp.

```
// Set the information needed to obtain the update date and time
char strSlotId[4];
const char *fields = "lastUpdatedDateTime";
NpCppWebApi::Common::IntrusivePtr<NpCppWebApi::Common::Vector<NpCppWebApi::Common::IntrusivePtr<TCS::DataStatus>>> dataStatusList;

snprintf(strSlotId, sizeof(strSlotId), "%d", slotId);

// Read the TCS data statuses and obtain the update date and time
getMultiDataStatusesByUser(accountId, strSlotId, fields, dataStatusList);

for (const auto& dataStatus : *dataStatusList) {
    // Obtains the update date and time from the TCS data status
    *expectedTimeTick = dataStatus->getLastUpdatedDateTime();
}

// Read the TCS data status of the specified user slot
TcsCrossDataTransferRequest::getMultiDataStatusesByUser(const char *accountId, const char *slotIds, const char *fields, NpCppWebApi::Common::IntrusivePtr<NpCppWebApi::Common::Vector<NpCppWebApi::Common::IntrusivePtr<TCS::DataStatus>>> &dataStatusList)
{
    NpCppWebApi::Common::Transaction<NpCppWebApi::Common::IntrusivePtr<TCS::GetMultiDataStatusesResponseBody>> transaction;
    NpCppWebApi::Common::IntrusivePtr<TCS::GetMultiDataStatusesResponseBody> body;
    TCS::DataApi::ParameterToGetMultiDataStatusesByUser param;

    transaction.start(m_cppwebapiLibContext);
    param.initialize(m_cppwebapiLibContext, accountId, slotIds;
    param.setfields(fields);

    TCS::DataApi::getMultiDataStatusesByUser(m_webapi2UserCtxId, param, transaction);

    transaction.getResponse(body);
    dataStatusList = body->getDataStatusList();

    param.terminate();
    transaction.finish();
}
```

## Generating a Hash Value from the Data to Be Uploaded

Generate a hash value using the data to be uploaded and its size. This hash value can be used when checking for updates to the TCS data by calling the separately provided `compareHash()`. The function that generates the hash value is contained in the `TcsCrossDataTransferManager` class of tcs\_cross\_data\_transfer\_manager.cpp.

# Setting the Last Update Date/Time or the Slot State and Performing an Atomic Upload

This section explains important logic. All of the content introduced here is contained in `setDataInfoThenUploadData()` of the `TcsCrossDataTransferRequest` class in tcs\_cross\_data\_transfer\_request.cpp.

## (1) Specify the request header that starts the atomic registration session and set supplementary data

Specify "`X-Psn-Atomic-Operation: begin`" in the request header when starting the atomic registration session and execute `setDataInfo()`. By executing `setDataInfo()`, the generated hash value will be written to the supplementary data of the TCS data slot.

```
transactionOfInfo.start(m_cppwebapiLibContext);

TCS::SetDataInfoRequestBodyFactory::create(m_cppwebapiLibContext, info, infoSize, &requestBodyOfInfo);
paramOfInfo.initialize(m_cppwebapiLibContext, accountId, slotId, requestBodyOfInfo);
    
// Start an atomic registration session
paramOfInfo.setxPsnAtomicOperation(TCS::DataApi::ParameterToSetDataInfo::XPsnAtomicOperation::kBegin);
// Set supplementary data
TCS::DataApi::setDataInfo(m_webapi2UserCtxId, paramOfInfo, transactionOfInfo);
```

## (2) Obtain the atomic ID from the response header

An ID for managing the atomic registration session will be issued, and the response header including this atomic ID `"X-Psn-Atomic-Operation-Id: {UUID}"` will be returned. Call `getXPsnAtomicOperationId()` to obtain the atomic ID from the response header.

The atomic ID is an atomic operation ID for identifying the atomic write transaction of TCS data and its associated metadata.

```
// Obtain the response header
transactionOfInfo.getResponseHeaders(headersOfInfo);

// Obtain the atomic ID
atomicOperationId = headersOfInfo->getXPsnAtomicOperationId().c_str();
```

## (2)' Set the last update date/time or the slot state in the header

Set the date and time of the last update of the TCS data obtained in "[Obtaining the Existing TCS Data's Last Update Date and Time](preparation.html#topic13117_3_1_1__section_ozj_lqz_xxb)" in the header when uploading data. `X-Psn-Tcs-Compared-Last-Updated-Date-Time` is the date and time for preventing conflicts. Only execute processing if the last update date and time of the TCS data that is currently registered to the server are the same as the date and time set in the header.

```
char lastUpdatedTime[ISO8601FORMAT_SIZE];
SceRtcDateTime clk;
sceRtcSetTick(&clk, &expectedSavedTick);
snprintf(lastUpdatedTime, ISO8601FORMAT_SIZE, "%04d-%02d-%02dT%02d:%02d:%02d.%03dZ", clk.year, clk.month, clk.day, clk.hour, clk.minute, clk.second, clk.microsecond / 1000);
paramOfData.setxPsnTcsComparedLastUpdatedDateTime(lastUpdatedTime);
```

If the last update data and time have not been obtained, set the state of the slot in the header. `X-Psn-Tcs-If-Slot-State` is the slot state for preventing conflicts. Only execute processing if the slot state of the TCS data that is currently registered to the server is the same as the state set in the header.

```
paramOfData.setxPsnTcsIfSlotState("empty");
```

## (3) Specify the request header when uploading data

Specify the request headers `"X-Psn-Atomic-Operation-Id: {UUID}"` and `"X-Psn-Atomic-Operation: end"` for the final request (the upload request). At this time, set the atomic ID obtained in "[(2) Obtain the atomic ID from the response header](setting-the-last-update-date-and-time-and.html#topic13117_3_1_2__section_kpl_4qz_xxb)" as the header parameter. Upload preparations are now complete.

```
transactionOfData.start(m_cppwebapiLibContext, dataSize);
paramOfData.initialize(m_cppwebapiLibContext, accountId, slotId;

paramOfData.setxPsnAtomicOperation(TCS::DataApi::ParameterToUploadData::XPsnAtomicOperation::END);
paramOfData.setxPsnAtomicOperationId(atomicOperationId;
```

## (4) Upload the data and end the atomic registration session

Finally, start the upload using `uploadData()`, and then send the uploaded data using `sendData()`. This ends the atomic registration session. An error is returned if the update date/time or the slot state does not match.

```
ret = TCS::DataApi::uploadData(m_webapi2UserCtxId, paramOfData, transOfData);
if (ret < SCE_OK) {
    // Upload fails if the date/time or the slot state does not match
    DBG_ERR_TRACE(ret);
    goto error_data;
}

transOfData.sendData(data, dataSize);

error_data: 
    transactionOfData.finish();
    paramOfData.terminate();
```