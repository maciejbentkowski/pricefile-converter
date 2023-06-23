import pricefile_scripts_helpers as helpers
import pandas as pd

### TESTS FOR CHECK PN AND SS COLUMNS

def data_frame_creator(data, correct_data):
    sample_df = pd.DataFrame(data, columns=['pn', 'ss', 'price', 'cuntry_tag'])
    correct_df = pd.DataFrame(correct_data, columns=['pn', 'ss', 'price', 'cuntry_tag'])
    return sample_df, correct_df

### TEST FOR CHECK PN AND SS COLUMNS
###
###


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
    pd.testing.assert_frame_equal(sample_df, correct_df)


### TESTS FOR CHECK PRICE COLUMN
###
###

def test_delete_empty_price_rows():
    data = (['0000001', '', 0.18, 'A'],['0000004', '', 0.10, 'A'],['0000005', '0000006', 1.25, 'A'],['0000006', '', "no price", 'A'],['0000007', '', None, 'A'])
    correct_data = (['0000001', '', 0.18, 'A'],['0000004', '', 0.10, 'A'],['0000005', '0000006', 1.25, 'A'],['0000006', '', "no price", 'A'])
    sample_df, correct_df = data_frame_creator(data, correct_data)
    sample_df = helpers.delete_empty_price_rows(sample_df)
    pd.testing.assert_frame_equal(sample_df, correct_df)

def test_delete_string_price_rows():
    data = (['0000001', '', 'no price', 'A'],['0000004', '', 0.10, 'A'],['0000005', '', 0.09, 'A'],['0000006', '', 0.07, 'A'], ['0000007', '', 'no price', 'A'])
    correct_data = (['0000004', '', 0.10, 'A'],['0000005', '', 0.09, 'A'],['0000006', '', 0.07, 'A'])
    sample_df, correct_df = data_frame_creator(data, correct_data)
    sample_df = helpers.delete_string_price_rows(sample_df, 'no price')
    pd.testing.assert_frame_equal(sample_df, correct_df, check_dtype=False)

def test_delete_zero_price_rows():
    data = (['0000001', '0000004', 3, 'A'],
            ['0000004', '', 0.10, 'A'],
            ['0000005', '', 0.09, 'A'],
            ['0000006', '', 0.07, 'A'],
            ['0000007', '', 0.00, 'A'],
            ['0000008', '0000009', None, 'A'],
            ['0000010', '', 0.00, 'A'],)
    correct_data = (['0000001', '0000004', 3, 'A'],
                    ['0000004', '', 0.10, 'A'],
                    ['0000005', '', 0.09, 'A'],
                    ['0000006', '', 0.07, 'A'],
                    ['0000008', '0000009', None, 'A'])
    sample_df, correct_df = data_frame_creator(data, correct_data)
    sample_df = helpers.delete_zero_price_rows(sample_df)
    pd.testing.assert_frame_equal(sample_df, correct_df, check_dtype=False)

def test_remove_chain_without_price():

    data = (['0000001', '', 0.18, 'A'],
        ['0000004', '', 0.10, 'A'],
        ['0000005', '0000006', None, 'A'],
        ['0000006', '', 4.25, 'A'],
        ['0000007', '', 51.53, 'A'],
        ['0000009', '0000011', None, 'A'],
        ['0000020', '', 41.51, 'A'],
        ['0000011', '', 3.51, 'A'],
        ['0000010', '0000012', None, 'A'],
        ['0000012', '0000013', None, 'A'],
        ['0000013', '0000014', None, 'A'])
    

    correct_data = (['0000001', '', 0.18, 'A'],
            ['0000004', '', 0.10, 'A'],
            ['0000005', '0000006', None, 'A'],
            ['0000006', '', 4.25, 'A'],
            ['0000007', '', 51.53, 'A'],
            ['0000009', '0000011', None, 'A'],
            ['0000020', '', 41.51, 'A'],
            ['0000011', '', 3.51, 'A'])

    sample_df, correct_df = data_frame_creator(data, correct_data)
    print(sample_df)
    sample_df = helpers.remove_chain_without_price(sample_df)
    print(sample_df)
    pd.testing.assert_frame_equal(sample_df, correct_df, check_dtype=False)

def test_replace_comma_with_dot():
    data = (['0000001', '', "0,18", 'A'], ['0000004', '', "0,10", 'A'], ['0000005', '', "0,09", 'A'], ['0000006', '', 0.07, 'A'], ['0000007', '', 0.00, 'A'], ['0000008', '0000009', 0.03, 'A'])
    correct_data = (['0000001', '', 0.18, 'A'], ['0000004', '', 0.10, 'A'], ['0000005', '', 0.09, 'A'], ['0000006', '', 0.07, 'A'], ['0000007', '', 0.00, 'A'], ['0000008', '0000009', 0.03, 'A'])
    sample_df, correct_df = data_frame_creator(data, correct_data)
    sample_df = helpers.replace_comma_with_dot(sample_df)
    pd.testing.assert_frame_equal(sample_df, correct_df, check_dtype=False)

