import unittest
from unittest.mock import patch
import pandas as pd
import numpy as np

from utils import n_of_images, get_all_images_data, color_tuples_to_array


class Tests(unittest.TestCase):

    @patch('os.listdir')
    def test_n_of_images(self, mock_listdir):
        # GIVEN
        mock_listdir.return_value = [1, 2]
        # WHEN
        result = n_of_images()
        # THEN
        self.assertEqual(result, 2)

    @patch('utils.get_image_data')
    def test_get_all_images_data(self, mock_get_image_data):
        # GIVEN
        input_list = ['abc', 'def']
        # WHEN
        get_all_images_data(input_list)
        # THEN
        self.assertEqual(mock_get_image_data.call_count, 2)

    def test_color_tuples_to_array(self):
        # GIVEN
        column_name = 'color'
        dataframe = pd.DataFrame([{'color': (10, 128, 16), 'dog': 10}, {'color': (11, 110, 198), 'dog': 33}])
        # WHEN
        result = color_tuples_to_array(dataframe, column_name)
        # THEN
        np.testing.assert_almost_equal(result, np.array([[0.03921, 0.50196, 0.06274],
                                                         [0.04313, 0.43137, 0.77647]]), decimal=4)


if __name__ == '__main__':
    unittest.main()
