from numpy import ndarray

_steps = {
    "1.01": "Convert to Canonical Form for Base Indices of {}",
    "1.02": "Basis (B):\n{}",
    "1.03": "Corresponding Columns of c (C): {}",
    "1.04": "Basis Inverse:\n{}",

    "2.01": "Is {} Feasible?",
    "2.02": "{} is Feasible:",
    "2.03": "* P is in SEF",
    "2.04": "* All Entries of {} is Nonnegative",
    "2.05": "* Constraints are Satisfied (Ax = b)",
    "2.06": "{} is Not Feasible:",
    "2.07": "* Some Entries of {} are Negative",
    "2.08": "* Constraints are Not Satisfied (Ax ≠ b)",
    "2.09": "* Entry at Index {} is Negative",
    "2.10": "* Entry at Index {} is Not a Free Variable",
    "2.11": "* {} • {} = {} and {} is Not ≤ {}",
    "2.12": "* {} • {} = {} and {} is Not ≥ {}",
    "2.13": "* {} • {} = {} and {} is Not ≠ {}",
    "2.14": "* Constraints are Satisfied",
    "2.15": "* All Entries are Either Nonnegative or is a Free Variable"
}

def render_descriptor(key, arguments):
    if not key in _steps:
        raise KeyError(key)

    for i in range(len(arguments)):
        if isinstance(arguments[i], ndarray):
            text = " ".join(filter(None, str(arguments[i]).split(" ")))
            text = text.replace("[ ", "[")
            arguments[i] = text.replace(" ]", "]")

    return _steps[key].format(*arguments)

def assert_correctness(steps):
    pass