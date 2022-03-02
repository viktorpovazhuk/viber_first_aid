from parse_medical_data.read_medical_data import ReadMedicalData

def main():
    medical_data = ReadMedicalData().get_medical_data()

    c = medical_data.get_begin_options()
    d = medical_data.get_next_options("Серцево-легенева реанімація дитини")
    a = 1
    b = a

if __name__ == "__main__":
    main()