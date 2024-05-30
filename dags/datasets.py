from airflow import Dataset

idezar_barrios_dataset = Dataset("data/IDEZAR/Barrios/raw/BARRIO_DELIMITACION.xml")
idezar_barrios_refined = Dataset("data/IDEZAR/Barrios/refined/BARRIO_DELIMITACION.csv")
idezar_barrios_rdf = Dataset("data/IDEZAR/Barrios/rdf/BARRIO_DELIMITACION.nt")

idezar_distritos_dataset = Dataset("data/IDEZAR/Distritos/raw/distritos.xml")
idezar_distritos_refined = Dataset("data/IDEZAR/Distritos/refined/distritos.csv")
idezar_distritos_rdf = Dataset("data/IDEZAR/Distritos/rdf/distritos.nt")

zgz_residencial_dataset = Dataset("data/ZGZ/Residencial/raw/01_BBDD_EnerEst_EResidenciales_2021_v001.xlsx")
zgz_residencial_refined = Dataset("data/ZGZ/Residencial/refined/01_BBDD_EnerEst_EResidenciales_2021_v001.csv")
zgz_residencial_rdf = Dataset("data/ZGZ/Residencial/rdf/01_BBDD_EnerEst_EResidenciales_2021_v001.csv")

rdf_combined = Dataset("data/rdf-file.nt")
