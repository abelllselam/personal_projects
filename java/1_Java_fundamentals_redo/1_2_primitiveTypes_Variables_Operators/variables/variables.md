1. What is a static variable (class variable)?
   - A static variable is tied to the class, not to any single object.
   - There is one copy of a static variable shared by the whole class and all its instances.
   - It’s initialized when the class is loaded by the JVM (before any instances are created or main runs).
   - You can access it using ClassName.variable (recommended) or instance.variable (allowed but less clear).

```java
    public class C {
    static int staticCount = 2; // one shared value for C.class
}
System.out.println(C.staticCount); // valid without creating any C object

```

2. What is an instance field (object field)?
   - An instance field belongs to a particular object (instance) of the class.
   - Each object has its own copy of that field.
   - Instance fields are created and initialized when you call new ClassName() and the constructor runs.

```java
public class C {
    int instanceCount = 3; // unique to each C object
}

C a = new C();
C b = new C();
a.instanceCount = 5;
System.out.println(b.instanceCount); // still 3, because b has its own field

```

3. Why you didn’t need to instantiate staticCount before printing it
   - When the JVM loads the class (before main runs), it:
   - Allocates space for all static fields,
   - Initializes them (explicit initializer values or defaults),
   - Runs any static initialization blocks.
   - Because that happens at class load time, staticCount already exists and has a value when main executes — you don’t need any object instance to access or print it.

Concretely, this is valid:

```java
public class Demo {
    static int staticCount = 2;
    public static void main(String[] args) {
        System.out.println(Demo.staticCount); // prints 2 — no instance needed
    }
}
```

4. Defaults and initialization
   - Static and instance fields get default values if you don’t explicitly initialize them:
     int → 0, boolean → false, object refs → null, etc.
   - Local variables (inside methods) do not get defaults — the compiler forces you to initialize them before use.
5. Practical consequences / patterns
   - Use static for class-wide data or utilities (e.g., counters shared across all objects, constants like public static final int MAX = 10).
   - Be careful: because static data is shared, changes affect all instances — that can cause bugs or thread-safety issues in multi-threaded code.
   - Prefer static for immutable constants (static final) and avoid mutable static state unless you really need shared state.
6. Quick demonstration (what you'd see)

```java
public class VariablesDemo {
    static int staticCount = 2;
    int instanceCount = 3;

    public static void main(String[] args) {
        System.out.println(VariablesDemo.staticCount); // 2 (class field)
        VariablesDemo v = new VariablesDemo();
        System.out.println(v.instanceCount);           // 3 (instance field)
        v.staticCount = 7;                             // allowed, but prefer VariablesDemo.staticCount = 7;
        System.out.println(VariablesDemo.staticCount); // 7 (changed for the whole class)
    }
}

```
