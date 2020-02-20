
from input_parser import InputParser
from book_library import Library

if __name__ == '__main__':
    print('START')
    inputs = ['e_so_many_books.txt']
    # inputs = ['a+_example+.txt']
    inputs.reverse()
    for input_file in inputs:
        ip = InputParser('problem/'+input_file)
        
        output_file = 'output_'+input_file
        # output_file = 'output_test.txt'
        
        book_scores = ip.book_scores
        
        libs = ip.libs
        # libs.sort(key=lambda lib: lib.signup)  # sort by signup time in ascending order
        libs.sort(key=lambda lib: -lib.grade)  # sort by library grade in descending order

        days_left = ip.D
        books = []
        score = 0
        output_content = []
        remaining_books = ip.book_scores
        for lib in libs:
            if days_left<0:
                break
            # print(lib.id, lib.grade)
            lib.get_scanned_books(days_left,books)
            if not lib.scanned_books:
                continue
            score += lib.score
            books += lib.scanned_books
            days_left -= lib.signup
            output_content.append('{} {}'.format(lib.id, str(len(lib.scanned_books))))
            output_content.append(' '.join([str(sb) for sb in lib.scanned_books]))
            # print('Score: {}; Library {} scans: {}'.format(score,lib.id,lib.scanned_books))
        
        output_content = [str(int(len(output_content)/2))] + output_content
        print('{}   Score: {}'.format(input_file,score))
        # print(output_content)
        with open(output_file,'w') as f_output:
            # f_output.writelines(output_content)
            for line in output_content:
                f_output.write(line+'\n')

