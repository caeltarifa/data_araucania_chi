# Data Araucania 
Data wrangling, routing, transformation, and system mediation logic.

## Main concerns
1. After the data has been collected, they have to be loaded into remote database.
2. Giving format to xlxs files' tables to json for each file and book that it is inside on it.
3. The data is turned into sql format after json data structure has done in order to load with diagram by itself (i.e. automaticlly).

## 1.   NiFi processors
![nifi design](https://user-images.githubusercontent.com/23003922/207765016-ad4aa477-5516-47cc-985b-c1bdf757f6a9.png)


## 2.   Wranling data from Excel files
In a perfect world, data is clean, structured, and all in one place. That’s every analyst’s dream! But much like most things in life, data is messy and unpredictable.

## 3.   Abstraction and encapsulation: Estatistic National Institute of Chili (INE)
Within INE's data bank, several documents with different format is storaged. This library comprises the process of cleaning and unifying raw, messy and complex data sets for easy access and analysis for Biosoft aproaches. In below is shown the usage.

### 3.1.   Requirements
```
polars==0.15.8
numpy==1.21.6
pandas==1.3.5
xlrd==1.2.0
```

### 3.2.   Main class or how to instance "wrangling procceses"
Reading Excel files by FileReader Class where it requires files' folder to be processed.
```
files = FileReader('/content/data_income')
files.collect_files()
files.show_files()
```

```
1    /content/data_income/numero-upa-practicas-mejoramiento-suelo.xlsx
2    /content/data_income/numero-productores-tramos-edad.xlsx
3    /content/data_income/existencias-colmenas.xlsx
4    /content/data_income/numero-upa-orientación-colmenas.xlsx
5    /content/data_income/01_numero_superficie_de_upa_censadas_regional-xlsx.xlsx
6    /content/data_income/numero-superficie-de-upa-forestal-regional-comunal.xlsx
7    /content/data_income/numero-de-upa-y-superficie-por-categoría-de-uso-del-suelo.xlsx
8    /content/data_income/numero-productores-pueblos-originarios.xlsx
9    /content/data_income/numero-persona-natural-tipo-tenencia.xlsx
10    /content/data_income/tamaño-upa-región-comuna.xlsx
11    /content/data_income/actividad-principal-región.xlsx
12    /content/data_income/numero-superficie-de-upa-frutales-regional-comunal.xlsx
13    /content/data_income/numero-superficie-de-upa-aire-libre-bajo-cubierta-regional-comunal.xlsx
14    /content/data_income/numero-personas-administradoras.xlsx
15    /content/data_income/superficie-principal-sistema-riego.xlsx
16    /content/data_income/superficie-categoría-cultivo-región-comuna.xlsx
17    /content/data_income/trabajo-agrícola.xlsx
18    /content/data_income/existencias-animales.xlsx
19    /content/data_income/numero-superficie-de-upa-riego-secano-regional-comunal.xlsx
20    /content/data_income/tipo-gestión-región-comuna.xlsx
21    /content/data_income/numero-superficie-de-upa-bosque-nativo-regional-comunal.xlsx
```
For each file, the access and analysis over sheet content, structure and design have been into account to specify the work zone as a dataframe.
```
for url_file in files.list_files:
  array_xl = Array_xl(url_file, '/content/data_outcome_ine_cl')

  array_xl.data_wrangling()
  array_xl.data_normalization()
  array_xl.default_dataframe_csv()
  #array_xl.custom_dataframe_csv(1)
  
  array_xl.xl_array.shape
```

![sectorizindata](https://user-images.githubusercontent.com/23003922/209239062-f6882cbe-eb26-462e-bcfb-4e5e76f524d6.png)


![Dataframe](https://user-images.githubusercontent.com/23003922/209751585-2294c36d-4216-49a6-9b60-954cf56e3816.png)




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
