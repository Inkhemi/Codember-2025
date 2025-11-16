"""
· Sólo usa letras minúsculas y dígitos.
· Nunca usa dígitos después de una letra (Una vez aparecen letras, la contraseña debe continuar solo con letras)
· Si usa dígitos, siempre los usa de forma igual o creciente (si sale un 3, ya no usará después un número menor)
· Si usa letras, siempre las usa en orden alfabético igual o creciente (si sale una "b" ya no podrá usar una "a", por ejemplo)
"""


def valid_pass():
    with open("log_reto_2.txt", "r") as log_file:
        true_cont = 0
        false_cont = 0
        for line in log_file:
            password = line.strip()
            if not password:
                continue
            char_seen = False
            last_digit = -1
            last_char = ""
            valid_pw = True
            for ch in password:
                if ch.isdigit():
                    if char_seen:
                        valid_pw = False
                        break
                    d = int(ch)
                    if d < last_digit:
                        valid_pw = False
                        break
                    last_digit = d
                elif 'a' <= ch <= 'z':
                    char_seen = True
                    if last_char and ch < last_char:
                        valid_pw = False
                        break
                    last_char = ch
                else:
                    # invalid character (not lowercase letter or digit)
                    valid_pw = False
                    break
            if valid_pw:
                true_cont += 1
            else:
                false_cont += 1

    values = f"submit {true_cont}true{false_cont}false"

    return values


print(valid_pass())
