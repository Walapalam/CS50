MONTHS: list[str] = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def get_month_numeral(_m: str) -> int:
    for i in range(len(MONTHS)):
        if _m == MONTHS[i]:
            return i + 1

def is_valid_date(m: int, d: int) -> bool:
    return (int(m) > 0 and int(m) < 13) and (int(d) > 0 and int(d) < 32)


while True:
    date: str = input("Date: ").strip()
    try:
        m, d, y = date.split("/")
        if is_valid_date(m, d): break

    except Exception:
        try:
            _m, _d, y = date.split(" ")

            if "," in date:
                d: str = _d.replace(",", "")
                m: int = get_month_numeral(_m)
                if is_valid_date(m, d): break
        except Exception:
            pass

print(f"{y}-{int(m):02}-{int(d):02}")