import psycopg2
import json


# cursor = connection.cursor()
file = open("./voter_data/extra_voting_dates.txt",
            'r', encoding="ISO-8859-1")


if connection:
    # postgres_insert_query = "INSERT INTO test_app_user (name) VALUES (%s)"
    # records_to_insert = ('Dax',)
    # cursor.execute(postgres_insert_query, records_to_insert)
    # connection.commit()

    # cursor.execute('''DELETE FROM ivote_api_vote''')
    # connection.commit()

    i = 0
    records = []

    for each_line in file:
        line = each_line.split('\t')

        if i != 0:
            records_to_insert = (line[1], line[2], line[0],)
            records.append(records_to_insert)
            # state_voter_id, county_voter_id, title, f_name, m_name, l_name, name_suffix, birthdate, gender, st_num, st_frac, st_name, st_type, unit_type, st_post_direction,  unit_num, city, state, zip_code, county_code, precinct_code,  precinct_part, legislative_district, congressional_district,  registration_date, absentee_type,  last_voted, status_code

            if i % 40 == 0:
                postgres_insert_query = """INSERT INTO ivote_api_vote (state_voter_id, election_date, county_code) VALUES %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s;"""

                # postgres_insert_query = """INSERT INTO test_app_registered_voter (StateVoterID,	CountyVoterID, FName,	MName, LName,	NameSuffix,	Birthdate,	Gender,	RegStNum,	RegStFrac,	RegStName,	RegStType,	RegUnitType,	RegStPreDirection,	RegStPostDirection,	RegUnitNum,	RegCity,	RegState,	RegZipCode,	CountyCode,	PrecinctCode,	PrecinctPart,	LegislativeDistrict, CongressionalDistrict,	Registrationdate,	AbsenteeType,	LastVoted,	StatusCode) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

                # records_to_insert = (line[1], line[2], line[0],)

                cursor.execute(postgres_insert_query, records)
                connection.commit()
                records = []

        if i % 1000 == 0:

            print(i)

        # if i == 1000:
        #     break

        i += 1
    print(i)

    connection.commit()
    cursor.close()
    connection.close()
    print("PostgreSQL connection is closed")
