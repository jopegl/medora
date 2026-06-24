from django.contrib.auth import get_user_model

Doctor = get_user_model()

def create_doctor(
        username:str,
        password:str,
        email:str,
        crm:str="",
        **extra_fields
):
    doctor = Doctor(
        username = username,
        email = email,
        crm = crm,
        **extra_fields
    )
    doctor.set_password(password)
    doctor.save()
    return doctor

def get_doctor_by_id(id):
    return Doctor.objects.filter(id=id).first()

def get_doctor_by_crm(crm):
    return Doctor.objects.filter(crm=crm).first()

def update_doctor(id, **fields):
    doctor = get_doctor_by_id(id)
    if doctor is None:
        return None
    
    for key, value in fields.items():
        if hasattr(doctor, key):
            setattr(doctor, key, value)
    
    doctor.save()
    return doctor

def delete_doctor(id):
    doctor = get_doctor_by_id(id)
    if doctor is None:
        return None
    
    deleted = doctor.delete()
    return deleted > 0