'''functions used to find postcodes
	ref_df is the csv file containing the postcode data (import via pandas)
'''

ref_post_df_1 =  ref_post_df.loc[ref_post_df['type'] == 'Delivery Area                                ']

def postcode_dictionary(ref_df):
    #creating a dictionary for postcodes
    temp_df = pd.DataFrame({ref_df['state'].name: ref_df['state'].values,
                            ref_df['suburb'].name: ref_df['suburb'].values,
                            ref_df['postcode'].name: ref_df['postcode'].values})
    temp_df = temp_df.set_index(['state', 'suburb'])
    postcode_dict = temp_df.to_dict()
    return postcode_dict

def find_postcode(row):
    #so elegant!
    return postcode_dictionary(ref_post_df_1)['postcode'][row['MCS State'].upper(), row['CITY'].upper()]