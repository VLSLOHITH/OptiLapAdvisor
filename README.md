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

<font color="white">From the above graphs one can observe that there are more number of "8 GB" RAM ,"512 GB" Storage,"15.6" inches screen size, "Non Gaming","No Finger Print Featured", "No OLED Featured", "No SSD Featured","New",around "4 points" Rated,around "50,000 Rs" priced Laptops.<font>



