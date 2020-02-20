from math import floor

class Library:
    def __init__(self,books_score,T_signup,M_shipping_n,id):
        self.signup = T_signup
        self.shipping_n = M_shipping_n
        self.books_score = books_score
        self.grade = 0
        self.id = id

    def score_books(self,total_score):
        self.grade_library()
        return
        # for id, score in enumerate(total_score):
        #     if id in self.books:
        #         self.books_score.update({id: score})
        # self.books_score = {k: v for k, v in sorted(self.books_score.items(), key=lambda item: item[1])}
        # self.grade_library()
        
    def grade_library(self):
        self.grade = (self.shipping_n*sum(self.books_score.values()))/(self.signup)

    def get_scanned_books(self,total_days,books_already_scanned):
        n_scanned_books = floor((total_days-self.signup)*self.shipping_n)
        if n_scanned_books < 0:
            self.scanned_books = []
            return
        # print(total_days,self.signup,self.shipping_n,n_scanned_books)
        # simple solution that does not consider books already scanned by other libraries
        # self.scanned_books = self.books_score.keys()[:n_scanned_books]

        # check if the books were already scanned
        available_books = list(set(self.books_score.keys()) - set(books_already_scanned))
        self.scanned_books = available_books[:n_scanned_books]
        
        self.get_score()
        
    def get_score(self):
        self.score = 0
        for book in self.scanned_books:
            self.score += self.books_score[book]
    
    def update_score(self,all):
        pass