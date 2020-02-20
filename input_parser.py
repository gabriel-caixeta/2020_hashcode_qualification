from book_library import Library

class InputParser:
    def __init__(self, in_file):
        libs = []
        D = 0
        
        with open(in_file, 'r') as f:
            B, L, D = f.readline().split()
            B, L, D = int(B), int(L), int(D)

            book_scores = f.readline().split()
            book_scores = [int(bs) for bs in book_scores]
            book_scores = {book_id: score for book_id, score in enumerate(book_scores)}

            for _ in range(L):
                num_books, signup_time, books_per_day = f.readline().split()
                num_books, signup_time, books_per_day = int(num_books), int(signup_time), int(books_per_day)

                books_list = f.readline().split()
                books_list = [int(b) for b in books_list]
                books_set = set(books_list)
                lib_books_score = {id: book_scores[id] for id in book_scores if id in books_set}
                lib = Library(lib_books_score, signup_time, books_per_day, _)
                lib.score_books(book_scores)
                libs.append(lib)
        
        
        self.libs = libs
        self.book_scores = book_scores
        self.D = D
        self.book_scores = book_scores
