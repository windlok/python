class movies:
    def __init__(self,title,director,duraction):
        self.title =title
        self.director =director
        self.duraction=duraction
        print("init olusuturuldu")

    def __str__(self,):
        return f'{self.title} by {self.director}'    
    
    def __len__(self):
        return self.duraction
    
    def __del__(self,):
        print("movies silindi")
m1=movies('film adi','yonetmen adi',120)

m1
print(str(m1))

"""print(len(m1))
del m1"""