CREATE TABLE
    players (
        id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
        name VARCHAR(40) NOT NULL,
        height integer NOT NULL,
        team VARCHAR(64) NOT NULL,
        active BOOLEAN NOT NULL
    );