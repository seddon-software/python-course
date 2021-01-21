############################################################
#
#    global interpreter lock
#
############################################################

import dis

# The GIL is released every 15 msec, but not during an atomic operation
# Operations consisting of a single byte code are thread safe

dis.dis("x += 1")           # not thread safe
#               0 LOAD_NAME                0 (x)
#               2 LOAD_CONST               0 (1)
#               4 INPLACE_ADD
#               6 STORE_NAME               0 (x)

dis.dis("sort([2,5,3,6])")  # thread safe
#               0 LOAD_NAME                0 (sort)
#               2 LOAD_CONST               0 (2)
#               4 LOAD_CONST               1 (5)
#               6 LOAD_CONST               2 (3)
#               8 LOAD_CONST               3 (6)
#              10 BUILD_LIST               4
#              12 CALL_FUNCTION            1            <== ATOMIC
#              14 RETURN_VALUE