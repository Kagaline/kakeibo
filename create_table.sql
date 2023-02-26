CREATE TABLE transactions ( 
    id INTEGER PRIMARY KEY, 
    date TEXT NOT NULL,     
    amount REAL NOT NULL,   
    category TEXT NOT NULL, 
    description TEXT        
);
