import cv2
from matplotlib import pyplot as plt
from utils import create_df, submission_list, save_pkl, mapk, get_image, plot_rgb, plot_gray
from method1 import store_histogram_total, histograms_to_list
from task5 import haar_wavelet, haar_sticking
import pandas as pd

# Paths
pathDS = "dataset/"
pathQueries = "queries/query_devel_random/"
pathResults = "results/"

# Number of results per query
k = 10
build_dataset=True
pass_queries=True
level=2

# Read Images
dfDataset = create_df(pathDS)
dfQuery = create_df(pathQueries)


if build_dataset==True:
    ## Save image descriptors
    store_histogram_total(dfDataset, pathDS, channel_name=['B','G','R'], level=level)
    
if pass_queries == True:
    # Despres s'ha de cridar la funcio que calcula distancies
    queryImage=pathQueries+"ima_000000.jpg"
    store_histogram_total(dfQuery,pathQueries, channel_name=['B','G','R'], level=level)
    histogram_list_query = histograms_to_list(dfQuery, level, 0)

    for i in range(1):#(len(df)):
        histogram_list_dataset = histograms_to_list(dfDataset, level, i)
        # S'ha de retocar xk accepti aixo
        #distanceList = getX2results(histogram_list_dataset,  histogram_list_query)



# --> MORE HERE <-- #
# --> MORE HERE <-- #
# --> MORE HERE <-- #
# --> MORE HERE <-- #
#
## Texture Descriptors - Haar Wavelets technique + GLCM
#imgTest = get_image(df.iloc[0]['Image'], pathDS)
#grayImg = cv2.cvtColor(imgTest, cv2.COLOR_BGR2GRAY)
#coeff = haar_wavelet(grayImg, level = 0)
#imgHaar = haar_sticking(coeff, level = 0)
#plot_gray(imgHaar)
#
## Save and Evalaute Results..
#resultTest = pd.DataFrame({
#    'Image' : ['im1', 'im3', 'im67', 'im97', 'im69', 'im46'],
#    'Order' : [2, 1, 0, 1, 0, 2],
#    'Query': [1, 1, 1, 2, 2, 2],
#    })
#
#result_list = submission_list(resultTest)
#
#query_list = result_list
#evaluation = mapk(query_list, result_list, k)
#save_pkl(result_list, pathResults)
