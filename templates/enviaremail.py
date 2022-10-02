from email.message import EmailMessage
import smtplib

def enviar_email(email_destino,codigo):
    remitente = "quinterolf@uninorte.edu.co"
    destinatario = email_destino
    mensaje = "Ingrese el Siguiente Codigo: "+codigo+" Para Activar Su Cuenta"
    email = EmailMessage()
    email["From"] = remitente
    email["To"] = destinatario
    email["Subject"] = "Codigo de Activacion"
    email.set_content(mensaje)
    smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
    smtp.starttls()
    smtp.login(remitente, "Martin13")
    smtp.sendmail(remitente, destinatario, email.as_string())
    smtp.quit()