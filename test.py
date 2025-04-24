

def getConsultaationsForPatient(patient_id: int, consultations: list[Consultation]):
    # sort consultations by patient_id
    consultations.sort(key=lambda x: x.patient_id)
    # return consultations
    return consultations


def getConsultationsForDoctor(doctor_id: int, consultations: list[Consultation]):
    # sort consultations by doctor_id
    consultations.sort(key=lambda x: x.doctor_id)
    # return consultations
    return consultations


def scheduleConsultation(patient_id: int, date: datetime):
    # find a free slot for the consultation
    doctor = findDoctorForPatient(patient.condition)


def findDoctorForPatient(patient_id: int, doctors: list[Doctor]):
    # find a doctor for the patient depending on the patient's condition


# dict for doctor of what they specialize in
specialization = {
    "doctor_id": "specialization"
}

# object for treatment room
treatment_room = {
    "room_id": "room_name",
    "has_treatment_machine": True
}

# find a treatment room for the consultation
def findTreatmentRoomForConsultation(patient: Patient):

    # check condition of patient
    # find a room with the required treatment machine
    

# list of conditions that require a treatment machine
conditions_that_require_treatment_machine = [
    "condition_name": "treatment_machine_name"
]


