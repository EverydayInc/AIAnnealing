# Current formatter contract

Input:

```text
Item
  Child
```

Released output:

```text
Item
   Child
```

A snapshot test and three downstream examples contain the released output. The supported renderer accepts both two and three leading spaces in this location. Changing the default is reversible in code but changes serialized output and downstream snapshots.
