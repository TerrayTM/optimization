from ._equation import LinearEquation
from ._constraint import VariableConstraint
from typing import Union, Tuple

class MetaVariable(type):
    def __getitem__(cls, key: Union[int, slice]) -> LinearEquation:
        if isinstance(key, slice):
            pass # TODO implement
        elif isinstance(key, int):
            if key <= 0:
                raise ValueError("Variable indexing must starts at 1.")

            key -= 1

        return LinearEquation({key: 1})



    def __le__(self, other: int) -> VariableConstraint:
        if not other == 0:
            raise ValueError()

        return VariableConstraint(negative_variables=[])



    def __ge__(self, other: int) -> VariableConstraint:
        if not other == 0:
            raise ValueError()
        
        return VariableConstraint(positive_variables=[])



class x(object, metaclass=MetaVariable):
    def __init__(self):
        raise NotImplementedError("Incorrect usage of `x`. Please refer to the Pytimize formulation docs.")



def variables(count: int) -> Tuple[LinearEquation]:
    return tuple(LinearEquation({i: 1}) for i in range(count))
    # delay resolving variable keys? TODO
