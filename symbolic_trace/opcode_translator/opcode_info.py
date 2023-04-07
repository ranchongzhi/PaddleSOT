import opcode

UNARY = {
    "UNARY_POSITIVE",
    "UNARY_NEGATIVE",
    "UNARY_NOT",
    "UNARY_INVERT",
}

BINARY = {
    "BINARY_MATRIX_MULTIPLY",
    "BINARY_POWER",
    "BINARY_MULTIPLY",
    "BINARY_MODULO",
    "BINARY_ADD",
    "BINARY_SUBTRACT",
    "BINARY_SUBSCR",
    "BINARY_FLOOR_DIVIDE",
    "BINARY_TRUE_DIVIDE",
    "BINARY_LSHIFT",
    "BINARY_RSHIFT",
    "BINARY_AND",
    "BINARY_XOR",
    "BINARY_OR",
}

INPLACE = {
    "INPLACE_MATRIX_MULTIPLY",
    "INPLACE_FLOOR_DIVIDE",
    "INPLACE_TRUE_DIVIDE",
    "INPLACE_ADD",
    "INPLACE_SUBTRACT",
    "INPLACE_MULTIPLY",
    "INPLACE_MODULO",
    "INPLACE_POWER",
    "INPLACE_LSHIFT",
    "INPLACE_RSHIFT",
    "INPLACE_AND",
    "INPLACE_XOR",
    "INPLACE_OR",
}

CALL = {
    "CALL_FUNCTION",
    "CALL_FUNCTION_KW",
    "CALL_FUNCTION_EX",
    "CALL_METHOD",
}

COMPARE = {
    "COMPARE_OP",
}

IMPORT = {
    "IMPORT_FROM",
}

ITER = {
    "FOR_ITER",
}

LOAD = {
    "LOAD_BUILD_CLASS",
    "LOAD_CONST",
    "LOAD_NAME",
    "LOAD_ATTR",
    "LOAD_GLOBAL",
    "LOAD_FAST",
    "LOAD_CLOSURE",
    "LOAD_DEREF",
    "LOAD_CLASSDEREF",
    "LOAD_METHOD",
}

MAKE_FUNCTION = {
    "MAKE_FUNCTION",
}

UNPACK = {
    "UNPACK_SEQUENCE",
    "UNPACK_EX",
}


PUSH_ONE = UNARY | BINARY | INPLACE | CALL | COMPARE | IMPORT | ITER | LOAD | MAKE_FUNCTION
PUSH_ARG = UNPACK

ALL_WITH_PUSH = PUSH_ONE | PUSH_ARG

ALL_JUMP = set(opcode.hasjabs + opcode.hasjrel)
REL_JUMP = set(opcode.hasjrel)
ABS_JUMP = set(opcode.hasjabs)

RETURN = {
    "RETURN_VALUE",
}