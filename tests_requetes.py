import requetes
import networkx as nx

G = requetes.json_vers_nx("data_100.txt")
def test_collaroteurs_communs():
    assert requetes.collaborateurs_communs(G, "Kevin Bacon", "Jack Lemmon")==set()
    assert requetes.collaborateurs_communs(G, "Kevin Bacon", "Holmes")==None
    assert requetes.collaborateurs_communs(G, "Al Pacino", "Larry Gates")=={'James Broderick'}
    assert requetes.collaborateurs_communs(G,"Vicki Wauchope","Mark Derwin")=={'Charles Durning'}

def test_collaborateurs_proches():
    print(requetes.collaborateurs_proches(G, "Jason Patric", 2))
    print(requetes.collaborateurs_proches(G, "Kevin Bacon", 1))
    assert requetes.collaborateurs_proches(G, "Jason Patric", 2)=={'Paul Winfield', 'James Murtaugh', 'Toni Kalem', 'Billy L. Sullivan', 'William Finley (actor)|William Finley', 'Randi Brooks', 'Sean Penn', 'William Hootkins', 'Brad Grunberg', 'Brad Sullivan', 'Sally Kirkland', 'Rich Steber', 'Curtis Armstrong', 'William Marshall (actor)|William Marshall', 'William "Billy" Benedict', 'John Ortiz|John Augstin Ortiz', 'Lisle Wilson', 'Scatman Crothers', 'Robert Clary', 'Tom Noonan', 'John Finn', 'James Mapes', 'Frederick Lawrence', 'Fred Meyers', 'Floyd L. Peterson', 'Dirk Bogarde', 'Ricky Jay', 'David Mauro', 'Paul Hirsch (actor)|Paul Hirsch', 'Austin Pendleton', 'Carrie Fisher', 'Sarah Douglas (actress)|Sarah Douglas', 'Ben Pesner', 'Ed Bakey', 'Bruce Payne', 'Larry D. Mann', 'Ray Jewers', 'Bill Walker (actor)|Bill Walker', 'Jennifer Jason Leigh', 'James Coburn', 'Tom Amandes', 'Peter DeLuise', 'Lionel Pina', 'Eileen Brennan', 'Joyce Brothers', 'Douglas Livingstone', 'Scott Walker', 
    'Milton Berle', 'Anita Barone', 'Kent O. Doering', 'Peter Kowanko', 'Paul Newman', 'Mary Davenport', 'Avon Long', 'Burt Young', 'Nicollette Sheridan', 'René Auberjonois', 'Chris Sarandon', 'Susan Peretz', 'Laura Silverman', 'Joseph King (actor)|Joseph King', 'Tim Robbins', 'Alfred Lynch', 'Raymond J. Barry', 'Frank Minucci', 'Lewis Fiander', 'Penelope Allen', 'Clark Gregg', 'Jack Kehoe', 'Carlos Lauchu', 'Dave Goelz', 'Rick Cramer (actor)|Rick Cramer', 'Telly Savalas', 'John Leguizamo', 'James Woods', 'Charles Durning', 'Orson Welles', 'Tom Spratley', 'Michael Mellinger', 'Rachel Roberts (actress)|Rachel Roberts', 'Beatrice Straight', 'Lukas Haas', 'Richard Jordan', 'Olivia Newton-John', 'Garrick Hagon', 'Pamela Roland', 'John Quade', 'Beulah Garrick', 'Peter Donat', 'Jay O. Sanders', 'Jaime Sánchez (actor)|Jaime Sánchez', 'William Sylvester', 'Colby Chester', 'Todd Zeile', "Robert O'Neil (actor)|Robert O'Neil", 'Jim Belushi', 'William Smith (actor)|William Smith', 'Frances Sternhagen', 'Eddie Deezen', 'John Ales', 'Jason Patric', 'Andy Parker (actor)|Andy Parker', 'Jack Collins (actor)|Jack Collins', 'Irving Metzman', 'Roscoe Lee Browne', 'Taylor Negron', 'Richard Carpenter (screenwriter)|Richard Carpenter', 'Bill Cobbs', 'Edward Herrmann', 'J. J. Johnston', 'Milo Ventimiglia', 
    'Mark Derwin', 'Nicholas Sadler', 'Oliver Reed', 'Lionel Mark Smith', 'Jon Polito', 'Ernie Hudson', 'Leslie Nielsen', 'William H. Macy', 'Penelope Ann Miller', 'Keith Britton', 'Dom DeLuise', 'Joseph Siravo', 'Cameron Diaz', 'Shane Rimmer', 'Olaf Pooley', 'Arch Johnson', 'Ron Lee (actor)|Ron Lee', 'Rawle D. Lewis', 'Mark Eden', 'Ta-Tanisha', 'Ray Charles', 'Terrence Mann', 'Melvyn Douglas', 'Mr. T', 'Melinda Lynch', 'Kevin Bacon', 'Erin Torpey', 'Daniel Stern (actor)|Daniel Stern', 'Elya Baskin', 'Stephanie Romanov', 'Jill Clayburgh', 'Jorge Porcel', 'Paul Bartel', 'Katherine Helmond', 'Gary Springer', "Kenneth O'Brien", 'Roy Thinnes', 'Charles Noland', 'Downtown Julie Brown', 'Johnny Kassir|John Kassir', 'Robert De Niro', 'Peter Gallagher', 'Ray Santiago', 'Lesley Ann Warren', 'Anne Bancroft', 'Sully Boyar', 'Arielle Kebbel', 'George Pravda', 'Larry Walsh', 'Jonathan Penner', 'Judith Malina', 'Simon Scott (actor)|Simon Scott', 'Marcia Gay Harden', 'Sally Stevens', 'Michael Bradshaw', 'Tom Mardirosian', 'Hard Boiled Haggerty|H.B. Haggerty', 'Philip Seymour Hoffman', 'Richard Jaeckel', 'Josef Sommer', 'Steven Anderson', 'Ed Devereaux', 'Lacey Chabert', 'Dana Elcar', 'David Paymer', 'Maria Perschy', 'Robert MacLeod (actor)|Robert MacLeod', 'Carol Kane', 'Patti LuPone', 'Joe Tornatore', 'Jim Henson', 'Edwin Malave|Edwin "Chu Chu" Malave', 'Castulo Guerra', 
    'Vicki Wauchope', 'David Ogden Stiers', 'Dimitra Arliss', 'Hulk Hogan', 'Alec Baldwin', 'Art LaFleur', 'Frank Converse', 'Phil Brown (actor)|Phil Brown', 'Adrian Pasdar', 'Catherine Gaffigan', 'Rex Everhart', 'Ron Perlman', 'Marcia Jean Kurtz', 'James Rebhorn', 'Roger Clinton, Jr.|Roger Clinton', 'Robert Sherman (writer)|Robert Sherman', 'Claude Brooks', 'Ray Walston', 'Steven Lambert', 'Matthew Carey (actor)|Matthew Carey', 'Allen Garfield', 'Charles Haid', 'Luis Guzmán', 'Ingrid Rogers', 'Colin Blakely', 'Dabney Coleman', 'Mel Brooks', 'Al Pacino', 'Barry Bostwick', 'George Mikell', 'Melinda Dillon', 'Drew W. Wesche', 'Paul Eliopoulos', 'Angela Visser', 'Nora Dunn', 'Jack White (musician)|Jack White', 'Thuy Trang', 'Michael Higgins (actor)|Michael Higgins', 'Robert Earl Jones', 'Lori Singer', 'Frank Oz', 'Margaret Whiting (actress)|Margaret Whiting', 'Richard Pryor', 'Barnard Hughes', 'Paulene Myers', 'Arnold Marlé', 'Pat Morita', 'Andrew Christian English', 'Ed Bishop', "Gerald S. O'Loughlin", 'Richard A. Dysart', 'Rich Demarest', 'Dominic Chianese', 'Steve Buscemi', 'Annie McEnroe', 'Candice Bergen', 'Justine Johnston', 'Mason Gamble', 'Lionel Murton', 'Jean Rasey', 'Brett Tabisel', 'Michael Richardson', 'Tina Arning', 'Edward Herrmann|Ed Herrmann', 'Robert Guillaume', 'Joanna Cook Moore', 'Robert Costanzo', 'Sandra Kazan', 
    'Rebecca Pidgeon', 'William Finley (actor)|Bill Finley', 'Mark Russell', 'Jason Alexander', 'Wayne Cotter', 'Charles Dierkop', 'Alex Trebek', 'Jennifer Salt', 'John Mahoney', 'Greg Mullavey', 'Weston Gavin', 'Mary Kay Place', 'William Atherton', 'Bruce Gray', 'Tony Beckley', 'Joey Dente', 'Cloris Leachman', 'Joyce Davis', 'Philip Charles MacKenzie', 'Gary Harper', 'Michael Berryman', 'David Baxt', 'John Travolta', "Ron O'Neal", 'John Petievich', 'Ken Sansom', 'Caroll Spinney', 'Allan Dean Moore', 'Jihmi Kennedy', 'Alexei Sayle', 'Addison Powell', 'John Goodman', 'Lara Parker', 'Jim True-Frost|Jim True', 'Rolfe Sedan', 'Jerry Nelson', 'James Frawley', 'Charles McGraw', 'Paul Williams (songwriter)|Paul Williams', 'Elliott Gould', 'Carl Ciarfalio', 'Robert Culp', 'Sarah Jessica Parker', 'Wallace Shawn', 'Julia Stiles', 'Lee Paul', 'Burgess Meredith', 'Charles Aidman', 'Courtney B. Vance', 'Amy Levitt', 'Alan Oppenheimer', 'Edgar Bergen', 'Patrick Tatten', 'Mark Harmon', 
    'Lupe Ontiveros', 'Richard Widmark', 'Robert Shaw (actor)|Robert Shaw', 'James Broderick', 'Harry Bugin', 'The Umbilical Brothers|David Collins', 'Richard Marner', 'David Healy (actor)|David Healy', 'Bruce Kirby (actor)|Bruce Kirby', 'Patrick Cranshaw', '"Weird Al" Yankovic', 'Jan McGill', 'James LeGros', 'Willoughby Gray', 'Stephen Elliott (actor)|Stephen Elliott', 'Michael Lee Gogin', 'Fabio Lanzoni', 'Morgan Paull', 'Talisa Soto', 'Olympia Dukakis', 'Lance Henriksen', 'Dennis Cleveland Stewart|Dennis Stewart', 'Margot Kidder', 'Dolph Sweet', 'Robert Redford', 'John Ratzenberger', 'Clyde Kusatsu', 'Herbert Nelson', 'Leonard Barr', 'Harold Gould', 
    'Burt Lancaster', 'Tom Hanks', 'Joseph Cotten', 'Bill Durks', 'Herbert Morrison (announcer)|Herbert Morrison', 'Ferdy Mayne', 'Johnny G', 'Thomasine Heiner', 'Richard Hunt (puppeteer)|Richard Hunt', 'Alex Solowitz', 'Gary Cockrell', 'Gig Young', 'John Krasinski', 'Danso Gordon', 'Zoe Saldana', 'Ricky Parker', 'Keith Campbell', 'Mark Margolis', 'Gene Hackman', 'Elizabeth Halliday', 'Jonathan Katz', 'Michael Milhoan', 'Burt Reynolds', 'Nigel Stock (actor)|Nigel Stock', 'John Cazale', 'Leif Erickson (actor)|Leif Erickson', 'Colleen Dewhurst', 'Jami Gertz', 'Viggo Mortensen', 'Don Fellows', 'Pete Cody', 'Bruce Campbell', 'Reginald Beckwith', 'Sam Raimi', 'Bernard Archard', 'Bruce D. Price', 'George C. Scott', 'Estelle Omens', 'Madeline Kahn', 'Stephen Burrows (actor)|Stephen Burrows', 'Burt Richards', 'Dick Anthony Williams', 'James Sloyan|James J. Sloyan', 'Gerrit Graham', 'Wes Robinson', 'David L. Lander', 'Glenn Beck (actor)|Glenn Beck', 'Richard Bright (actor)|Richard Bright', 'Ron Eldard', 'Annabeth Gish', 'Bill Paxton', 'M. Phil Senini', 'Andy Griffith', 'Donald Sutherland', 'Anna Nicole Smith', 'John Marriott (actor)|John Marriott', 'William Barillaro', 'Belinda Bauer (actress)|Belinda Bauer', 'Bob Hope', 'John Heffernan', 'Christopher Wynne', 'Steve Martin'}
    assert requetes.collaborateurs_proches(G, "Kevin Bacon", 1)=={'Frances Sternhagen', 'Ben Pesner', 'Mary Kay Place', 'Kevin Bacon', 'Burt Reynolds', 'Charles Durning', 'Jay O. Sanders', 'Daniel Stern (actor)|Daniel Stern', 'Jill Clayburgh', 'Candice Bergen', 'Austin Pendleton', 'Wallace Shawn'}

def test_est_proche():
    assert requetes.est_proche(G,'Jason Patric', 'Lara Parker',  1)==False
    assert requetes.est_proche(G,'Jason Patric', 'Lara Parker',  2)==True
    assert requetes.est_proche(G,'Jason Patric', 'Kevin Bacon',  4)==False

def test_distance_naive():
    assert requetes.distance_naive(G, 'Jason Patric', 'Lara Parker')==2
    assert requetes.distance_naive(G, "Richard Bauman", "Anne Francis")==1
    assert requetes.distance_naive(G, "Al Pacino", "Jack Kehoe")==1
    assert requetes.distance_naive(G, "Al Pacino", "Katie Holmes")==1

def test_distance():
    assert requetes.distance(G, "Al Pacino", "Katie Holmes")==1

def test_centralite():
    assert requetes.centralite(G, "Kevin Bacon")==4
    assert requetes.centralite(G, "Al Pacino")==2
    assert requetes.centralite(G, "Alicia Witt")==7
    assert requetes.centralite(G, "Karen Allen")==8
    assert requetes.centralite(G, "Tracy Morgan")==3
    assert requetes.centralite(G, "Paul Newman")==6
    assert requetes.centralite(G, "Holmes")==None

def test_centre_hollywood():
    assert requetes.centre_hollywood(G)=='Kevin Bacon'

def test_eloignement_max():
    assert requetes.eloignement_max(G)==9



