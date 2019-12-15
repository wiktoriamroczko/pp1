from sms import SMS
from email import Email

sms = SMS(987654432,765654987)
sms.send('Informuję, że nasze czwartkowe spotkanie zostało odwołane.')

email = Email('nowak@onet.pl', 'kowalski@gmail.com', 'Spotkanie w czwartek')
email.send('Informuję, że nasze czwartkowe spotkanie zostało odwołane.')