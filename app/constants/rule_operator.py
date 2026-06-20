from enum import Enum


class RuleOperator(str, Enum):

    IS_EMPTY = "IS_EMPTY"

    IS_NOT_EMPTY = "IS_NOT_EMPTY"

    EQUALS = "EQUALS"

    NOT_EQUALS = "NOT_EQUALS"

    CONTAINS = "CONTAINS"
