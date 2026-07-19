def calculate_cpm(price: float, miles: int) -> tuple[float, str]:
    cpm = round(price / (miles / 1000), 2)
    label = "bom" if cpm <= 180 else "ruim"
    return cpm, label
