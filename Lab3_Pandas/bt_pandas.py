import pandas as pd

csv= pd.read_csv('Lab3_Pandas/sample_data.csv')
json= pd.read_json("Lab3_Pandas/sample_data.json", lines=True)
excel= pd.read_excel("Lab3_Pandas/sample_data.xlsx")

def docCsv():
    print(csv)

def docJson():
    print(json)

def docExcel():
    print(excel)

def moTa(df):
    print(df.describe())
    print(df.info())

def tanXuat(df,cot):
    print("tần xuất các giá trị trong cột", cot)
    print(df[cot].value_counts())

def phuongSai(df,cot):
    print("Phương sai của cột", cot)
    print(df[cot].var())

def timMinMax(df,cot):
    print("Giá trị lớn nhất của cột", cot, "là:", df[cot].max())
    print("Giá trị nhỏ nhất của cột", cot, "là:", df[cot].min())

def soDongCot(df):
    print("Số dòng:", df.shape[0])
    print("Số cột:", df.shape[1])


def tachTheoDieuKien(df, cot, nguong):
    df1 = df[df[cot] > nguong]
    df2 = df[df[cot] <= nguong]
    return df1, df2
def lay2dong(df):
    print("In 2 dòng đầu tiên:")
    print(df.iloc[1:3])

def lay2cot(df):
    print(" In 2 cột đầu tiên:")
    print(df.iloc[:, 1:3])

def lay10dong(df):
    print(" In 10 dòng đầu tiên:")
    print(df.head(10))

docCsv() # đọc file csv
docJson() # đọc file json
docExcel() # đọc file excel

moTa(csv) # mô tả dataframe dùng hàm describe và info 

tanXuat(csv,'age') # dùng value_count
phuongSai(csv,'age') # dùng var tính phương sai
timMinMax(csv,'age') # dùng max, min
soDongCot(csv) # in số dòng và số cột
lay2cot(csv) # lấy 2 cột đầu tiên trong csv
lay10dong(csv)  # lấy 10 dòng đầu tiên trong csv
lay2dong(csv) # lấy 2 dòng đầu trong csv
print("Tách DataFrame theo tuổi > 30:") 
df1, df2 = tachTheoDieuKien(csv, "age", 30) # tách dữ liệu thành 2 dataframe với dữ liệu tuổi >30 và <=30
print("Tuổi > 30:\n", df1)
print("Tuổi <= 30:\n", df2)