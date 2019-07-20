import psycopg2
import json

connection = psycopg2.connect(
    database='',
    user='',
    password='',
    host='',
    port='',)

cursor = connection.cursor()
file = open("", 'r', encoding="ISO-8859-1")


if connection:
    print('connection')
    cursor.execute('''DELETE FROM ivote_api_voter''')
    # postgres_insert_query = "INSERT INTO test_app_user (name) VALUES (%s)"
    # records_to_insert = ('Dax',)
    # cursor.execute(postgres_insert_query, records_to_insert)
    # connection.commit()

    # cursor.execute('''DELETE FROM ivote_voter''')
    # connection.commit()

    i = 0
    headers = []

    for each_line in file:
        line = each_line.split('\t')

        if i != 0:

                # state_voter_id, county_voter_id, title, f_name, m_name, l_name, name_suffix, birthdate, gender, st_num, st_frac, st_name, st_type, unit_type, st_post_direction,  unit_num, city, state, zip_code, county_code, precinct_code,  precinct_part, legislative_district, congressional_district,  registration_date, absentee_type,  last_voted, status_code

            postgres_insert_query = """INSERT INTO ivote_api_voter (state_voter_id, county_voter_id, f_name, m_name, l_name, name_suffix, birthdate, gender, st_num, st_frac, st_name, st_type, unit_type, st_pre_direction, st_post_direction, unit_num, city, state, zip_code, county_code, precinct_code, precinct_part, legislative_district, congressional_district, registration_date, absentee_type, last_voted, status_code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

            # postgres_insert_query = """INSERT INTO test_app_registered_voter (StateVoterID,	CountyVoterID, FName,	MName, LName,	NameSuffix,	Birthdate,	Gender,	RegStNum,	RegStFrac,	RegStName,	RegStType,	RegUnitType,	RegStPreDirection,	RegStPostDirection,	RegUnitNum,	RegCity,	RegState,	RegZipCode,	CountyCode,	PrecinctCode,	PrecinctPart,	LegislativeDistrict, CongressionalDistrict,	Registrationdate,	AbsenteeType,	LastVoted,	StatusCode) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

            records_to_insert = (line[0], line[1], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12], line[13], line[14],
                                 line[15], line[16], line[17], line[18], line[19], line[20], line[21], line[22], line[23], line[24], line[33], line[34], line[35], line[36],)

            cursor.execute(postgres_insert_query, records_to_insert)
            connection.commit()

        if i % 10 == 0:

            print(i)
        if i == 1000:
            break
        i += 1

    connection.commit()
    cursor.close()
    connection.close()
    print("PostgreSQL connection is closed")
