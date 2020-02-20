from book_library import Library

class Grader:
    def __init__(self, D, books_score):
        self.D = D
        self.books_score = books_score

    def grade(self, solution):
        """
        solution format is [(library_object, books_list), (..), ..]
        """
        score = 0
        d = self.D
        all_books = set()

        for lib, books_list in solution:
            d -= lib.signup
            if d <= 0:
                break

            i = 0  # number of days to ship books
            for book_id in books_list:
                if i >= d * lib.shipping_n:
                    break  # no more days left to ship books
                if book_id in all_books:
                    print('repeated book {}'.format(book_id))
                    i += 1
                    continue
                print('add book {}'.format(book_id))
                score += self.books_score[book_id]
                all_books.add(book_id)
                i += 1

        return score

if __name__ == '__main__':
    from input_parser import InputParser

    ip = InputParser('problem/a_example.txt')
    grader = Grader(ip.D, ip.book_scores)

    libs = ip.libs
    solution = [(libs[1], [5, 2, 3]), (libs[0], [0, 1, 2, 3, 4])]
    score = grader.grade(solution)
    print(score)
