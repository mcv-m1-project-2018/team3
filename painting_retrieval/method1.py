from task1 import get_image, compute_histogram, histogram_region


def store_histogram_total(df, path,channel_name, level=0):
    """
    Method to store histograms into the dataframe

    df: dataframe with image names

    channel_name: by default it is set to RGB

    level: level of segmentation in the image

    To access histogram:
    IMAGE | LEVEL0_R | LEVEL0_G | LEVEL0_B | LEVEL1_R | LEVEL1_G | LEVEL1_B |...

    ex:
    - LEVEL0: df["level0_B"].iloc[i][0] will return the histogram values (only one) for image i
    - LEVEL1: df["level1_B"].iloc[i][0..3] each index returns the hist values for the region for image i
    - LEVELN: df["levelN_B"].iloc[i][0..2**N]

    Order of the histograms:
    It follows columns ordering. Example for a level2 image:
    |0|4|08|12|
    |1|5|09|13|
    |2|6|10|14|
    |3|7|11|15|

    """
    channel_name = list(channel_name)

    channels = range(len(channel_name))

    hists= [[histogram_region(get_image(row[0][:], path), c, level) \
             for c in channels ] for index,row in df.iterrows()]

    df['level' + str(level) + "_" + channel_name[0]] = [item[0] for item in hists]
    df['level' + str(level) + "_" + channel_name[1]] = [item[1] for item in hists]
    df['level' + str(level) + "_" + channel_name[2]] = [item[2] for item in hists]

    return hists

def histograms_to_list(df_row, level, channel_name):
    rf=[]
    bf=[]
    gf=[]
    channel_name = list(channel_name)
    #print (channel_name)
    R = 'level' + str(level) + "_"+channel_name[2]
    G = 'level' + str(level) + "_"+channel_name[1]
    B = 'level' + str(level) + "_"+channel_name[0]

    r = df_row[R]
    g = df_row[G]
    b = df_row[B]

    for i in range(len(r)):
        rf.extend([item[0] for item in r[i].tolist()])
        gf.extend([item[0] for item in g[i].tolist()])
        bf.extend([item[0] for item in b[i].tolist()])

    return rf+gf+bf
