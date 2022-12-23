# Data Araucania 
Data wrangling, routing, transformation, and system mediation logic.

## Main concerns
1. After the data has been collected, they have to be loaded into remote database.
2. Giving format to xlxs files' tables to json for each file and book that it is inside on it.
3. The data is turned into sql format after json data structure has done in order to load with diagram by itself (i.e. automaticlly).

## NiFi processors
![nifi design](https://user-images.githubusercontent.com/23003922/207765016-ad4aa477-5516-47cc-985b-c1bdf757f6a9.png)


## Wranling data from Excel files
In a perfect world, data is clean, structured, and all in one place. That’s every analyst’s dream! But much like most things in life, data is messy and unpredictable.

![sectorizindata](https://user-images.githubusercontent.com/23003922/209239062-f6882cbe-eb26-462e-bcfb-4e5e76f524d6.png)


## References
> Polar 
*   [Getting Started with the Polars DataFrame Library](https://towardsdatascience.com/getting-started-with-the-polars-dataframe-library-6f9e1c014c5c)
*   [Handling dataframe](https://pola-rs.github.io/polars/py-polars/html/reference/dataframe/index.html)
*   [Read_excel](https://pola-rs.github.io/polars/py-polars/html/reference/api/polars.read_excel.html)
*   [Polars DataFrame library: from Numpy and from Pandas](https://pola-rs.github.io/polars-book/user-guide/introduction.html)

> NumPy 
*   [Normalization & Multidimensional Arrays](https://numpy.org/doc/stable/reference/index.html)

> Pandas 
*   [How to Convert NumPy Array to Pandas DataFrame](https://datatofish.com/numpy-array-to-pandas-dataframe/)
*   [Data wrangling with Pandas](https://exeter-data-analytics.github.io/python-data/pandas.html)

> Xldr
*   [[Chapter 4] Data Wrangling with Python by Jacqueline Kazil, Katharine Jarmul](https://demo.mobilepit.com/pub/book/DataScience/Data%20Wrangling%20with%20Python.pdf)
*   [Scraping Excel Data with Python](https://medium.com/@tanyashapiro_72192/scraping-excel-data-with-python-41725308d9b0)

> Data wrangling: Fundamentals & best practices 
*   [Data Wrangling with Python by Jacqueline Kazil, Katharine Jarmul](https://demo.mobilepit.com/pub/book/DataScience/Data%20Wrangling%20with%20Python.pdf)
*   [All You Need to Know About Data Wrangling and Importing CSV in Python](https://www.turing.com/kb/data-wrangling-and-importing-csv-in-python)
*   [Master Data Wrangling First: Top 20 Python Libraries + Best Practices](https://pub.towardsai.net/master-data-wrangling-first-top-20-python-libraries-15-best-practices-a07ac7a26efd)
