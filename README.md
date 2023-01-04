# Data Araucania 
Data wrangling, routing, transformation, and system mediation logic.

## General concerns
1. After the data has been collected, they have to be loaded into remote database.
2. Giving format to xlxs files' tables to json for each file and book that it is inside on it.
3. The data is turned into sql format after json data structure has done in order to load with diagram by itself (i.e. automaticlly).
4. Extract, transform, and load data

## 1.   Wrangling data from Excel files: 
In a perfect world, data is clean, structured, and all in one place. That’s every analyst’s dream! But much like most things in life, data is messy and unpredictable.

   ### Case: [Instituto Nacional de Estadistica - Chile (INE)](https://www.ine.gob.cl/estadisticas)
 
  Several files withim INE's site to be handled are messy, no align to easily read, and they do not have structured a header for storing them. In this section,  we, by seeking the right method, explored different ways to read, transform, and load all data withim Excel files. The most optimal, regarding time of execution and memory output, would be choosen. By the way, below is presented, an example of the INE's excel file, requirements of Python's libraries, and data Pipeline comprised in three paths.
    
  | **Frame of data:** Messy data and unreadeable fields as headers for database |
  |:------------:|
  |![selecting_target](https://user-images.githubusercontent.com/23003922/210661172-659e382f-ffdb-4419-a3b6-d2e93fcac2e6.png) |
  
  
  <details>
    <summary><h3>By Xldr (retrieves data from Excel files)</h3></summary>
    <p>
    Within INE's data bank, several documents with different format is storaged. This library comprises the process of cleaning and unifying raw, messy             and complex data sets for easy access and analysis for Biosoft aproaches. In below is shown the usage.

    This way was built using [Jupyter notebook](https://github.com/caeltarifa/process_distributed_data/blob/main/DW0___data_wrangling_with_XLDR.ipynb).

    - **Requirements**
      ```python
      polars==0.15.8
      numpy==1.21.6
      xlrd==1.2.0
      ```
    - **Datapipeline**
    Main class or how to instance "wrangling procceses".
    Reading Excel files by FileReader Class where it requires files' folder to be processed.

      - [x] `files = FileReader('/content/data_income')`
      - [x] `files.collect_files()`
      - [x] `files.show_files()`

        ```python
        1    /content/data_income/numero-upa-practicas-mejoramiento-suelo.xlsx
        2    /content/data_income/numero-productores-tramos-edad.xlsx
        3    /content/data_income/existencias-colmenas.xlsx
        .
        ```
      For each file, the access and analysis over sheet content, structure and design have been into account to specify the work zone as a dataframe.
      `for url_file in files.list_files:`

      - [x] `array_xl = Array_xl(url_file, '/content/data_outcome_ine_cl')`
      - [x] `array_xl.data_wrangling()`
      - [x] `array_xl.data_normalization()`
      - [x] `array_xl.default_dataframe_csv()` or `array_xl.custom_dataframe_csv(1)`

     - **Outcome** [CSV dataset](https://github.com/caeltarifa/process_distributed_data/tree/main/dataset_censo_agropecuario/outcome/xldr_numpy)

        |  Dataframe on defining range action|
        |:-------------------------:|
        |  ![Dataframe](https://user-images.githubusercontent.com/23003922/209751585-2294c36d-4216-49a6-9b60-954cf56e3816.png)|

    </p>

  </details>
  
  
<details>
  <summary><h3> By PySpark (Parallel computing) </h3></summary>
  <p>
    This solution was built using [Jupyter notebook](https://github.com/caeltarifa/process_distributed_data/blob/main/DW1___data_wrangling_with_Parallel_processing_PySpark.ipynb).

  - **Requirements**
    ```python
    pandas==1.3.5
    numpy==1.21.6
    pyspar==3.3.1
    ```
  - **Datapipeline**
  Main class or how to instance "wrangling procceses".
  Reading Excel files by FileReader Class where it requires files' folder to be processed.

    - [x] `files = FileReader('/content/data_income')`
    - [x] `files.collect_files()`
    - [x] `files.show_files()`

      ```python
      1    /content/data_income/numero-upa-practicas-mejoramiento-suelo.xlsx
      2    /content/data_income/numero-productores-tramos-edad.xlsx
      3    /content/data_income/existencias-colmenas.xlsx
      .
      ```
    For each file, the access and analysis over sheet content, structure and design have been into account to specify the work zone as a dataframe.
    `for xl_file in folder.list_f`

    - [x] `first = spark_dataframe(path_origin=xl_file, path_export="./pyspark/")`
    - [x] `first.remove_nan()`
    - [x] `first.remove_comments()`
    - [x] `first.remove_empty_column()`
    - [x] `first.Establishing_header()`
    - [x] `first.export_to_csv()`

   - **Outcome** [CSV dataset](https://github.com/caeltarifa/process_distributed_data/tree/main/dataset_censo_agropecuario/outcome/xldr_numpy)

      |  Preliminar Dataframe |  Extracting Data|
      |:-------------------------:|:-------------------------:|
      |  ![Preliminar Dataframe](https://user-images.githubusercontent.com/23003922/210667833-c9ec4a11-65d8-46b4-a015-a14af9308402.png)| ![Extracting Data](https://user-images.githubusercontent.com/23003922/210667863-8d18a875-901b-49d0-a2f3-1f9d3e2ee7a7.png) |

  </p>

</details>
  
  

<!--
## 3.   NiFi processors
![nifi design](https://user-images.githubusercontent.com/23003922/207765016-ad4aa477-5516-47cc-985b-c1bdf757f6a9.png)
-->


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

> Xlrd
*   [[Chapter 4] Data Wrangling with Python by Jacqueline Kazil, Katharine Jarmul](https://demo.mobilepit.com/pub/book/DataScience/Data%20Wrangling%20with%20Python.pdf)
*   [Scraping Excel Data with Python](https://medium.com/@tanyashapiro_72192/scraping-excel-data-with-python-41725308d9b0)

> Data wrangling: Fundamentals & best practices 
*   [Data Wrangling with Python by Jacqueline Kazil, Katharine Jarmul](https://demo.mobilepit.com/pub/book/DataScience/Data%20Wrangling%20with%20Python.pdf)
*   [All You Need to Know About Data Wrangling and Importing CSV in Python](https://www.turing.com/kb/data-wrangling-and-importing-csv-in-python)
*   [Master Data Wrangling First: Top 20 Python Libraries + Best Practices](https://pub.towardsai.net/master-data-wrangling-first-top-20-python-libraries-15-best-practices-a07ac7a26efd)
