# Visual Studio Integration for PlayStation®5 User's Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Visual_Studio_Integration_for_PS5-Users_Guide/vsi-appendix-e-thread-sanitizer-errors.html

# Visual Studio Integration for PlayStation®5 User's Guide Appendix E - Thread Sanitizer Errors

| **Error** | **Description** |
| --- | --- |
| `Data race` | The program has performed memory modifications and accesses to the same location from multiple threads without synchronization. |
| `Data race on virtual table pointer (constructor/destructor vs virtual call)` | The program attempted to access an object's virtual table pointer as the object was being constructed or destructed. |
| `Destruction of locked mutex` | A mutex was destroyed while it was locked. |
| `Double locked mutex` | The program has attempted to lock an already locked mutex. |
| `Heap use after free` | The program has attempted to use an address that was previously heap-allocated, but has since been deallocated. |
| `Lock order inversion (potential deadlock)` | A potential deadlock has been identified in the program. |
| `Read lock of a write locked mutex` | The program attempted to read lock a write locked mutex. |
| `Read unlock of a write locked mutex` | The program attempted to read unlock a write locked mutex. |
| `Signal handler spoils errno` | The program changed `errno` from inside a signal handler. |
| `Signal unsafe call inside of a signal` | The program made an unsafe function call from inside a signal handler. |
| `Thread leak` | A thread in the program was not joined after the thread had finished. |
| `Use of an invalid mutex` | The program has attempted to use an invalid mutex, such as before the mutex had been initialized or after it had been destroyed. |
| `Unlock of an unlocked mutex (or by wrong thread)` | The program has attempted to unlock an already unlocked mutex or unlock a mutex on a different thread to the one that locked the mutex. |
| `Virtual table pointer use after free (virtual call vs free)` | The program has attempted to access an object's virtual table pointer after the object has been deallocated. |