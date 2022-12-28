import polars as pl
import xlrd as xls
import numpy as np
import os

class Array_xl:
  work_book = xls.open_workbook("url_bookincome")
  xl_array = np.array([])
  url_bookincome = ""
  url_bookoutside = ""

  def __init__(self, url_bookincome, url_bookoutside, index=0):
    self.url_bookincome = url_bookincome
    self.url_bookoutside = url_bookoutside
    self.work_book = xls.open_workbook(url_bookincome)
    self.work_book = self.work_book.sheet_by_index(index)
    self.to_ndimention_xls()
    self.create_folder_outcome()

  def to_ndimention_xls(self):
    """ Proccessing data and giving Numpy array format: source excel file """

    rack_book = np.array(['']*self.work_book.ncols, dtype='<U32')
    for i in range(self.work_book.nrows):
      rack_book = np.vstack( ( rack_book, np.array(self.work_book.row_values(i), dtype='<U32') ) )    
    self.xl_array = rack_book
  
  def show_work_book(self):
    """ show work_rows' rows """
    for i in work_book.get_rows():
      print(i)
  
  def show_array_excel(self):
    """ show array excel's rows """
    if len(self.xl_array):
      for i in self.xl_array:
        print(i)
  
  def get_ncols(self):
    _, b = self.xl_array.shape
    return b
  def get_nrows(self):
    a, _ = self.xl_array.shape
    return a

  def extending_values_blanckspaces(self):
    """ extextending values toward blank cells: source xl_array"""
    nrows, ncols = self.get_nrows(), self.get_ncols()
    rack_rows = np.array([False]*ncols)
    for i in range(nrows):
      array_row = self.xl_array[i]
      for index in range(len(array_row)):##going by columns
        if array_row[index] == '' and index > 0:
          self.xl_array[i, index] = self.xl_array[i, index-1]

  def remove_empty_rows(self):
    """ Removing empty rows: source xl_array """
    nrows, ncols = self.get_nrows(), self.get_ncols()
    c = 0
    while c < nrows:
      nempty = self.xl_array[c].tolist().count('')
      if nempty == ncols:
        self.xl_array = np.delete( self.xl_array, c, 0)
        nrows = self.get_nrows()
      else:
        c+=1

  def remove_empty_cols(self):
    """ removing empty columns: source xl_array"""
    nrows, ncols = self.get_nrows(), self.get_ncols()
    
    for i in range(1, ncols):
      nempty = self.xl_array[:, i-1:i]
      nempty = np.transpose(nempty).tolist()[0].count('')
      if float(nempty/nrows) >= 0.75 :
        self.xl_array = self.xl_array[:, i:]
  
  def is_empty_col(self, col:int):
    """ Verifying if this column is empty: source xl_array"""
    nrows, ncols = self.get_nrows(), self.get_ncols()
    if col < ncols:
      col+=1
      nempty = self.xl_array[:, col-1:col]
      nempty = np.transpose(nempty).tolist()[0].count('')
      if nempty == nrows :
        return True
      else:
        return False
    else:
      print("Col out of range")

  def is_empty_row(self,row:int):
    """## Verifying if this row is empty: source self.xl_array"""
    nrows, ncols = self.get_nrows(), self.get_ncols()
    if row < nrows:
      nempty = self.xl_array[row].tolist().count('')
      if nempty == ncols:
        return True
      else:
        return False
    else:
      print("Row out of range")
    


  def remove_head_comments(self):
    """ Removing comments head 1. By a row with contente between before and after blank line 2 and if it would be the first and unique column with data: source self.xl_array """
    nrows, ncols = self.get_nrows(), self.get_ncols()
    empty = False
    row_remove=[]
    index=0
    while index < int(nrows*0.3):
      if self.is_empty_row(index):
        row_remove.append(index)
      index+=1

    if len(row_remove):
      row_remove = np.arange(row_remove[0],row_remove[-1])
      self.xl_array = np.delete(self.xl_array, row_remove, axis=0)


  def extending_values_blanckspaces_col(self):
    """ Filling blank spaces in columns"""
    self.xl_array = np.transpose(self.xl_array)
    self.extending_values_blanckspaces()
    self.xl_array = np.transpose(self.xl_array)

  def remove_bottom_comments(self):
    """ Removing comments bottom 2. 
    By couting from last row to up and verifying 
    if it would be the first and unique column with data: source self.xl_array """
    nrows, ncols = self.get_nrows(), self.get_ncols()
    empty = False
    row_remove=[]
    for i in range(1, int(nrows*0.3)): 
      # raging up to 30% to the array seeking for comment section
      if not self.is_empty_row(-i):
        row_remove.append(-i)
      else:
        row_remove.append(-i)
        empty = True
        break
    if len(row_remove) and empty:
      self.xl_array = np.delete( self.xl_array, row_remove, axis = 0)
    else:
      print("There is no comment section apparently >", row_remove)

  def create_folder_outcome(self):
    """ Check whether the specified path exists or not. Create a new directory because it does not exist"""
    isExist = os.path.exists(self.url_bookoutside)
    if not isExist:
      os.makedirs(self.url_bookoutside)
  
  def get_titles_dataframe(self):
    nrows, ncols = self.get_nrows(), self.get_ncols()
    #print(list(map(chr, range(65, 91))))
    titles = np.array([i for i in range(ncols)] ).astype(str)
    return titles


  def default_dataframe_csv(self):
    """ Establishing a correlation of integer numbers as titles for dataframe """
    titles = self.get_titles_dataframe()

    df_polar = pl.from_numpy(data=self.xl_array, columns=titles.tolist(),)
    self.dataframe = df_polar
    print(df_polar)

    df_polar.write_csv(self.url_bookoutside+"/"+self.url_bookincome.split('/')[-1].split('.')[0]+'.csv')
  
  def there_are_repeated(self, titles:list):
    ini = len(titles)
    fin = len( list(set(titles)) )
    if ini == fin:
      return False
    else:
      return True

  def asign_correlative_row(self, titles:list):
    for i in range(len(titles)):
      titles[i] = titles[i]+"_"+str(i)
    return titles

  def custom_dataframe_csv(self, row=None, titles=None):
    """ row:int or titles:list Establishing a certain row within self.xl_array as titles for dataframe """
    if titles == None or row == None:
      if row != None:
        row = int(row)
        titles = self.xl_array[row].astype(str).tolist()
        data = self.xl_array[row+1:]
      else:
        data = self.xl_array
        titles = np.array(titles).astype(str).tolist()
        
      if self.there_are_repeated(titles):
        titles = self.asign_correlative_row(titles)
      
      df_polar = pl.from_numpy(data=data, columns=titles)
      self.dataframe = df_polar
      print(df_polar)
      df_polar.write_csv(self.url_bookoutside+"/"+self.url_bookincome.split('/')[-1].split('.')[0]+'.csv')
    else:
      print("Passed arguments is a must or both are not valid at the same time")

  def data_wrangling(self):
    self.remove_head_comments()
    self.remove_bottom_comments()

    self.remove_empty_cols()
    self.remove_empty_rows()

    self.extending_values_blanckspaces()
    self.extending_values_blanckspaces_col()
    
    self.data_normalization()
  
  def data_normalization(self):
    """It will swap: uppercase to lowercase, 
    blanckspace to underscore, and other"""
    self.xl_array = np.char.lower(self.xl_array)
    self.xl_array = np.char.strip(self.xl_array)
    self.xl_array = np.char.replace(self.xl_array, "-", "")
    self.xl_array = np.char.replace(self.xl_array, "  ", " ")
    self.xl_array = np.char.replace(self.xl_array, " ", "_")
    ##self.xl_array = np.char.replace(self.xl_array, ".", "")
    ##self.xl_array = np.char.replace(self.xl_array, ",", "")
  
