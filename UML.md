# modelleringsuppgift 

# UML

### Patient 

* Representerar en patient i systemet
* - Attribut:
    * - namn: String
    * - condition: Enum

### Doctor

* Representerar en läkare i systemet
* - Attribut:
    * - namn: String
    * - roll: Enum

### Treatmentroom

* Representerar en behandlingslokal i systemet
* - Attribut:
    * - roomId: String
    * - hasTreatmentMachine: Boolean

### Consultation

* Representerar en schemalagd konsultation mellan patient och läkare
* - Attribut:
    * - patient: Patient
    * - doctor: Doctor
    * - room: Treatmentroom
    * - date: Date

* Responsibiliies: Länkar en patient, läkare och behandlingslokal till en specifik tidpunkt och skapar en konsultation. 

### Hospital 

* Innehåller en lista av alla patienter, läkare och behandlingslokaler. 

* - Attribut:
    * - patients: List<Patient>
    * - doctors: List<Doctor>
    * - rooms: List<Treatmentroom>
    * - consultations: List<Consultation>

### Condition

* Representerar en tillstånd eller sjukdom som en patient kan ha

* Values: Cancer, Heart disease, Diabetes, Stroke, etc.

### DoctorRole

* Representerar en roll som en läkare kan ha

* Values: Oncologist, Cardiologist, Endocrinologist, etc.

# Relationer

* Patient -> Consultation: one-to-many
* Doctor -> Consultation: one-to-many
* Treatmentroom -> Consultation: one-to-many


# Implementering

1. Registrera patient

* Hospital har en metod, registreraPatient(name: String, condition: Condition)
* Skapar en ny Patient med namn och tillstånd
* Anropar metod bokaKonsultation(patient: Patient, date: Date)
  - Hittar en tillgänglig läkare som matchar patientens tillstånd
  - Hittar en tillgänglig behandlingslokal
  - Skapar en ny Consultation med patient, läkare och behandlingslokal
  - Lägger till Consultationen i listan av konsultationer
  - Returnerar Consultationen
* Lägger till patienten i listan av patienter

2. Lista konsultationer

* Hospital har en metod, listaKonsultationer()
* Returnerar en lista av alla konsultationer

