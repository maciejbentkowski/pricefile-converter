import pricefile_scripts_helpers as helpers
import pandas as pd

def data_frame_creator(data, correct_data):
    sample_sample_df = pd.DataFrame(data, columns=['pn', 'ss', 'price', 'cuntry_tag'])
    correct_sample_df = pd.DataFrame(correct_data, columns=['pn', 'ss', 'price', 'cuntry_tag'])
    return sample_sample_df, correct_sample_df



def test_full_ford_at_script():
    data = (['0000001', '', 0.18, 'A'],
            ['0д00002', '', 0.23, 'A'],
            [None, '', 0.36, 'A'],
            ['0000004', '0000004', 0.45, 'A'],
            ['0000005', '', None, 'A'],
            ['0000006', '', 'KEIN PREIS', 'A'],
            ['0000007', '', 0.00, 'A'],
            ['0000008', '', 0.86, 'A'],
            ['0000009', '0000010', None, 'A'],
            ['0000010', '0000011', None, 'A'],
            ['0000011', '0000012', None, 'A'],
            ['0000013', '0000014', None, 'A'],
            ['0000015', '', 15.51, 'A'],
            ['0000014', '', 14.41, 'A'],
            ['0000016', '', '16,61', 'A'])
    
    correct_data = (['0000001', '', 0.18, 'A'],
                    ['0D00002', '', 0.23, 'A'],
                    ['0000004', '', 0.45, 'A'],
                    ['0000008', '', 0.86, 'A'],
                    ['0000013', '0000014', None, 'A'],
                    ['0000015', '', 15.51, 'A'],
                    ['0000014', '', 14.41, 'A'],
                    ['0000016', '', 16.61, 'A'])

    sample_df, correct_df = data_frame_creator(data, correct_data)
    sample_df = helpers.strange_characters_replace(sample_df)
    sample_df = helpers.clear_ss_while_there_is_no_equivalent_pn(sample_df)
    sample_df = helpers.drop_pn_null_values(sample_df)
    sample_df = helpers.blank_ss_while_same_as_pn(sample_df)
    sample_df = helpers.delete_empty_price_rows(sample_df)
    sample_df = helpers.delete_zero_price_rows(sample_df)
    sample_df = helpers.delete_string_price_rows(sample_df, 'KEIN PREIS')

    print(sample_df)
    sample_df = helpers.replace_comma_with_dot(sample_df)
    print(sample_df)
    sample_df = helpers.remove_chain_without_price(sample_df)
    pd.testing.assert_frame_equal(sample_df, correct_df, check_dtype=False)
