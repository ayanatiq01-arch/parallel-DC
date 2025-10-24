<<<<<<< HEAD
# Chapter 2 – Threading with Lock Demonstration

![Thread Demonstration](https://raw.githubusercontent.com/ayanatiq01-arch/parallel-DC/main/P-DC/thread.JPG)

![Lock Demonstration](https://raw.githubusercontent.com/ayanatiq01-arch/parallel-DC/main/P-DC/lock.JPG)

![Lock 2 Demonstration](https://raw.githubusercontent.com/ayanatiq01-arch/parallel-DC/main/P-DC/lock2.JPG)

---

## Conclusion (LOCK)

1. **Without Lock:**  
   - Execution Time: **~3.006 seconds**  
   - Observation: Multiple threads accessed and modified the shared variable (`account_balance`) simultaneously.  
   - Result: Faster execution but **incorrect and inconsistent** final balance due to race conditions.

2. **With Partial Lock:**  
   - Execution Time: **~3.004 seconds**  
   - Observation: Threads were synchronized during certain operations only.  
   - Result: **Improved accuracy** compared to the unlocked version, but occasional inconsistencies still occurred.

3. **With Full Lock:**  
   - Execution Time: **~11 seconds**  
   - Observation: Each thread waited for its turn to fully access and update the shared resource.  
   - Result: **Completely accurate and consistent** results, but execution was slower due to sequential thread execution.


**Final Verdict:**  
Using a lock ensures **data accuracy and consistency** by preventing race conditions but increases **execution time**. Without a lock, threads run faster but cause data corruption. Therefore, choosing between speed and accuracy depends on the nature of the application.
=======

**Event, Barrier, Condition**
![event,barrier,condition](https://raw.githubusercontent.com/ayanatiq01-arch/parallel-DC/a423383b2c95e85d3a54cc7097531a248c5b107a/P-DC/event%2Cbarrier%2Ccondition%20sc.JPG)

## Conclusion

This project demonstrates three distinct thread synchronization mechanisms in Python — Event, Barrier, and Condition — through a race car simulation. Each approach showcases a different way to coordinate multiple threads. In the Event example, the controller signals all cars to start simultaneously after preparation, illustrating one-to-many communication. In the Barrier version, all threads wait at a common point until everyone is ready, emphasizing synchronization at a shared checkpoint. The Condition example uses a lock-based wait and notify approach, where the controller explicitly notifies all waiting cars to begin. The outputs confirm that each mechanism achieves thread coordination differently while producing logically consistent results.

>>>>>>> d05f7f3399cbcc2f92c25d38fca285d6c4137491
