from faker import Faker


faker = Faker('ru_RU')

def generate_user_body():
    return {
        "email": f"{faker.user_name()}@yandex.ru",
        "password": faker.password(),
        "name": faker.user_name()
    }

def generate_random_email_password():
    return {
        "email": f"{faker.user_name()}@yandex.ru",
        "password": faker.password()
    }



class DataForOrder:
    
    VALID_INGREDIENTS = { 
    "ingredients": ["61c0c5a71d1f82001bdaaa6d", 
                    "61c0c5a71d1f82001bdaaa6f"] 
} 
    
    INVALID_INGREDIENT_HASH = {
    "ingredients": ["11а1а1a11а1а11111ааaaa1а"]
}

    WITHOUT_INGREDIENTS = {
    "ingredients": []
}
