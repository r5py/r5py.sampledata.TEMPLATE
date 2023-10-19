#!/usr/bin/env python3


"""Sample data set for r5py, covering CHANGE_THIS, downloaded upon first access."""


import warnings


__version__ = "0.1.1.dev1"
__all__ = ["__version__"]


try:
    from r5py.util.sample_data_set import SampleDataSet

    BASE_URL = f"https://github.com/r5py/CHANGE_THIS/raw/v{__version__}/data/"

    example = SampleDataSet(
        f"{BASE_URL}/example.zip",
        "57d0d5f3359cbd0d42cc7467c51ec9b14e0c9dc1665308246644fbc3bddd9a1f",
    )

    __all__ += [
        "example",
    ]

except ImportError:
    warnings.warn(
        "Install r5py>=0.1.1.dev1 to use the sample data sets",
        RuntimeWarning,
    )
