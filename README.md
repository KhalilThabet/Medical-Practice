# <b>Medical-Practice</b>

  

### School Mini-Project coded in Python

A windows terminal application for a medical practice aiming at managing ressources and patient's appointments and store them in a database.

### DATABASE
The data of the appointments are stored in files inside the DATA directory.
### FORMAT

### patient.txt
```r
CIN | NOM | PRENOM | AGE | SEXE
``` 
### rdv.txt
```r
CIN | DATE | HEURE
```
### Historique_CIN.txt
```r
CIN | NOM | PRENOM | DATE | HEURE
MEDICAMENT | QUANTITE | DUREE
```
### Nbr_Consultation.txt
```r
MONTH | YEAR
```


### DEMO


https://user-images.githubusercontent.com/69755000/154850316-30e65ff8-5537-4570-9d6a-e7c9880d05fc.mp4


  

### Usage
Clone Repository
```linux 
> $ git clone https://github.com/khalilthabet/medical-practice.git
> $ cd src
```

Install virtual environment
```linux
> $ python3 -m venv .
```

Activate The Environment
```linux
linux   > $ source ./bin/activate
windows > Scripts\activate
```

Install dependencies
```linux
linux   > $ pip install matplotlib
windows > python3 -m pip install matplotlib
```
Run Program
```linux
> $ cd Src && python3 M_P.py
> Enter UNIX if you're using a Linux distribution or WINDOWS 
```

### NOTES

In case there is an issue please submit an issue to this project and give us your feedback.
