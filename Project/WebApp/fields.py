fields2 = ['coverimg', 'publishdate', 'title', 'author', 'edition', 'rating', 'language', 'isbn', 'genres', 'publisher', 'pages', 'setting', 'characters', 'bookformat', 'description', 'awards']
fields = {
    'admin': False,
    'html': {
        'title': ''
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

length = {'coverimg': 100, 'title': 45, 'author': 45, 'edition': 15, 'rating': 45, 'language': 45, 'isbn': 45, 'genres': 45, 'publisher': 15, 'pages': 45, 'setting': 20, 'characters': 45, 'bookformat': 45, 'description': 200, 'publishdate': 45, 'awards': 45}