import argparse
import csv
from dateutil.parser import parse
from registration.models import Participant


def import_participants(csv_file):
    with open(csv_file, 'r', encoding='UTF-8') as f:
        csv_reader = csv.DictReader(f, fieldnames=['Timestamp', 'FullName', 'Email', 'Phone', 'Occupation', 'Position', 'Organization', 'InvitationRequired'])
        next(csv_reader, None)
        for row in csv_reader:
            participant = Participant(
                registration_date_time = parse(row['Timestamp']),
                full_name = row['FullName'],
                email = row['Email'],
                phone_number = row['Phone'],
                occupation = row['Occupation'],
                position = row['Position'],
                organization = row['Organization'],
                invitation_required = row['InvitationRequired'] == 'True',
                is_checked_in = False,
            )
            participant.save()
