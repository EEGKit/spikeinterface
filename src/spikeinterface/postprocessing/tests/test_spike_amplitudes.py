import unittest
import numpy as np

from spikeinterface.postprocessing import ComputeSpikeAmplitudes
from spikeinterface.postprocessing.tests.common_extension_tests import ResultExtensionCommonTestSuite


class ComputeSpikeAmplitudesTest(ResultExtensionCommonTestSuite, unittest.TestCase):
    extension_class = ComputeSpikeAmplitudes
    extension_function_kwargs_list = [
        dict(),
    ]

if __name__ == "__main__":
    test = ComputeSpikeAmplitudesTest()
    test.setUp()
    test.test_extension()
    # test.test_scaled()
    # test.test_parallel()

    # for k, sorting_result in test.sorting_results.items():
    #     print(sorting_result)
    #     print(sorting_result.get_extension("spike_amplitudes").data["amplitudes"].shape)
