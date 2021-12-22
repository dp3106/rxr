dob_list = []


def get_last_id():
    if dob_list:
        last_dob = dob_list[-1]
    else:
        return 1
    return last_dob.id + 1


class Dob:
    def __init__(self, BOROUGH, Job_Type, Block, Lot, Zip_Code,
                 Work_Type, Permit_Status, Filing_Status, Permit_Type,
                 Permit_Subtype, Issuance_Date, Expiration_Date, Job_Start_Date,
                 LATITUDE, LONGITUDE, COUNCIL_DISTRICT, CENSUS_TRACT, NTA_NAME, year, BBL):
        self.id = get_last_id()
        self.BOROUGH = BOROUGH
        self.Job_Type = Job_Type
        self.Block = Block
        self.Lot = Lot
        self.Zip_Code = Zip_Code
        self.Work_Type = Work_Type
        self.Permit_Status = Permit_Status
        self.Filing_Status = Filing_Status
        self.Permit_Type = Permit_Type
        self.Permit_Subtype = Permit_Subtype
        self.Issuance_Date = Issuance_Date
        self.Expiration_Date = Expiration_Date
        self.Job_Start_Date = Job_Start_Date
        self.LATITUDE = LATITUDE
        self.LONGITUDE = LONGITUDE
        self.COUNCIL_DISTRICT = COUNCIL_DISTRICT
        self.CENSUS_TRACT = CENSUS_TRACT
        self.NTA_NAME = NTA_NAME
        self.year = year
        self.BBL = BBL

    @property
    def data(self):
        return {
            'id': self.id,
            'BOROUGH': self.BOROUGH,
            'Job_Type': self.Job_Type,
            'Block': self.Block,
            'Lot': self.Lot,
            'Zip_Code': self.Zip_Code,
            'Work_Type': self.Work_Type,
            'Permit_Status': self.Permit_Status,
            'Filing_Status': self.Filing_Status,
            'Permit_Type': self.Permit_Type,
            'Permit_Subtype': self.Permit_Subtype,
            'Issuance_Date': self.Issuance_Date,
            'Expiration_Date': self.Expiration_Date,
            'Job_Start_Date': self.Job_Start_Date,
            'LATITUDE': self.LATITUDE,
            'LONGITUDE': self.LONGITUDE,
            'COUNCIL_DISTRICT': self.COUNCIL_DISTRICT,
            'CENSUS_TRACT': self.CENSUS_TRACT,
            'NTA_NAME': self.NTA_NAME,
            'year': self.year,
            'BBL': self.BBL
        }
