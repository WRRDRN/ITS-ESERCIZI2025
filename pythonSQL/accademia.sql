create type Strutturato as
    enum ('Ricercatore', 'Professore Associato', 'Professore Ordinario');

create type LavoroProgetto as
    enum ('Ricerca e Sviluppo','Dimostrazione','Management','Altro');

create type LavoroNonProgettuale as
    enum ('Didattica','Ricerca','Missione','Incontro Dipartimentale','Incontro Accademico','Altro');

create type CausaAssenza as
    enum ('Chiusura Universitaria','Maternità','Malattia');

create domain PosInteger as integer
    check (value >=0);

create domain StringaM as varchar(100);

create domain NumeroOre as integer
    check (value >=0 and value <=8);

create domain Denaro as integer
    check (value >=0);

create table Persona(
    id PosInteger, 
    nome StringaM,
    cognome StringaM,
    posizione Strutturato,
    stipendio Denaro,


    primary key (id)
);

create table Progetto(
    id PosInteger,
    nome StringaM,
    inizio date,
    fine date,
    budget Denaro,

     primary key(id),
     unique(nome),
     check(inizio<fine)


);

create table WP(
    progetto PosInteger,
    id PosInteger,
    nome StringaM,
    inizio date,
    fine date,
    foreign key (progetto) references Progetto(id),
    unique (progetto,nome),
    check (inizio<fine)
);

create table AttivitaProgetto (
    id PosInteger not null,
    persona PosInteger not null,
    progetto PosInteger not null,
    wp PosInteger not null,
    giorno date not null,
    tipo LavoroProgetto not null,
    oreDurata NumeroOre not null,
    primary key (id),
    foreign key (persona) references Persona(id) deferrable,
    foreign key (progetto, wp) references WP(progetto, id) deferrable
);

create table AttivitaNonProgettuale(
    id PosInteger,
    persona PosInteger,
    tipo LavoroNonProgettuale, 
    giorno date,
    oreDurata NumeroOre,

    foreign key (persona) references Persona(id)
);

create table Assenza (
    id PosInteger,
    persona PosInteger,
    tipo CausaAssenza,
    giorno date,
    unique(persona,giorno),
    foreign key (persona) references Persona(id)
);
