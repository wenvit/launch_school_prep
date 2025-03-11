# 4. Refactor this statement to use a regular if statement instead.

# The first expression is an example of a ternary expression

return ('bar' if foo() else qux())

# refactored version:

if foo():
    return 'bar'

else:
    return qux()