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

## Data Pre-Analysis:
Analyzed the data visually using the matplotlib and seaborn.

### 1.Analysis of renewed laptops correlation with other features

![Screenshot 2024-01-19 163628](https://github.com/VLSLOHITH/OptiLapAdvisor/assets/84633352/76b6e7f9-0e71-414e-a056-e4c7346bb901)
![Screenshot 2024-01-19 163854](https://github.com/VLSLOHITH/OptiLapAdvisor/assets/84633352/777ab809-67c8-492a-8261-4c55dec50cf0)
From the analysis Renewed laptops lack gaming capabilities and fingerprint features, and OLED displays are also uncommon. However, a higher percentage of these laptops come equipped with SSDs, and there is also a significant prevalence of renewed laptops with 8 GB of RAM and 256 GB of storage.Based on this analysis, it becomes evident that the majority of renewed laptops are characterized by average features, and their prices are considerably low (with a maximum of around 40,000 and an average around 20,000), especially when compared to new ones. Additionally, Lenovo emerges as the most prevalent brand among renewed laptops.