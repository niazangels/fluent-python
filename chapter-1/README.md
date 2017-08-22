# Questions

### What happened when we reversed the French Deck? 
We didn't explicitly ask to reverse the Cards inside. Was this then handled by the iterator? If so, how did it know what to iterate over?

# Quotes

"Note that in both cases, the methods create and return a new instance of Vector , and do not modify either operand — self or other are merely read. This is the
expected behavior of infix operators: to create new objects and not touch their operands." - Page 11-12

"If `__bool__` is not implemented, Python tries to invoke x.`__len__()` , and if that returns zero, bool returns False . Otherwise bool returns True ." - Page 12

"explicit conversion to bool is needed because `__bool__` must return a boolean" - Page 12

"len(x) runs very fast when x is an instance of a built-in type. No method is called for the built-in objects of CPython: the length is simply read from a field in a C struct." - Page 14

"If you only implement one of these special methods, choose `__repr__` , because when
no custom `__str__` is available, Python will call __repr__ as a fallback."