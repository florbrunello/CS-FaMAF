from generator.identification import generate_identification_doctor
from generator.assistance import generate_assistance

class Doctor():
    def __init__(self):
        self.name, self.surname1, self.surname2, self.gender, self.medical_registration_number, self.healthcare_role, self.institution = generate_identification_doctor()

    def doctor_to_string(self):
        if self.gender == "M":
            return f"Médico: Dr. {self.name} {self.surname1} {self.surname2}. {self.medical_registration_number}. {self.healthcare_role}. {self.institution}\n"
        return f"Médico: Dra. {self.name} {self.surname1} {self.surname2}. {self.medical_registration_number}. {self.healthcare_role}. {self.institution}\n"
    
class Assistance():
    def __init__(self, birthdate):
        self.assistance_date, self.episode, self.hospital, self.health_center, self.registration, self.vin, self.model = generate_assistance(birthdate)

    def assistance_to_string(self):
        assistance = f"Fecha de ingreso: {self.assistance_date}\n"
        if self.episode is not None:
            assistance += f"Episodio: {self.episode}\n"
        if self.hospital is not None:
            assistance += f"Hospital: {self.hospital}\n"
        if self.health_center is not None:
            assistance += f"Centro de salud: {self.health_center}\n"
        if self.registration is not None:
            assistance += f"Matrícula del coche: {self.registration}\nModelo: {self.model}\nVIN: {self.vin}\n"

        return assistance
    
class HealthRecord():
    def __init__(self, birthdate):
        self.doctor = Doctor()
        self.assistance = Assistance(birthdate)

    def health_record_to_string(self):
        return self.doctor.doctor_to_string() + self.assistance.assistance_to_string()
