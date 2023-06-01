# Data Analysis Project - ICO Coffee Data Exports/Imports 1990 to 2019

## This project uses data from...

### http://www.ico.org/new_historical.asp?section=Statistics

## This project uses these skills...

### **Python**, **Microsoft Excel**, **Microsoft SQL Server**, and **PowerBI**

## How does this project work?

### 1. Python Web Scraping Script
The Python Script that can be found in the repo utilizes beautifulsoup & requests libraries in order to download the data sheets from the ICO website.

<img src="https://github.com/cpadierna/DataAnalysis/blob/main/pythonscript_gif.gif" width="500">

### 2. CLeaning the data in Excel
The Excel sheets have been transposed and then INDEX, MATCH, and SUMIFs syntax were mainly used to clean the tranposed data. 
Each stage can be seen in the workbooks.

<img src="https://github.com/cpadierna/DataAnalysis/blob/main/excel_gif.gif" width="500">

### 3. Importing into SQL Server Database
The Excel files were transformed into CSV flat files to create an ease of creating a database in SQL Server.
Once in SQL Server, numerous queries were conducted to get an idea of the data moving forward.

<img src="https://github.com/cpadierna/DataAnalysis/blob/main/sqlserver_gif.gif" width="500">

### 4. Visualizations in PowerBI
The database that the cleaned data was imported into has now been imported into PowerBI. The PowerBI document can be accessed via the repo.
In PowerBI, a star-schema data model was created to relate the data and to ease the process of making visualization to data storytell.
The PowerBI visualization ties together the top importer/exporter for the time period, top-5 exporters/importers data and their trends, etc.

<img src="https://github.com/cpadierna/DataAnalysis/blob/main/powerbi_gif.gif" width="500">

## Take Aways from Project?

### 1. The top-5 importers/exporters and their trends are interesting. This data would be useful for a roastery in terms of sourcing raw coffee beans.
### 2. I am intrigued to learn more about the exporters/importers of roasted coffee and how this compares to the raw coffee importers/exporters.
### 3. I would be additionally interested in comparing the exporter and importer nations with the crop yield years and temperature information for each crop year.

## Thank you for checking out my project!
