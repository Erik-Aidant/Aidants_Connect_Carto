import re
import humanized_opening_hours as hoh


# CHOICE fields


def find_verbose_choice(choices: tuple, value: str):
    for choice in choices:
        if choice[1] == value:
            return choice[0]
    # raise Exception(f"error with choices for {value}")
    return None


# Float fields


def process_float(value: str):
    if value:
        value = value.replace(",", ".")
        return float(value)
    return None


# Phone number


def process_phone_number(value: str):
    """
    03 44 91 12 52
    03.23.52.24.05
    03-44-15-67-02
    3960 (Service 0,06 € / mn + prix appel)
    0810 25 59 80* (0,06 €/mn + prix appel)  Un conseiller vous répond du lundi au vendredi de 9h à 16h00. # noqa
    """
    value = value.replace(" ", "").replace(".", "").replace("-", "")
    # value = re.sub(r"\D", "", value)
    if len(value) < 10:
        return value
    else:
        return None


# Opening Hours


def process_opening_hours(opening_hours_string: str):
    """
    'Du lundi au vendredi : 09:00-12:00 et 14:00-16:30 / Samedi : 09:00-12:00'
    'Mo-Fr 09:00-12:00, 14:00-16:30 ; Sa 09:00-12:00'
    'du lundi au samedi matin'
    """
    # hoh.sanitize(opening_hours_string) ? https://github.com/rezemika/humanized_opening_hours/issues/38 # noqa
    opening_hours_string = opening_hours_string.replace(u"\xa0", u" ")
    opening_hours_string = re.sub(" h ", ":", opening_hours_string, flags=re.IGNORECASE)
    # opening_hours_string = re.sub("h ", ":00 ", opening_hours_string, flags=re.IGNORECASE) # sanitize can take care of it # noqa
    opening_hours_string = re.sub(
        " au ", "-", opening_hours_string, flags=re.IGNORECASE
    )
    opening_hours_string = opening_hours_string.replace(" à ", "-")
    opening_hours_string = re.sub(" et", ",", opening_hours_string, flags=re.IGNORECASE)
    opening_hours_string = re.sub(
        " puis de", ",", opening_hours_string, flags=re.IGNORECASE
    )
    opening_hours_string = re.sub(" de", "", opening_hours_string, flags=re.IGNORECASE)
    opening_hours_string = re.sub("le ", "", opening_hours_string, flags=re.IGNORECASE)
    opening_hours_string = opening_hours_string.replace(" :", "")
    opening_hours_string = opening_hours_string.replace("/", ";")
    opening_hours_string = opening_hours_string.replace("–", "-")
    opening_hours_string = re.sub("du", "", opening_hours_string, flags=re.IGNORECASE)
    opening_hours_string = re.sub(
        "lundis", "Mo", opening_hours_string, flags=re.IGNORECASE
    )
    opening_hours_string = re.sub(
        "lundi", "Mo", opening_hours_string, flags=re.IGNORECASE
    )
    opening_hours_string = re.sub(
        "mardis", "Tu", opening_hours_string, flags=re.IGNORECASE
    )
    opening_hours_string = re.sub(
        "mardi", "Tu", opening_hours_string, flags=re.IGNORECASE
    )
    opening_hours_string = re.sub(
        "mercredis", "We", opening_hours_string, flags=re.IGNORECASE
    )
    opening_hours_string = re.sub(
        "mercredi", "We", opening_hours_string, flags=re.IGNORECASE
    )
    opening_hours_string = re.sub(
        "jeudis", "Th", opening_hours_string, flags=re.IGNORECASE
    )
    opening_hours_string = re.sub(
        "jeudi", "Th", opening_hours_string, flags=re.IGNORECASE
    )
    opening_hours_string = re.sub(
        "vendredis", "Fr", opening_hours_string, flags=re.IGNORECASE
    )
    opening_hours_string = re.sub(
        "vendredi", "Fr", opening_hours_string, flags=re.IGNORECASE
    )
    opening_hours_string = re.sub(
        "samedi", "Sa", opening_hours_string, flags=re.IGNORECASE
    )
    opening_hours_string = re.sub(
        "samedis", "Sa", opening_hours_string, flags=re.IGNORECASE
    )
    opening_hours_string = re.sub(
        "dimanches", "Su", opening_hours_string, flags=re.IGNORECASE
    )
    opening_hours_string = re.sub(
        "dimanche", "Su", opening_hours_string, flags=re.IGNORECASE
    )
    return opening_hours_string.lower()


def process_service_schedule_hours(service_schedule_hours_string: str):
    """
    """
    if any(
        elem in service_schedule_hours_string.lower() for elem in ["de la structure"]
    ):
        return None
    return service_schedule_hours_string


def sanitize_opening_hours_with_hoh(opening_hours: str):
    """
    https://github.com/rezemika/humanized_opening_hours#basic-methods

    Cleans up the opening_hours string
    Must be close to the OSM format
    Returns an Exception if it fails to parse/sanitize the string

    '  mo-su 09:30-20h;jan off' --> 'Mo-Su 09:30-20:00; Jan off'
    'Tu 14h-16h' --> 'Tu 14:00-16:00'
    """
    sanitized_opening_hours = hoh.sanitize(opening_hours)
    hoh.OHParser(sanitized_opening_hours, locale="fr")  # fails if given a wrong format
    return sanitized_opening_hours


# Other fields


def process_support_access(value: str):
    """
    'accès en mairie aux heures d'ouverture et sur rendez vous'
    'Allocataires CAF'
    'Accès libre - accompagnement si besoin'
    'Accès libre / La consultation est limitée à 30 minutes par personne'
    'accès libre hors ateliers'
    """
    if any(elem in value.lower() for elem in ["libre"]):
        return "libre"
    if any(
        elem in value.lower()
        for elem in ["rdv", "rendez", "inscription", "réservation"]
    ):
        return "inscription"
    return ""


def process_support_mode(value: str):
    """
    'Accompagnement individuel et personnalisé'
    'accompagnement personnalisé sur demande'
    'Collectif et accompagnement individuel'
    'Individuel ou collectif'
    """
    if any(
        elem in value.lower() for elem in ["personnalisé", "individuel", "personnel"]
    ):
        return "individuel"
    if any(elem in value.lower() for elem in ["groupe", "collectif"]):
        return "collectif"
    return ""


def process_cost(value: str):
    """
    'Gratuit - Tarif d’adhésion annuelle : 6€'
    'Gratuit pour les habitants du Sud-Avesnois / abonnement annuel de 80 euros pour les personnes extérieures' # noqa
    """
    if value:
        if any(elem in value.lower() for elem in ["gratuit"]):
            return True
        if any(elem in value.lower() for elem in ["payant", "coût", "prix"]):
            return False
    return False