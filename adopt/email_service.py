from django.core.mail import send_mail


def send_confirmation_email(adopt):
    subject = "Adoção realizada com sucesso!"
    content = f"Parabéns por realizar a adoção do pet {adopt.pet.name} com o valor mensal de R${adopt.amount}"
    sender = "adote.pet.rn@gmail.com"
    recipients = [adopt.email]
    send_mail(subject, content, sender, recipients)