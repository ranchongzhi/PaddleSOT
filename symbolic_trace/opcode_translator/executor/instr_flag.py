# flags for instructions


class FORMAT_VALUE_FLAG:
    FVC_MASK = 0x3
    FVC_NONE = 0x0
    FVC_STR = 0x1
    FVC_REPR = 0x2
    FVC_ASCII = 0x3
    FVS_MASK = 0x4
    FVS_HAVE_SPEC = 0x4


class MAKE_FUNCTION_FLAG:
    MF_HAS_CLOSURE = 0x08
    MF_HAS_ANNOTATION = 0x04
    MF_HAS_KWDEFAULTS = 0x02
    MF_HAS_DEFAULTS = 0x01
