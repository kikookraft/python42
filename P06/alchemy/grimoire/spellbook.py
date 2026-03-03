def record_spell(spell_name: str, ingredients: str) -> str:
    # Late import or else KABOUM
    from .validator import validate_ingredients

    validation_result: str = validate_ingredients(ingredients)
    if "- VALID" in validation_result and "- INVALID" not in validation_result:
        return f"Spell recorded: {spell_name} ({validation_result})"
    return f"Spell rejected: {spell_name} ({validation_result})"
