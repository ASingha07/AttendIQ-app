from src.database.config import superbase
import bcrypt


def hash_pass(pwd):
    return bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode()


def check_pass(pwd, hashed):
    return bcrypt.checkpw(pwd.encode(), hashed.encode())


def check_teacher_exists(username):
    # check for unique username
    response = superbase.table("teachers").select("username").eq("username", username).execute()
    return len(response.data) > 0


def create_teacher(username, password, name):

    data = { "username": username, "password": hash_pass(password), "name":name }
    response = superbase.table("teachers").insert(data).execute()
    return response.data


def teacher_login(username, password):
    response = superbase.table("teachers").select("*").eq("username", username).execute()

    if response.data:
        teacher = response.data[0]
        if check_pass(password, teacher["password"]):
            return teacher
    return None


def get_all_students():
    response = superbase.table("students").select("*").execute()
    return response.data


def create_student(new_name, face_embedding=None, voice_embedding=None):
    data = {"name": new_name, "face_embedding": face_embedding, "voice_embedding": voice_embedding}
    response = superbase.table("students").insert(data).execute()
    return response.data