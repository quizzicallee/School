max_chapter = 0
book_with_max = ''
with open("books_and_chapters.txt") as book_file:
    for line in book_file: 
        parts = line.split(":")
        books = parts[0].strip()
        chapters = int(parts[1].strip())
        scriptures = parts[2].strip()

        print(f'Scripture:{scriptures}, Book:{books}, Chapters:{chapters}')

        if chapters > max_chapter:
            max_chapter = chapters
            book_with_max = books

print(f'The book with the most chapter is:{book_with_max}')
print(f'It has {max_chapter} chapters')