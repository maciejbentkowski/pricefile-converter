import pytest
import pricefile_scripts_helpers as helpers
import pandas as pd
import numpy.testing as npt



def data_frame_creator(data, correct_data):
    sample_df = pd.DataFrame(data, columns=['pn', 'ss', 'price', 'cuntry_tag'])
    correct_df = pd.DataFrame(correct_data, columns=['pn', 'ss', 'price', 'cuntry_tag'])
    return sample_df, correct_df



def test_strange_characters_replace():
    data = (['0д00001', '', 0.18, 'A'],['0000004', '', 0.10, 'A'],['0000005', '', 0.09, 'A'],['0000006', '', 0.07, 'A'])
    correct_data = (['0D00001', '', 0.18, 'A'],['0000004', '', 0.10, 'A'],['0000005', '', 0.09, 'A'],['0000006', '', 0.07, 'A'])
    sample_df, correct_df = data_frame_creator(data, correct_data)
    pd.testing.assert_frame_equal(helpers.strange_characters_replace(sample_df), correct_df)

def test_drop_pn_null_values():
    data = ([None, '', 0.18, 'A'],['0000004', '', 0.10, 'A'],['0000005', '', 0.09, 'A'],['0000006', '', 0.07, 'A'])
    correct_data = (['0000004', '', 0.10, 'A'],['0000005', '', 0.09, 'A'],['0000006', '', 0.07, 'A'])
    sample_df, correct_df = data_frame_creator(data, correct_data)
    sample_df = helpers.drop_pn_null_values(sample_df)
    pd.testing.assert_frame_equal(sample_df, correct_df)

def test_blank_ss_while_same_as_pn():
    data = (['0000001', '0000001', 0.18, 'A'],['0000004', '', 0.10, 'A'],['0000005', '0000005', 0.09, 'A'],['0000006', '', 0.07, 'A'])
    correct_data = (['0000001', '', 0.18, 'A'],['0000004', '', 0.10, 'A'],['0000005', '', 0.09, 'A'],['0000006', '', 0.07, 'A'])
    sample_df, correct_df = data_frame_creator(data, correct_data)
    sample_df = helpers.blank_ss_while_same_as_pn(sample_df)
    print(sample_df)
    print(correct_df)
    pd.testing.assert_frame_equal(sample_df, correct_df)