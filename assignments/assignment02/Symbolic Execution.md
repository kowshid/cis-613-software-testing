First, watch these videos on Symbolic Execution (slides available in the post-class slides area):

- [Symbolic Execution Theory](https://www.youtube.com/watch?v=0znka6M0NDM),
- [Symbolic Execution Application](https://www.youtube.com/watch?v=TdWjS2qm55U).

Second, symbolically execute one of the following code listings (i.e., create a symbolic execution tree) to determine if
it ever returns the wrong result. The code listings are both intended to return the minimum of three inputs or, when
invalid inputs are provided, an error code (e.g., null or None).

**Java Listing**

```java
static Integer minimum(Integer a, Integer b, Integer c) {

    if (a == null || b == null || c == null)
        return null;

    Integer min = a;

    if (min >= c) {
        min = c;

        if (min >= b) {
            min = b;
        }
    }

    return min;
}
```

**Python Listing**

```jupyter
def minimum(a, b, c):

    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return None

    min = a
    if min >= c:
       min = c

        if min >= b:
           min = b

    return min
```

Finally, discuss the symbolic values and path conditional in each of the leaf nodes of the symbolic execution tree to
justify that the code is correct or contains an error. If the code contains an error, provide a concrete set of values
that illustrates the error.

