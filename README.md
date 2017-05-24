## Feedback

* Not bad!
* You were off by a minus sign for the force, which was causing bad behavior
  * I fixed it in the code, so you can try running it again now
* The way of initializing points is slightly problematic because it has a high chance of putting two particles in the same position. It was nice that the initialization was different each time, but you might want to use `random.uniform(0,1)` to avoid that issue (almost always).
