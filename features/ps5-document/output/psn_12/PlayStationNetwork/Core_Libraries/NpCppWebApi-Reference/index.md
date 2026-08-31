# NpCppWebApi Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/__toc.html

1. Namespace sce::Np::CppWebApi
   1. Summary
      1. [sce::Np::CppWebApi](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/sce-np-cpp-web-api.html "sce::Np::CppWebApi")
2. Namespace sce::Np::CppWebApi::Common
   1. Summary
      1. [sce::Np::CppWebApi::Common](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/sce-np-cpp-web-api-common.html "sce::Np::CppWebApi::Common")
   2. Functions
      1. [sce::Np::CppWebApi::Common::initialize()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/sce-np-cpp-web-api-commoninitialize.html "sce::Np::CppWebApi::Common::initialize()")
      2. [sce::Np::CppWebApi::Common::terminate()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/sce-np-cpp-web-api-commonterminate.html "sce::Np::CppWebApi::Common::terminate()")
      3. [sce::Np::CppWebApi::Common::isWebApiError()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/sce-np-cpp-web-api-commonis-web-api-error.html "sce::Np::CppWebApi::Common::isWebApiError()")
   3. [typedef](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/typedef.html "typedef")
3. Class sce::Np::CppWebApi::Common::InitParams
   1. Summary
      1. [sce::Np::CppWebApi::Common::InitParams](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/sce-np-cpp-web-api-common-init-params.html "sce::Np::CppWebApi::Common::InitParams")
4. Class sce::Np::CppWebApi::Common::LibContext
   1. Summary
      1. [sce::Np::CppWebApi::Common::LibContext](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/sce-np-cpp-web-api-common-lib-context.html "sce::Np::CppWebApi::Common::LibContext")
   2. In-Class Structure
      1. [LibContext::MemoryStats](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/lib-context-memory-stats.html "LibContext::MemoryStats")
   3. Public Member Functions
      1. [LibContext::getMemoryStats()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/lib-contextget-memory-stats.html "LibContext::getMemoryStats()")
5. Class sce::Np::CppWebApi::Common::ParameterBase
   1. Summary
      1. [ParameterBase](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/parameter-base.html "ParameterBase")
   2. Public Member Functions
      1. [ParameterBase::initialize](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/parameter-baseinitialize.html "ParameterBase::initialize")
      2. [ParameterBase::terminate](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/parameter-baseterminate.html "ParameterBase::terminate")
      3. [ParameterBase::setRequestHeader](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/parameter-baseset-request-header.html "ParameterBase::setRequestHeader")
      4. [ParameterBase::unSetRequestHeader](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/parameter-baseun-set-request-header.html "ParameterBase::unSetRequestHeader")
      5. [ParameterBase::setWebtraceTagHeader](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/parameter-baseset-webtrace-tag-header.html "ParameterBase::setWebtraceTagHeader")
      6. [ParameterBase::unSetWebtraceTagHeader](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/parameter-baseun-set-webtrace-tag-header.html "ParameterBase::unSetWebtraceTagHeader")
6. Class sce::Np::CppWebApi::Common::TransactionBase
   1. Summary
      1. [TransactionBase](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/transaction-base.html "TransactionBase")
   2. Public Member Functions
      1. [TransactionBase::start()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/transaction-basestart.html "TransactionBase::start()")
      2. [TransactionBase::finish()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/transaction-basefinish.html "TransactionBase::finish()")
      3. [TransactionBase::abort()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/transaction-baseabort.html "TransactionBase::abort()")
      4. [TransactionBase::getResponseHeaders()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/transaction-baseget-response-headers.html "TransactionBase::getResponseHeaders()")
      5. [TransactionBase::getId()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/transaction-baseget-id.html "TransactionBase::getId()")
      6. [TransactionBase::setResponseInformationOption()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/transaction-baseset-response-information-option.html "TransactionBase::setResponseInformationOption()")
      7. [TransactionBase::getResponseInformationOption()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/transaction-baseget-response-information-option.html "TransactionBase::getResponseInformationOption()")
7. Class sce::Np::CppWebApi::Common::Transaction
   1. Summary
      1. [Transaction](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/transaction.html "Transaction")
   2. Public Member Functions
      1. [Transaction::getResponse()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/transactionget-response.html "Transaction::getResponse()")
      2. [Transaction::hasResponse()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/transactionhas-response.html "Transaction::hasResponse()")
      3. [Transaction::setOnFinishedCallback()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/transactionset-on-finished-callback.html "Transaction::setOnFinishedCallback()")
8. Class sce::Np::CppWebApi::Common::UpStreamTransaction
   1. Summary
      1. [UpStreamTransaction](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/up-stream-transaction.html "UpStreamTransaction")
   2. Public Member Functions
      1. [UpStreamTransaction::start()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/up-stream-transactionstart.html "UpStreamTransaction::start()")
      2. [UpStreamTransaction::sendData()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/up-stream-transactionsend-data.html "UpStreamTransaction::sendData()")
9. Class sce::Np::CppWebApi::Common::DownStreamTransaction
   1. Summary
      1. [DownStreamTransaction](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/down-stream-transaction.html "DownStreamTransaction")
   2. Public Member Functions
      1. [DownStreamTransaction::readData()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/down-stream-transactionread-data.html "DownStreamTransaction::readData()")
10. Class sce::Np::CppWebApi::Common::UpDownStreamTransaction
    1. Summary
       1. [UpDownStreamTransaction](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/up-down-stream-transaction.html "UpDownStreamTransaction")
    2. Public Member Functions
       1. [UpDownStreamTransaction::start()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/up-down-stream-transactionstart.html "UpDownStreamTransaction::start()")
       2. [UpDownStreamTransaction::sendData()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/up-down-stream-transactionsend-data.html "UpDownStreamTransaction::sendData()")
       3. [UpDownStreamTransaction::readData()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/up-down-stream-transactionread-data.html "UpDownStreamTransaction::readData()")
11. Class sce::Np::CppWebApi::Common::DefaultResponse
    1. Summary
       1. [DefaultResponse](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/default-response.html "DefaultResponse")
12. Class sce::Np::CppWebApi::Common::ResponseHeaderBase
    1. Summary
       1. [ResponseHeaderBase](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/response-header-base.html "ResponseHeaderBase")
    2. Public Member Functions
       1. [ResponseHeaderBase::getHeaderValue](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/response-header-baseget-header-value.html "ResponseHeaderBase::getHeaderValue")
13. Class sce::Np::CppWebApi::Common::Binary
    1. Summary
       1. [Binary](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/binary.html "Binary")
    2. Public Member Functions
       1. [Binary::size()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/binarysize.html "Binary::size()")
       2. [Binary::clear()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/binaryclear.html "Binary::clear()")
       3. [Binary::getBinary()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/binaryget-binary.html "Binary::getBinary()")
       4. [Binary::setBinary()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/binaryset-binary.html "Binary::setBinary()")
14. Class sce::Np::CppWebApi::Common::IntrusivePtr
    1. Summary
       1. [Common::IntrusivePtr](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/common-intrusive-ptr.html "Common::IntrusivePtr")
    2. Public Member Functions
       1. [IntrusivePtr::reset()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/intrusive-ptrreset.html "IntrusivePtr::reset()")
       2. [IntrusivePtr::get()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/intrusive-ptrget.html "IntrusivePtr::get()")
       3. [IntrusivePtr::get\_deleter()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/intrusive-ptrgetdeleter.html "IntrusivePtr::get_deleter()")
15. Class sce::Np::CppWebApi::Common::RefObject
    1. Summary
       1. [Common::RefObject](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/common-ref-object.html "Common::RefObject")
    2. Public Member Functions
       1. [RefObject::GetRefCount()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/ref-object-get-ref-count.html "RefObject::GetRefCount()")
16. Class sce::Np::CppWebApi::Common::String
    1. Summary
       1. [Common::String](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/common-string.html "Common::String")
    2. Public Member Functions
       1. [String::copyFrom](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/stringcopy-from.html "String::copyFrom")
       2. [String::append()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/stringappend.html "String::append()")
       3. [String::size()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/stringsize.html "String::size()")
       4. [String::length()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/stringlength.html "String::length()")
       5. [String::find()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/stringfind.html "String::find()")
       6. [String::clear()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/stringclear.html "String::clear()")
       7. [String::c\_str()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/stringcstr.html "String::c_str()")
       8. [String::replace()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/stringreplace.html "String::replace()")
       9. [String::empty()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/stringempty.html "String::empty()")
       10. [String::setContext()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/stringset-context.html "String::setContext()")
17. Class sce::Np::CppWebApi::Common::Vector
    1. Summary
       1. [Common::Vector](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/common-vector.html "Common::Vector")
    2. Public Member Functions
       1. [Vector::pushBack()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/vectorpush-back.html "Vector::pushBack()")
       2. [Vector::size()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/vectorsize.html "Vector::size()")
       3. [Vector::clear()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/vectorclear.html "Vector::clear()")
       4. [Vector::operator[]()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/vectoroperator.html "Vector::operator[]()")
       5. [Vector::empty()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/vectorempty.html "Vector::empty()")
       6. [Vector::begin()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/vectorbegin.html "Vector::begin()")
       7. [Vector::end()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/vectorend.html "Vector::end()")
       8. [Vector::reserve()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/vectorreserve.html "Vector::reserve()")
       9. [Vector::capacity()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/vectorcapacity.html "Vector::capacity()")
       10. [Vector::resize()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/vectorresize.html "Vector::resize()")
       11. [Vector::popBack()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/vectorpop-back.html "Vector::popBack()")
       12. [Vector::insert()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/vectorinsert.html "Vector::insert()")
       13. [Vector::erase()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/vectorerase.html "Vector::erase()")
18. Class sce::Np::CppWebApi::Common::ConstIterator
    1. Summary
       1. [Common::ConstIterator](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/common-const-iterator.html "Common::ConstIterator")
    2. Public Member Functions
       1. [ConstIterator::operator\*()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/const-iteratoroperator.html "ConstIterator::operator*()")
       2. [ConstIterator::operator->()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/const-iteratoroperator-2.html "ConstIterator::operator->()")
       3. [ConstIterator::operator++()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/const-iteratoroperator-3.html "ConstIterator::operator++()")
       4. [ConstIterator::operator++(int)](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/const-iteratoroperatorint.html "ConstIterator::operator++(int)")
       5. [ConstIterator::operator--()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/const-iteratoroperator-4.html "ConstIterator::operator--()")
       6. [ConstIterator::operator--(int)](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/const-iteratoroperator-int.html "ConstIterator::operator--(int)")
       7. [ConstIterator::operator==()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/const-iteratoroperator-5.html "ConstIterator::operator==()")
       8. [ConstIterator::operator!=()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/const-iteratoroperator-6.html "ConstIterator::operator!=()")
19. Class sce::Np::CppWebApi::Common::Iterator
    1. Summary
       1. [Common::Iterator](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/common-iterator.html "Common::Iterator")
    2. Public Member Functions
       1. [Iterator::operator\*()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/iteratoroperator.html "Iterator::operator*()")
       2. [Iterator::operator->()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/iteratoroperator-2.html "Iterator::operator->()")
       3. [Iterator::operator++()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/iteratoroperator-3.html "Iterator::operator++()")
       4. [Iterator::operator--()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/iteratoroperator-4.html "Iterator::operator--()")
       5. [Iterator::operator==()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/iteratoroperator-5.html "Iterator::operator==()")
       6. [Iterator::operator!=()](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/iteratoroperator-6.html "Iterator::operator!=()")
20. Correspondences with Web APIs
    1. [Correspondence Between Namespaces and Web APIs](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/correspondence-between-namespaces-and-web-apis.html "Correspondence Between Namespaces and Web APIs")
    2. [Correspondence Between Web APIs and Library Functions](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/correspondence-between-web-apis-and-library-functions.html "Correspondence Between Web APIs and Library Functions")
21. Common Constants
    1. [SCE\_NP\_CPPWEBAPI\_\*](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/scenpcppwebapi.html "SCE_NP_CPPWEBAPI_*")
    2. [Return Codes](https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/return-codes.html "Return Codes")