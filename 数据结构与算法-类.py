# class book:
#     def __init__(self,t,a,y,i):
#         self.title=t
#         self.author=a
#         self.year=int (y)
#         self.isbn=i


#     def bookmassage(self):
#         print(f"书名:{self.title}"+f" 作者:{self.author}"+f" 出版年份:{self.year}"+f" ISBN:{self.isbn}")
#         if self.year<=1970:
#             print("这本书是经典书籍.")
#         else:
#             print("这本书不是经典书籍.")
# book1=book("百年孤独","加西亚 马尔克斯","1967","978-3-16-138410-0")
# book2=book("Python编程","迈克尔 多赫提","2015","978-0-13-419044-0")

# book1.bookmassage()
# book2.bookmassage()

class shape:
    def __init__(self,a):
        self.color=a

    def area(self):
        return "Area not defined"

color1=shape("read")
print(color1.area())
