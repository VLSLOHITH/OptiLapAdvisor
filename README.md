# OptiLapAdvisor

## Introduction
It serves as a compact search engine dedicated to assisting users in finding the ideal laptop. For those facing challenges in the quest for a new laptop, this tool can prove invaluable by pinpointing the most optimal options based on specific features such as 'RAM,' 'Storage,' 'Screen Size,' 'Price,' and 'Type of laptop' tailored to usage purposes like 'Lower Generation' for basic tasks, 'Middle Generation' for coding and office work, and 'Higher Generation' for more complex applications. After receiving the results, users can further refine their choices by applying filters for 'Brand,' 'Processor,' 'RAM,' 'Storage,' 'Screen Size,' 'Price,' 'Gaming laptop,' 'Fingerprint feature,' 'OLED screen,' 'SSD,' 'Rating', and 'Renewed.' Ultimately, this streamlined process ensures that individuals can easily discover their perfect laptop match. 

## Data Collection:
Acquired data through web scraping of Amazon's e-commerce website, specifically extracting information from HTML pages related to laptop sales. Utilized the Beautiful Soup Python package to extract details such as laptop brand, processor, price, and various other attributes. Subsequently, compiled and saved the consolidated data into an Excel worksheet.
Tools used: BeautifulSoup

## Data Restructuring and Cleaning:
After extracting laptop data from the HTML pages, the information was initially presented in sentence form, describing various features. However, to organize the data more efficiently, we needed to transform it into a separate column format. Given the impracticality of manually performing this operation on a large dataset, the Python 're' module was employed to identify regular expressions associated with key attributes such as 'RAM,' 'Brand,' 'Size,' 'Storage,' 'Processor,' 'Fingerprint,' 'Gaming,' 'OLED,' 'SSD,' and 'Renewed.' Subsequently, these elements were parsed and separated using regular expressions. With the assistance of the 'pandas' library, the parsed data was then structured into a dataframe.

The data within the dataframe remains in a raw format, comprising a mix of numerical and string values. The next step involves parsing the data into distinct numerical and categorical forms. Subsequently, the data will be converted into their respective data types and updated in a series of dataframes. Additionally, a check will be conducted for null values within the dataframe. If a significant number of null values are identified, they will be replaced with the median value. For cases where only a few null values are present, the respective rows containing null values will be deleted. In instances where a substantial number of null values are found, the corresponding columns will be removed.
Tools used: re, pandas, numpy

## Data Pre-Analysis:![Screenshot 2024-01-19 170117](https://github.com/VLSLOHITH/OptiLapAdvisor/assets/84633352/d52af99a-a61b-4daf-8d34-8a2e12cebf25)

Analyzed the data visually using the matplotlib and seaborn.

### 1.Analysis of renewed laptops correlation with other features

![Screenshot 2024-01-19 163628](https://github.com/VLSLOHITH/OptiLapAdvisor/assets/84633352/76b6e7f9-0e71-414e-a056-e4c7346bb901)
![Screenshot 2024-01-19 163854](https://github.com/VLSLOHITH/OptiLapAdvisor/assets/84633352/777ab809-67c8-492a-8261-4c55dec50cf0)

From the analysis Renewed laptops lack gaming capabilities and fingerprint features, and OLED displays are also uncommon. However, a higher percentage of these laptops come equipped with SSDs, and there is also a significant prevalence of renewed laptops with 8 GB of RAM and 256 GB of storage.Based on this analysis, it becomes evident that the majority of renewed laptops are characterized by average features, and their prices are considerably low (with a maximum of around 40,000 and an average around 20,000), especially when compared to new ones. Additionally, Lenovo emerges as the most prevalent brand among renewed laptops.

### 2.Analysis of Brand.
![Screenshot 2024-01-19 165020](https://github.com/VLSLOHITH/OptiLapAdvisor/assets/84633352/3c6a0646-cf91-4f20-9812-78c7d17999e3)
![Screenshot 2024-01-19 165119](https://github.com/VLSLOHITH/OptiLapAdvisor/assets/84633352/aae3f8b9-4578-4e69-a32c-65b489e00ac5)
![Screenshot 2024-01-19 165211](https://github.com/VLSLOHITH/OptiLapAdvisor/assets/84633352/fb85eda3-c1c5-47a8-a33c-055e06b72eba)
![Screenshot 2024-01-19 165318](https://github.com/VLSLOHITH/OptiLapAdvisor/assets/84633352/e5813273-bbdc-4f0f-828b-e2dec00cdb18)
![Screenshot 2024-01-19 165421](https://github.com/VLSLOHITH/OptiLapAdvisor/assets/84633352/8442c0a6-cbeb-48b1-aa90-74e3c82b620a)
![Screenshot 2024-01-19 165545](https://github.com/VLSLOHITH/OptiLapAdvisor/assets/84633352/fab8f837-a3df-4cba-be9a-ca481d62d31c)
![Screenshot 2024-01-19 165750](https://github.com/VLSLOHITH/OptiLapAdvisor/assets/84633352/6701c5be-3d2f-45ec-a0dc-c903d4b38e46)
![Screenshot 2024-01-19 170020](https://github.com/VLSLOHITH/OptiLapAdvisor/assets/84633352/ae151a87-7428-4b35-89f6-bc7b2819d016)
![Screenshot 2024-01-19 170052](https://github.com/VLSLOHITH/OptiLapAdvisor/assets/84633352/a019c9e9-7c48-4b8b-9693-912314eb00bb)
![Screenshot 2024-01-19 170117](https://github.com/VLSLOHITH/OptiLapAdvisor/assets/84633352/a1e7e9ce-7399-4e0e-98a3-cc42e44239a5)
![Screenshot 2024-01-19 170248](https://github.com/VLSLOHITH/OptiLapAdvisor/assets/84633352/c425023a-3162-4c5a-86f1-e6c08d169036)

### 3.In the Final Part of Data Analysis, We can correlate the Remaining Fetures using Pair Wise plot.
![Screenshot 2024-01-19 172313](https://github.com/VLSLOHITH/OptiLapAdvisor/assets/84633352/ed9befb4-7753-4269-a38c-42227fba6430)
![Screenshot 2024-01-19 172514](https://github.com/VLSLOHITH/OptiLapAdvisor/assets/84633352/c5dd434c-031d-4276-ac2d-2edb4fc4668c)
From the off-diagonal graphs in the (Price vs Rating) graph, one can observe a higher density at the (price, rating) value around (50,000, 4). In the (Renewed vs Price) graph, renewed laptops are predominantly priced below 50,000 Rs. In the (Gaming vs Rating, Finger Print vs Rating, OLED vs Rating) graphs, laptops featuring gaming capabilities, fingerprint recognition, and OLED displays exhibit a distribution with high ratings, with the minimum rating hovering around "3". In the (Price vs SSD) graph, laptops without SSDs are priced less than 50,000 Rs. Lastly, in the (Size vs Price) graph, most laptops with a size of 15.6 inches fall within the price range of 25,000 to 50,000 Rs.

<h3 color="blue">From the above graphs one can observe that there are more number of "8 GB" RAM ,"512 GB" Storage,"15.6" inches screen size, "Non Gaming","No Finger Print Featured", "No OLED Featured", "No SSD Featured","New",around "4 points" Rated,around "50,000 Rs" priced Laptops.<h3>

## Data Preprocessing:
Through Label Encoding, the ordinal categorical values of processors are transformed into numerical representations, taking into account their Thermal Design Power (TDP) ratings and categorizing them into three classes(Low Generation, Mid Generation, High Generation.)
![Screenshot 2024-01-19 173754](https://github.com/VLSLOHITH/OptiLapAdvisor/assets/84633352/11944a47-cf59-46e6-8af8-0fc12b02a490)
![Screenshot 2024-01-19 173813](https://github.com/VLSLOHITH/OptiLapAdvisor/assets/84633352/0dd04a92-d37e-4e13-a310-43cce3207d88)
Tools used: Matplotlib, Seaborn

## Dealing with the Outliers:
Here, we are exclusively assessing "RAM," "storage," "Size," "Processor Type," and "Price" while omitting consideration for other features. This is because we are solely utilizing these specific features as key factors for our model.

![Screenshot 2024-01-19 203625](https://github.com/VLSLOHITH/OptiLapAdvisor/assets/84633352/dd7d572b-77f3-44eb-b35d-b8dec0deea46)

Here, we are not excluding the outliers from the Processor and Storage Features. This decision is based on the nature of these features, which are not continuous. Moreover, the outliers, especially in the case of processors, carry significance. For instance, when comparing mid-generation processors, there are notably fewer instances of both low and high-generation processors. However, these outliers matter, particularly when individuals are interested in purchasing laptops within those specific sections. Similarly, in the case of storage features, there is a higher prevalence of 512GB laptops compared to 256GB laptops.

We have used IQR method for detecting the outliers and excluding them from the data which we use for our model.

## Creating the Model:
We employ clustering to identify laptops that closely match the requirements sought by the finder. Specifically, we utilize Agglomerative Hierarchical Clustering instead of K-means due to its iterative nature. In Agglomerative Hierarchical Clustering, clusters are formed every time the data is updated, offering a fresh approach to grouping. This differs from K-means, which stores previous clusters, requiring us to then determine which cluster aligns with our specified requirements.
Scaling the data to prevent any single feature from dominating others; for this purpose, we employed standardization, ensuring a mean of 0 and a maximum standard deviation of 1.
### Deciding number of clusters
1.Plotting the Bent elbow,Dendogram to check for the number of clusters.

i)Bent Elbow curve

![Screenshot 2024-01-19 215428](https://github.com/VLSLOHITH/OptiLapAdvisor/assets/84633352/53cadb99-61b8-48c9-9202-5270f95af315)


ii)Dendogram

![Screenshot 2024-01-19 215600](https://github.com/VLSLOHITH/OptiLapAdvisor/assets/84633352/c963f42c-cc5a-4380-b286-b0c5851e8724)


Here, it is unclear that where the elbow is, we cant find the number of clusters from this but from the dendogram plot we can say that the inter clustering is either 3 or 4.

2.Checking the Silhouette Score and CH Score.

For the good cluster both the Silhouette Score and CH Score is maximum and for the "3" clusters it is max when compared with "4".
for n_clusters=3

silhouette_score: 0.33397633394771564

calinski_harabasz_score: 150.86539712098767

for n_clusters=4

silhouette_score: 0.3254319240222683

calinski_harabasz_score: 135.13784192329877

<h3>So, we are considering 3 clusters and it will also signifies the three generation laptops and we will see this at the end of this model.</h3> 

According to research the size of a good cluster should be between 5% and 35% of total size.

Cluster0 population:29.86

Cluster2 population:32.96

Cluster1 population:31.83

Done the Principal Component Analysis for the visualization of cluster and how the features are dominating the others.

Scree Plot:

![Screenshot 2024-01-19 220812](https://github.com/VLSLOHITH/OptiLapAdvisor/assets/84633352/674696f0-9a6f-43b1-9cf7-4f955ff0809d)

Here, from the scree plot we can see that the "PC1" have percentage and mainly dependent variable in the cluster and next to that is "PC2". So, by using both the PC1 and PC2 we can visualize the clustering. 

Visualizing the Clusters in 2D Scatter Plot using the PCA:

![Screenshot 2024-01-19 221018](https://github.com/VLSLOHITH/OptiLapAdvisor/assets/84633352/c3f47ad5-f9e0-4597-9638-0e8ebc99535f)

Tools used: AgglomerativeClustering, silhouette_score, calinski_harabasz_score, StandardScalar, scipy, PCA.

## Fitting the new data to the Agglomerative Clustering Model.

Adding New data to the existing data for the prediction.

![Screenshot 2024-01-20 122110](https://github.com/VLSLOHITH/OptiLapAdvisor/assets/84633352/2310293b-2b12-4c0d-8c26-83b358ae03ec)

Here, we are seeking recommendations for a mid-generation laptop suitable for coding, office tasks, and gaming. Our specifications include a preference for 8 GB RAM, 512 GB storage, a 15.6-inch screen size, and a budget of around Rs. 45,000
Result:

![Screenshot 2024-01-20 122131](https://github.com/VLSLOHITH/OptiLapAdvisor/assets/84633352/0d67443c-d920-4a4e-ae18-e9c4703f15aa)


### Filtering.

Assign the values if you want to filter the perticular feature in their respective Tab else leave it as None.

![Screenshot 2024-01-19 222417](https://github.com/VLSLOHITH/OptiLapAdvisor/assets/84633352/c9c53400-5cb0-4cf6-b088-3c6525354208)


Here, we are specifically filtering for a gaming laptop under the Lenovo brand.

Final Result after filtering:

![Screenshot 2024-01-20 122225](https://github.com/VLSLOHITH/OptiLapAdvisor/assets/84633352/b608e3a7-ec13-4b8a-89a0-b37e1b6a9ee0)


cluster 1 =>  mix of low end and mid generation.

cluster 2 => mix of mid and high generation.

cluster 3 => mid generation.

<font color='red'>Note: If you want the High Generation laptops then please check even the outlier cluster because this cluster mostly consisits with that laptops<font>

![Screenshot 2024-01-19 222638](https://github.com/VLSLOHITH/OptiLapAdvisor/assets/84633352/4fe5dc2d-766a-47fb-bad0-3f9fa7cdb319)

## Final Distribution:

![Screenshot 2024-01-20 122322](https://github.com/VLSLOHITH/OptiLapAdvisor/assets/84633352/c9d588e1-0c93-40da-8f45-9aea8dcaec32)


This represents the distribution of our recommended laptops, and upon closer examination, it is evident that they follow a normal distribution with minimal outliers. Furthermore, our selection process has successfully identified laptops that align closely with the specified requirements.

Hence, a sucessfull model!!

