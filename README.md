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
CIN DATE HEURE
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


### SCREENSHOT

  

![alt text](ScreenShotFrontPage.png)

  

### Usage
Clone Repository
> $ git clone https://github.com/khalilthabet/medical-practice.git

Install virtual environment
> python3 -m venv .

Activate The Environment
> source ./bin/activate

Install dependencies
> pip install matplotlib

Run Program
> cd medical-practice/Src && python3 M_P.py

### NOTES

In case there is an issue please submit an issue to this project and give us your feedback.