# LOCAL AND GLOBAL SCOPES OF VARIABLE
def to_check_scope():
    def local_scope():
        data = "local data"

    def nonlocal_scope():
        nonlocal data
        data = "nonlocal data"

    def global_scope():
        global data
        data = "global data"

    data = "test data"
    local_scope()
    print("After local scope assignment local scope data : ", data)
    nonlocal_scope()
    print("after non-local scope assignment data: ", data)
    global_scope()
    print("After global scope assignment data: ", data)


to_check_scope()
print("Checking the global scope data: ", data)

"""
local assignment (which is default) did not change scope_test's binding of data. 
The nonlocal assignment changed scope_test's binding of data, 
and the global assignment changed the module-level binding.
"""

