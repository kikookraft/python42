def validate_ingredients(ingredients: str) -> str:
    valid_elements = {"fire", "water", "earth", "air"}
    words = ingredients.lower().split()
    for word in words:
        if word in valid_elements:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
