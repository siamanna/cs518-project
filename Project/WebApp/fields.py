

fields = {
    'admin': False,
    'html': {
        'title': '',
        'method': 'POST'
    },
    'coverimg': {
        'display': 'Cover',
        'type': 'string',
        'max': 200,
        'case': 'unchanged'
    }, 
    'publishdate': {
        'display': 'Date Published',
        'type': 'date',
        'max': 45,
        'case': 'lower'
    }, 
    'title':{
        'display': 'Title',
        'type': 'string',
        'max': 45,
        'case': 'title'
    },  
    'author':{
        'display': 'Author',
        'type': 'string',
        'max': 45,
        'case': 'title'
    }, 
    'edition':{
        'display': 'Edition',
        'type': 'string',
        'max': 45,
        'case': 'title'
    },  
    'rating':{
        'display': 'Rating',
        'type': 'float',
        'max': 45,
        'case': 'lower'
    },  
    'language':{
        'display': 'Language',
        'type': 'string',
        'max': 45,
        'case': 'title'
    },  
    'isbn':{
        'display': 'ISBN',
        'type': 'integer',
        'max': 45,
        'case': 'lower'
    },  
    'genres':{
        'display': 'Genres',
        'type': 'string',
        'max': 45,
        'case': 'title'
    }, 
    'publisher':{
        'display': 'Publisher',
        'type': 'string',
        'max': 45,
        'case': 'title'
    },  
    'pages':{
        'display': 'Pages',
        'type': 'integer',
        'max': 45,
        'case': 'lower'
    }, 
    'setting':{
        'display': 'Setting',
        'type': 'string',
        'max': 45,
        'case': 'title'
    },  
    'characters':{
        'display': 'Characters',
        'type': 'string',
        'max': 45,
        'case': 'title'
    },  
    'bookformat':{
        'display': 'Format',
        'type': 'string',
        'max': 45,
        'case': 'title'
    }, 
    'description':{
        'display': 'Description',
        'type': 'string',
        'max': 45,
        'case': 'lower'
    }, 
    'awards': {
        'display': 'Awards',
        'type': 'string',
        'max': 45,
        'case': 'title'
    }
}

browse_categories = {
    'genres': {
        'options': ['All', '19th Century', 'Action', 'Adventure', 'Adult', 'Adult Fiction', 'Audiobook', 'Books About Books', 'British Literature', 'Chick Lit', 'Childrens', 'Christian', 'Christian Fiction', 'Classics', 'Comedy', 'Coming Of Age', 'Contemporary', 'Crime', 'Drama', 'Dystopia', 'Epic Fantasy', 'Fairy Tales', 'Fantasy', 'French Literature', 'Gothic', 'Greek Mythology', 'High Fantasy', 'Historical', 'Historical Fiction', 'Historical Romance', 'Holocaust', 'Horror', 'Humor', 'Japan', 'Juvenile', 'Kids', 'Latin American', 'Literary Fiction', 'Literature', 'Love', 'Magic', 'Magical Realism', 'Middle Grade', 'Mystery', 'Mystery Thriller', 'Novels', 'Paranormal', 'Paranormal Romance', 'Philosophy', 'Picture Books', 'Poetry', 'Politics', 'Post Apocalyptic', 'Realistic Fiction', 'Read For School', 'Romance', 'School', 'Science Fiction', 'Science Fiction Fantasy', 'Short Stories', 'Spanish Literature', 'Supernatural', 'Suspense', 'Teen', 'Thriller', 'Time Travel', 'Urban Fantasy', 'Vampires', 'War', 'World War II', 'Young Adult'],
        'category': 'genres'
    },
    'author': {
        'options': ['All', 'A.A. Milne',
            'Aldous Huxley',
            'Alice Sebold',
            'Alice Walker',
            'Anita Diamant',
            'Anthony Burgess',
            'Antoine de Saint-Exupéry',
            'Arthur Conan Doyle',
            'Arthur Golden',
            'Barbara Kingsolver',
            'Betty Smith',
            'Bram Stoker',
            'Cassandra Clare',
            'Charles Dickens',
            'Charlotte Brontë',
            'Cormac McCarthy',
            'Dan Brown',
            'Daphne du Maurier',
            'Diana Gabaldon',
            'Douglas Adams',
            'E.B. White',
            'Edgar Allan Poe',
            'Emily Brontë',
            'Ernest Hemingway',
            'F. Scott Fitzgerald',
            'Frances Hodgson Burnett',
            'Frank Herbert',
            'Frank McCourt',
            'Fyodor Dostoyevsky',
            'Gabriel García Márquez',
            'George Orwell',
            'George R.R. Martin',
            'Herman Melville',
            'Hermann Hesse',
            'Homer',
            'J.D. Salinger',
            'J.K. Rowling',
            'Jane Austen',
            'Jodi Picoult',
            'John Green',
            'John Irving',
            'John Steinbeck',
            'Joseph Heller',
            'J.R.R. Tolkien',
            'Ken Follett',
            'Ken Kesey',
            'Khaled Hosseini',
            'Kurt Vonnegut Jr.',
            'L.M. Montgomery',
            'Leo Tolstoy',
            'Lewis Carroll',
            'Lois Lowry',
            'Louisa May Alcott',
            'Madeleine LEngle',
            'Margaret Atwood',
            'Margaret Mitchell',
            'Mark Twain',
            'Markus Zusak',
            'Mary Wollstonecraft Shelley',
            'Maurice Sendak',
            'Miguel de Cervantes Saavedra',
            'Nicholas Sparks',
            'Oscar Wilde',
            'Orson Scott Card',
            'Paulo Coelho',
            'Philip Pullman',
            'Ray Bradbury',
            'Rick Riordan',
            'Richard Adams',
            'Roald Dahl',
            'S.E. Hinton',
            'Sara Gruen',
            'Shel Silverstein',
            'Stephen Chbosky',
            'Stephen King',
            'Stephenie Meyer',
            'Sue Monk Kidd',
            'Sylvia Plath',
            'Suzanne Collins',
            'Veronica Roth',
            'Vladimir Nabokov',
            'William Goldman',
            'William Golding',
            'William Shakespeare',
            'Yann Martel'],
        'category': 'author'
    },
    'rating': {
        'options': ['1 star and above', '2 stars and above', '3 stars and above', '4 stars and above', 'All'],
        'category': 'rating'
    }
}

eventvariables = {
    'eventname': {
        'display': 'Event Name',
        'type': 'string',
        'max': 45,
        'case': 'title'
    },

    'eventcatchphrase': {
        'display': 'Event Name',
        'type': 'string',
        'max': 45,
        'case': 'title'
    },

    'eventtime': {
        'display': 'Event Time',
        'type': 'time',
        'max': 45,
        'case': 'lower'
    },


    'eventdate': {
        'display': 'Event Date',
        'type': 'date',
        'max': 45,
        'case': 'lower'
    },

    'eventdescription':{
        'display': 'Event Description',
        'type': 'string',
        'max': 45,
        'case': 'lower'
    }
}





